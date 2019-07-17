#!/usr/bin/env python

# Created by Nitish Vijai under the assistance of Lt. Col. Deyoung
# This script requires a Jetson Nano to run

# import packages
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import matplotlib.pyplot as plt
import pandas
import random
import paramiko
import logging
import datetime
import sys
import csv
import re

#singularity_csv = 'ssd-mobilenetv2.singularity.csv'
#native_csv = 'ssd-mobilenetv2.native.csv'

# let the user know about output
print("Please wait...")
print("\n\nNow running the SSD MobileNet V2 TensorFlow benchmark...\n")
print("This will take approximately 18 minutes to complete.\n\n")

# get file timestamp
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

ssd = []
count = 0
result = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./sample_uff_ssd_rect")
    def line_buffered(f):
        line_buf = ""
        while not f.channel.exit_status_ready():
            line_buf += f.read(1)
            if line_buf.endswith('\n'):
                yield line_buf
                line_buf = ''
# reads times and writes them to list            
    for l in line_buffered(stdout):
        print l
        for i in l.split():
            try:
                if l.startswith("Time taken for inference per run is "):
                    result = float(i)
                    ssd.append(result)
                    break                
            except:
                continue
    count += 1
# converts standard Python list into NumPy array
ssd_analysis = np.array(ssd)

# Data description - steps repeat for each benchmark

print(stats.describe(ssd_analysis))

sys.stdout.close()
sys.stdout=orig_stdout

print("SSD Mobilenet V2 Summary Statistics: ")
print "Count: ", stats.describe(ssd_analysis).nobs
print "Interval: ", stats.describe(ssd_analysis).minmax
print "Mean: ", stats.describe(ssd_analysis).mean
print "Variance: ", stats.describe(ssd_analysis).variance
print "Skewness: ", stats.describe(ssd_analysis).skewness
print "Kurtosis: ", stats.describe(ssd_analysis).kurtosis

time = datetime.datetime.now()
file = "JetsonNano_ResNet50_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the ResNet-50 TensorFlow benchmark...\n")

print("This will take approximately 12 minutes to complete. \n")

sys.stdout = open(file, "w")

rn50 = []
nums = []
p = re.compile(r'\d+.\d{4}')
count = 0
result = 0
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
        for i in l.split():
            try:
                if l.startswith("Average over 10 runs is "):
                    nums = [float(s) for s in p.findall(l)]
                    result = nums[0]
                    rn50.append(result)
                    break                
            except:
                continue
    count += 1

for x in range(len(rn50)):
    print rn50[x]

rn50_analysis = np.array(rn50)

print(stats.describe(rn50_analysis))
sys.stdout.close()
sys.stdout=orig_stdout

print("ResNet-50 Summary Statistics: ")
print "Count: ", stats.describe(rn50_analysis).nobs
print "Interval: ", stats.describe(rn50_analysis).minmax
print "Mean: ", stats.describe(rn50_analysis).mean
print "Variance: ", stats.describe(rn50_analysis).variance
print "Skewness: ", stats.describe(rn50_analysis).skewness
print "Kurtosis: ", stats.describe(rn50_analysis).kurtosis

time = datetime.datetime.now()
file = "JetsonNano_InceptionV4_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the Inception V4 PyTorch benchmark...\n")

print("This will take approximately 21 minutes to complete.\n")

sys.stdout = open(file, "w")

inc4 = []
numbers = []
p = re.compile(r'\d+.\d{3}')
count = 0
result = 0
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
        for i in l.split():
            try:
                if l.startswith("Average over 10 runs is "):
                    numbers = [float(s) for s in p.findall(l)]
                    result = numbers[0]
                    inc4.append(result)
                    break                
            except:
                continue
    count += 1

for x in range(len(inc4)):
    print inc4[x]

inc4_analysis = np.array(inc4)

print(stats.describe(inc4_analysis))

sys.stdout.close()
sys.stdout=orig_stdout

print("Inception V4 Summary Statistics: ")
print "Count: ", stats.describe(inc4_analysis).nobs
print "Interval: ", stats.describe(inc4_analysis).minmax
print "Mean: ", stats.describe(inc4_analysis).mean
print "Variance: ", stats.describe(inc4_analysis).variance
print "Skewness: ", stats.describe(inc4_analysis).skewness
print "Kurtosis: ", stats.describe(inc4_analysis).kurtosis

