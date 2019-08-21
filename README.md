##Coral Dev Boards
###Windows
- Success with serial connection using Linux steps, except using PuttY and finding the right COM
    - It will show up under two COM ports, used the "enhance COM Port" to connect
- These use the MendelOS which is made by Google. In the "getting started guide", they say you can access the board
through USB but this only works on Linux.
    - It seems that Windows needs a driver to recognize the USB device, and Google did not make a driver. So, we have
    to try to SSH.
- For some reason, these devices would not create an IP for eth0 (the ethernet port), so I opened their network config
files (sudo nano /etc/network/interface) and added the following:


    auto eth0
    iface eth0 inet static
    address 192.168.55.x
    netmask 255.255.255.0
    broadcast 192.168.55.255
    gateway 192.168.55.254`
    
- I then restarted the device, and changed the ssh config file (sudo nano /etc/ssh/sshd_config) and changed
"Password Authentication" to "Yes" and "PubKeyAuthentication" to "No". This stops the OS from requiring a one time push
of keys using mdt, which windows cannot do because of driver issues

##Nano
- Had to download an compile MobileNet benchmark.
    - Had one error where we had to use vim to remove the "static" description from the gLogger variable.
- For the super resolution benchmark, makes sure the main folder resides withing the `/usr/src/tensortt/bin` folder.
    - Same with the U-Net Segmentation Benchmark
    
    