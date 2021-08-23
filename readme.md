
<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">The Claw</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> I like robotics and apparently so does my sister. So this serves as a good tool to nurture that interest. The UX is inspired by the dji tello.
    <br> 
</p>

## 📝 Table of Contents
- [The Build](#build)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🛠 The Build <a name = "build"></a>
The body is a EEZYbotARM MK2, which can be found on thingiverse, with version 2 of the base. You can watch Chris Reilys youtube video on how to assemble it.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/R2MI-tpXyS4/0.jpg)](https://www.youtube.com/watch?v=R2MI-tpXyS4)

#### Parts List
 - 3 MG995 Servos
 - 1 SG90 Servo
 - 1 ESP32 Dev Board
 - 5 WS2812B leds
 - 5v power supply

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites
The ESP32 is runing micropython and the frontend application is build with Vuejs. Having a basic understanding of electronics and microcontrollers will help with troubleshooting and further customizing it. I also use thonny ide to edit the code, you can use any text editor and esptool will need to be installed.

### Installing
- After cloning the respository you need to flash the latest version of micropython onto your board 
  - [Instructions](https://micropython.org/download/esp32/)

- Next install esptool.py on your computer
```python
pip install esptool.py
```
- Now update board/config.ini to further customize the robot to your liking

To check if everything worked see if the led lights light up when you connect to power.

## 🔧 Running the tests <a name = "tests"></a>
Explain how to run the automated tests for this system.

### Break down into end to end tests
Explain what these tests test and why

```
Give an example
```

### And coding style tests
Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>
Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>
Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>
- [MicroPython](https://micropython.org/) - Devboard Operationg System
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework

## ✍️ Authors <a name = "authors"></a>
- [@me](https://github.com/conceptcodes) - Initial work
- [@sis]() - Idea

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- Hat tip to anyone whose code was used
- Inspiration
- References