sudo rm -f /dev/so100_follower
sudo rm -f /dev/so100_leader

sudo ln $(realpath /dev/serial/by-id/usb-1a86_USB_Single_Serial_58FA081973-if00)  /dev/so100_leader
sudo ln $(realpath /dev/serial/by-id/usb-1a86_USB_Single_Serial_58FA082070-if00) /dev/so100_follower
