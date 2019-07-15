#!/usr/bin/env python

# Created by Nitish Vijai under the assistance of Lt. Col. Deyoung
# This script requires a Jetson Nano to run

# import packages
import paramiko
import logging
import datetime
import sys

# let the user know about output
print("Please wait...")
print("\n\nNow running the SSD MobileNet V2 TensorFlow benchmark...\n\n")

# get timestamp
time = datetime.datetime.now()
file = "JetsonNano_SSDMobileNetV2_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

# start logging and running benchmarks
orig_stdout = sys.stdout
sys.stdout = open(file, "w")
logger = logging.getLogger(__name__)
ssh = paramiko.SSHClient()
host="10.11.14.18"
user="nitish"
password="Vijai2001"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=password)
channel = ssh.get_transport().open_session()

count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./sample_uff_ssd_rect")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
    for l in line_buffered(stdout):
        print l
    count += 1

sys.stdout.close()
sys.stdout=orig_stdout

time = datetime.datetime.now()
file = "JetsonNano_ResNet50_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the ResNet-50 TensorFlow benchmark...\n\n")

sys.stdout = open(file, "w")
count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./trtexec --output=prob --deploy=../data/googlenet/ResNet50_224x224.prototxt --fp16 --batch=1")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
    for l in line_buffered(stdout):
        print l
    count += 1
    
sys.stdout.close()
sys.stdout=orig_stdout

time = datetime.datetime.now()
file = "JetsonNano_InceptionV4_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the Inception V4 PyTorch benchmark...\n\n")

sys.stdout = open(file, "w")

count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./trtexec --output=prob --deploy=../data/googlenet/inception_v4.prototxt --fp16 --batch=1")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
    for l in line_buffered(stdout):
        print l
    count += 1

sys.stdout.close()
sys.stdout=orig_stdout

time = datetime.datetime.now()
file = "JetsonNano_Vgg19_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the VGG-19 MXNet benchmark...\n\n")

sys.stdout = open(file, "w")

count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./trtexec --output=prob --deploy=../data/googlenet/VGG19_N2.prototxt --fp16 --batch=1")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
    for l in line_buffered(stdout):
        print l
    count += 1

sys.stdout.close()
sys.stdout=orig_stdout

time = datetime.datetime.now()
file = "JetsonNano_Unet_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the UNet Caffe benchmark...\n\n")

sys.stdout = open(file, "w")

count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./trtexec --uff=~/output_graph.uff --uffInput=input_1,1,512,512 --output=conv2d_19/Sigmoid --fp16")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
    for l in line_buffered(stdout):
        print l
    count += 1

sys.stdout.close()
sys.stdout=orig_stdout

time = datetime.datetime.now()
file = "JetsonNano_OpenPose_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the OpenPose benchmark...\n\n")

sys.stdout = open(file, "w")
count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./trtexec --output=Mconv7_stage2_L2 --deploy=../data/googlenet/pose_estimation.prototxt --fp16 --batch=1")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
    for l in line_buffered(stdout):
        print l
    count += 1

sys.stdout.close()
sys.stdout=orig_stdout

time = datetime.datetime.now()
file = "JetsonNano_SuperResolution_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the Super Resolution benchmark...\n\n")

sys.stdout = open(file, "w")
count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./trtexec --output=output_0 --onnx=./Super-Resolution-BSD500/super_resolution_bsd500.onnx --fp16 --batch=1")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
    for l in line_buffered(stdout):
        print l
    count += 1

sys.stdout.close()
sys.stdout=orig_stdout

time = datetime.datetime.now()
file = "JetsonNano_TinyYOLOv3_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the Tiny YOLO v3 benchmark...\n\n")

sys.stdout = open(file, "w")
count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd ~/deepstream_reference_apps/yolo && trt-yolo-app --flagfile=config/yolov3-tiny.txt")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
    for l in line_buffered(stdout):
        print l
    count += 1

sys.stdout.close()
sys.stdout = orig_stdout

# close SSH connection to Nano
ssh.get_transport().close()
ssh.close()