# Bluetooth

This is a small project to test if two devices can communicate via bluetooth. 

Remember to fill out you MAC-Address in both of the files. This should be the address of the server. 

 

    client.connect(('MAC-Address', 4))

    server.bind(('MAC-Address', 4))

## How to find you MAC-Address

### Windows

From the start menu, search for:
> Device manager

When opening this window, you should see a section called **Bluetooth**. Under this section there should be an element
called: 
> Intel(R) Wireless Bluetooth(R)

Right-click this element and go to **properties**. Under the advanced section you should see a field called Address:
where your MAC-Address should be shown.

### Linux

RTFM