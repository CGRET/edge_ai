import numpy as np
from scipy import stats
import paramiko

# Configuration Info
scope_ip = "169.254.177.210"
device = "Jetson Nano"

# Info for the devices [IP Address, username, password]
device_info = {"Jetson Nano": ["192.168.55.1", "ubuntu", "ubuntu"],
               "Coral Dev Board": ["192.168.55.20", "mendel", "mendel"]}

# Benchmark tests and their corresponding startup commands
benchmarks = {"MobileNet": "cd /usr/src/tensorrt/bin && ./sample_uff_ssd_rect",
              "ResNet": "./trtexec --output=prob --deploy=../data/googlenet/ResNet50_224x224.prototxt --fp16 --batch=1",
              "VGG-19": "./trtexec --output=prob --deploy=../data/googlenet/VGG19_N2 --fp16 --batch=1" ,
              "Inception": "./trtexec --output=prob --deploy=../data/googlenet/inception_v4.prototxt --fp16 --batch=1"}

# SSH Setup
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host_ip = device_info[device][0]
username = device_info[device][1]
password = device_info[device][2]
ssh.connect(host_ip, username=username, password=password)

# Run the test bench
(stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./sample_uff_ssd_rect")

data = stdout.readlines()   # Grab the output from the test bench
data = data[18:-1]          # Trims the data to the outputs we care about (i.e. inference run times)

times = []
# Loop through the outputs and grab the times
for count in range(0, len(data)-1):
    # Takes the current element, splits it by spaces, then takes the second to last object and converts it to a float
    times.append(float(data[count].split()[len(data[count].split()) - 2]))

# Converts the times into meaningful statistics
test_stats = stats.describe(np.array(times))

print("SSD Mobilenet V2 Summary Statistics: ")
print("Count: ", test_stats.nobs)
print("Interval: ", test_stats.minmax)
print("Mean: ", test_stats.mean)
print("Variance: ", test_stats.variance)
print("Skewness: ", test_stats.skewness)
print("Kurtosis: ", test_stats.kurtosis)
