## Coral Dev Boards

### Windows
- Success with serial connection using Linux steps, except using PuttY and finding the right COM
    - It will show up under two COM ports, used the "enhance COM Port" to connect
- These use the MendelOS which is made by Google. In the "getting started guide", they say you can access the board
through USB but this only works on Linux.
    - It seems that Windows needs a driver to recognize the USB device, and Google did not make a driver. So, we have
    to try to SSH.
- For some reason, these devices would not create an IP for eth0 (the ethernet port), so I opened their network config
files (sudo nano /etc/network/interface) and added the following:
```bash
    auto eth0
    iface eth0 inet static
    address 192.168.55.x
    netmask 255.255.255.0
    broadcast 192.168.55.255
    gateway 192.168.55.254`
```    
- I then restarted the device, and changed the ssh config file (sudo nano /etc/ssh/sshd_config) and changed
"Password Authentication" to "Yes" and "PubKeyAuthentication" to "No". This stops the OS from requiring a one time push
of keys using mdt, which windows cannot do because of driver issues
- The host computer must have the same address as the device. So, if you're on Windows set the ip to static. On linux,
just follow the above guidelines.

## Nano
- Had to download and compile MobileNet benchmark.
    - Had one error where we had to use vim to remove the "static" description from the gLogger variable.
- For the super resolution benchmark, makes sure the main folder resides withing the `/usr/src/tensortt/bin` folder.
    - Same with the U-Net Segmentation Benchmark
    
 * [Coral Dev Board](https://coral.withgoogle.com/docs/dev-board/get-started/)
 
### Linux:
- Able to login through a serial connection.
	- Only on one dev board. Other board has problems with it's serial connection. It's slow and choppy.
	
	Steps for Serial Connection:
	- Connect dev board to computer via micro-usb
	- Open terminal, enter "sudo screen /dev/ttyUSB0 115200" (check getting link above for info on screen)
		- If this does not work try /dev/ttyUSB1
    - username: mendel, password: mendel
- Able to login through mendel
    Steps for Mendel
    - Connect through serial through steps above
    - Once logged in through serial, open a new terminal
    - type "mendel shell"
    - the device should connect up and you will be able to talk with the board
        - very hit or miss
    
    
### Oscope
- Able to control using wincom32 with python.
    - Uses an API that works with ActiveDSO to send commands
    - wincom32 is not available on Linux
- Controlling through ssh connectino
    - Change IP to static and allow "File and Printer sharing" in the Firewall
    - Cannot control Oscope through command line so SSH will not work
    - Leaves us to only use the wincom32 API and use windows
    
## Overall Notes
- Only one dev board works (the one label "working") and one nano works, the one not in a box.
- The main problem is finding benchmark programs that can run on all of the devices. We cleaned up the original code and were able to get the Nano benchmarks working, but it had the best documentation. The devices are fairly new, so maybe time is necessary for other to document this stuff or do our own research into developing these benchmarking programs.
    
    
