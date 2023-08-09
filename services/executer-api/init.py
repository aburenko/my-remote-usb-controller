#!/bin/bash
service_name="usbswitcher"

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

sudo cp "${service_name}.service" "/etc/systemd/system/${service_name}.service"

sudo systemctl daemon-reload
sudo systemctl enable $service_name

echo Use for conrols:
echo sudo systemctl start $service_name
echo sudo systemctl stop $service_name
echo sudo systemctl status $service_name
echo sudo journalctl -u $service_name -r
