import esp
import configparser
import network

config = configparser.ConfigParser()

config.read('config.ini')

#create access point for 
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=config['SSID']['name'])
