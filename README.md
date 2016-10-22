# Witty Board

![board](board.jpg)

## Hardware

### Espressif ESP8266 chip

* 32-bit RISC CPU: Tensilica Xtensa LX106 running at 80 MHz
  * 64 KiB of instruction RAM, 96 KiB of data RAM
* External QSPI Flash - 512 KiB to 16 MiB
* IEEE 802.11 b/g/n Wi-Fi
  * Integrated TR switch, balun, LNA, power amplifier and matching network
  * Integrated TCP/IP protocol stack
  * WEP or WPA/WPA2 authentication, or open networks
  * Wi-Fi Direct (P2P), soft-AP
  * +19.5dBm output power in 802.11b mode
  * STBC, 1x1 MIMO, 2x1 MIMO
* 16 GPIO pins
* SDIO, SPI, I2C, UART
* 1x 10-bit ADC
* Power
  * Integrated PLLs, regulators, DCXO and power management units
  * Wake up and transmit packets in < 2ms
  * Standby power consumption of < 1.0mW (DTIM3)

### Witty board

#### Top
* ESP8266 ESP12-F
* User Button
* RGB LED
* Photoresistor

#### Bottom

* [CH340G](http://kig.re/2014/12/31/how-to-use-arduino-nano-mini-pro-with-CH340G-on-mac-osx-yosemite.html) USB-serial converter
* Flash and Reset buttons

## SDKs

* [NodeMCU](https://github.com/nodemcu/nodemcu-firmware)
* [Arduino](https://github.com/esp8266/Arduino)
* [MicroPython](https://github.com/micropython/micropython/tree/master/esp8266)

## Resources

* [WittyCloudTest](https://github.com/AdySan/WittyCloudTest)
* [ESP8266 Community Forum](http://www.esp8266.com/)