time = datetime.datetime.now()
file = "JetsonNano_Vgg19_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the VGG-19 MXNet benchmark...\n")

sys.stdout = open(file, "w")

count = 0
while count < 3:
    (stdin, stdout, stderr) = ssh.exec_command("cd /usr/src/tensorrt/bin && ./trtexec --output=prob --deploy=../data/googlenet/vgg19_N2.prototxt --fp16 --batch=1")
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

print("No summary statistics available for VGG-19.\n")

time = datetime.datetime.now()
file = "JetsonNano_Unet_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the UNet Caffe benchmark...\n")

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

print("U-Net benchmark not compatible with Jetson Nano.\n")

time = datetime.datetime.now()
file = "JetsonNano_OpenPose_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the OpenPose benchmark...\n")

print("This will take approximately 12 minutes to complete.\n")

sys.stdout = open(file, "w")
op = []
numeros = []
p = re.compile(r'\d+.\d{3}')
result = 0
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
        for i in l.split():
            try:
                if l.startswith("Average over 10 runs is "):
                    numeros = [float(s) for s in p.findall(l)]
                    result = numeros[0]
                    op.append(result)
                    break                
            except:
                continue
    count += 1

op_analysis = np.array(op)


sys.stdout.close()
sys.stdout=orig_stdout

print("OpenPose Summary Statistics: ")
print "Count: ", stats.describe(op_analysis).nobs
print "Interval: ", stats.describe(op_analysis).minmax
print "Mean: ", stats.describe(op_analysis).mean
print "Variance: ", stats.describe(op_analysis).variance
print "Skewness: ", stats.describe(op_analysis).skewness
print "Kurtosis: ", stats.describe(op_analysis).kurtosis

time = datetime.datetime.now()
file = "JetsonNano_SuperResolution_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the Super Resolution benchmark...\n")

print("This will take approximately 2 minutes to complete.\n")

sys.stdout = open(file, "w")
sr = []
numerals = []
result = 0
count = 0
p = re.compile(r'\d+.\d{4}')
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
        for i in l.split():
            try:
                if l.startswith("Average over 10 runs is "):
                    numerals = [float(s) for s in p.findall(l)]
                    result = numerals[0]
                    sr.append(result)
                    break                
            except:
                continue
    count += 1

sr_analysis = np.array(sr)

sys.stdout.close()
sys.stdout=orig_stdout

print("Super Resolution Summary Statistics: ")
print "Count: ", stats.describe(sr_analysis).nobs
print "Interval: ", stats.describe(sr_analysis).minmax
print "Mean: ", stats.describe(sr_analysis).mean
print "Variance: ", stats.describe(sr_analysis).variance
print "Skewness: ", stats.describe(sr_analysis).skewness
print "Kurtosis: ", stats.describe(sr_analysis).kurtosis

time = datetime.datetime.now()
file = "JetsonNano_TinyYOLOv3_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

print("\n\nNow running the Tiny YOLO v3 benchmark...\n")

print("This will take approximately 2 minutes to complete.\n")

sys.stdout = open(file, "w")

ty = []
decimals = []
p = re.compile(r'\d+.\d{4}')
count = 0
result = 0
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
        for i in l.split():
            try:
                if l.startswith("Network Type"):
                    decimals = [float(s) for s in p.findall(l)]
                    result = decimals[0]
                    ty.append(result)
                    break                
            except:
                continue
    count += 1

ty_analysis = np.array(ty)

sys.stdout.close()
sys.stdout = orig_stdout

print("Tiny YOLO v3 Summary Statistics: ")
print "Count: ", stats.describe(ty_analysis).nobs
print "Interval: ", stats.describe(ty_analysis).minmax
print "Mean: ", stats.describe(ty_analysis).mean
print "Variance: ", stats.describe(ty_analysis).variance
print "Skewness: ", stats.describe(ty_analysis).skewness
print "Kurtosis: ", stats.describe(ty_analysis).kurtosis

print("\n\nAll benchmarks complete. Closing remote connection.\n\n")

# close SSH connection to Nano
ssh.get_transport().close()
ssh.close()