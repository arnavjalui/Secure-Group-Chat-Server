# Secure Group Chat Server
This program was originally designed as a mini project for the Network Programming Laboratory course. <br /><br />
**Pre-requisites**: Python2<br /><br />
**Warning**: The program may throw errors in Windows environment.
```
Traceback (most recent call last):
  File "client.py", line 29, in <module>
    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])
select.error: (10038, 'An operation was attempted on something that is not a socket')
```
This is not an issue with the code, but with Windows itself. It is advisable to run the program in a Linux environment.<br /><br />
**Testing**: This program has been tested on Ubuntu 17.10.1 successfully.<br />
## Steps to get the server and clients up and running
- In the server machine, open a terminal window and type in `python server.py 127.0.0.1 8081` to start the server. <br />
**Note**: Replace `127.0.0.1` with the local IP address of the server in the network and `8081` with another port if you would like to use a port other than 8081. <br /><br />
- In the client machine, open a terminal window and run, `python client.py 127.0.0.1 8081` to connect with the server. <br />
**Note**: Replace `127.0.0.1` with the local IP address of the server and `8081` with the port on which the server is running.<br /><br />
_**The server and clients are up and running and the system is now ready to be used for the intended purpose.**_
<br />
