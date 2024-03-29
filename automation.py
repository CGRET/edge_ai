import numpy as np
from scipy import stats
import paramiko
import re

# Configuration Info
scope_ip = "169.254.177.210"
device = "Jetson Nano"

# Info for the devices [IP Address, username, password]
device_info = {"Jetson Nano": ["192.168.55.1", "ubuntu", "ubuntu"],
               "Coral Dev Board": ["192.168.55.20", "mendel", "mendel"]}

# Benchmark tests and their corresponding startup commands
benchmarks = {"SSD Mobilenet V2": "cd /usr/src/tensorrt/bin && ./sample_uff_ssd_rect",
              "ResNet": "cd /usr/src/tensorrt/bin && "
                        "./trtexec --output=prob --deploy=../data/googlenet/ResNet50_224x224.prototxt --fp16 --batch=1",
              "VGG-19": "cd /usr/src/tensorrt/bin && "
                        "./trtexec --output=prob --deploy=../data/googlenet/vgg19_N2.prototxt --fp16 --batch=1",
              "Inception": "cd /usr/src/tensorrt/bin && "
                           "./trtexec --output=prob --deploy=../data/googlenet/inception_v4.prototxt --fp16 --batch=1",
              "OpenPose": "cd /usr/src/tensorrt/bin && "
                          "./trtexec --output=Mconv7_stage2_L2 --deploy=../data/googlenet/pose_estimation.prototxt"
                          " --fp16 --batch=1",
              "Super Resolution": "cd /usr/src/tensorrt/bin && ./trtexec --output=output_0 "
                                  "--onnx=./Super-Resolution-BSD500/super_resolution_bsd500.onnx --fp16 --batch=1",
              "U-Net Segmentation": "cd /usr/src/tensorrt/bin && ./trtexec --uff=./output_graph.uff "
                                    "--uffInput=input_1,1,512,512 --output=conv2d_19/Sigmoid --fp16"}

# SSH Setup
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host_ip = device_info[device][0]
username = device_info[device][1]
password = device_info[device][2]
ssh.connect(host_ip, username=username, password=password)
print("SSH Successful...\n")

print("Starting Benchmarks...")
for benchmark, command in benchmarks.items():
    print("\n" + benchmark + " Benchmark\n")
    (stdin, stdout, stderr) = ssh.exec_command(command)     # Run the benchmark
    data = stdout.readlines()   # Grab the output from the test bench
    times = []
    if benchmark == "SSD Mobilenet V2":
        data = data[18:-1]  # Trims the data to the outputs we care about (i.e. inference run times)
        for line in range(0, len(data)-1):  # Loop through the outputs and grab the times
            # Split each line by spaces, then takes the second to last element and converts it to a float
            times.append(float(data[line].split()[len(data[line].split()) - 2]))
    else:
        for line in data:
            if line.startswith("[I] Average"):
                p = re.compile(r'\d+.\d{3}')
                times.append(float(p.findall(line.split("(")[0])[0]))   # Grab the correct time and turn it to a float

    test_stats = stats.describe(np.array(times))  # Converts the times into meaningful statistics

    print(benchmark + " statistics: ")
    print("Count: ", test_stats.nobs)
    print("Interval: ", test_stats.minmax)
    print("Mean: ", test_stats.mean)
    print("Variance: ", test_stats.variance)
    print("Skewness: ", test_stats.skewness)
    print("Kurtosis: ", test_stats.kurtosis)
