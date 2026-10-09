**STM32F405xx STM32F407xx**


Arm <sup><u>®</u></sup> Cortex <sup><u>®</u></sup> -M4 32b MCU+FPU, 210DMIPS, up to 1MB flash/192+4KB RAM, USB

<u>OTG HS/FS, Ethernet, 17 TIMs, 3 ADCs, 15 comm. interfaces, and camera</u>

**Datasheet** <u>-</u> **production data**

# **Features**


- **Includes ST state-of-the-art patented**
**technology**




- Core: Arm <sup>®</sup> 32-bit Cortex <sup>®</sup> -M4 CPU with FPU,
Adaptive real-time accelerator (ART
Accelerator) allowing 0-wait state execution
from flash memory, frequency up to 168 MHz,
memory protection unit, 210 DMIPS/
1.25 DMIPS/MHz (Dhrystone 2.1), and DSP
instructions

- Memories

  - Up to 1 Mbyte of flash memory

  - Up to 192+4 Kbytes of SRAM including 64Kbyte of CCM (core coupled memory) data
RAM

  - 512 bytes of OTP memory

  - Flexible static memory controller
supporting CompactFlash™, SRAM,
PSRAM, NOR and NAND memories

- LCD parallel interface, 8080/6800 modes

- Clock, reset, and supply management

  - 1.8 V to 3.6 V application supply and I/Os

  - POR, PDR, PVD and BOR

  - 4-to-26 MHz crystal oscillator

  - Internal 16 MHz factory-trimmed RC (1%
accuracy)

  - 32 kHz oscillator for RTC with calibration

  - Internal 32 kHz RC with calibration

- Low-power operation

  - Sleep, Stop, and Standby modes

  - VBAT supply for RTC, 20×32-bit backup
registers + optional 4 KB backup SRAM

- 3×12-bit, 2.4 MSPS A/D converters: up to 24
channels and 7.2 MSPS in triple interleaved
mode

- 2×12-bit D/A converters

- General-purpose DMA: 16-stream DMA
controller with FIFOs and burst support










- Up to 17 timers: up to twelve 16-bit and two 32bit timers up to 168 MHz, each with up to 4
IC/OC/PWM or pulse counter and quadrature
(incremental) encoder input

- Debug mode

  - Serial wire debug (SWD) & JTAG
interfaces

  - Cortex-M4 Embedded Trace Macrocell™

- Up to 140 I/O ports with interrupt capability

  - Up to 136 fast I/Os up to 84 MHz

  - Up to 138 5 V-tolerant I/Os

- Up to 15 communication interfaces

  - Up to 3 × I <sup>2</sup> C interfaces (SMBus/PMBus)

  - Up to 4 USARTs/2 UARTs (10.5 Mbit/s, ISO
7816 interface, LIN, IrDA, modem control)

  - Up to 3 SPIs (42 Mbits/s), 2 with muxed
full-duplex I <sup>2</sup> S to achieve audio class
accuracy via internal audio PLL or external
clock

  - 2 × CAN interfaces (2.0B Active)

  - SDIO interface

- Advanced connectivity

  - USB 2.0 full-speed device/host/OTG
controller with on-chip PHY

  - USB 2.0 high-speed/full-speed
device/host/OTG controller with dedicated
DMA, on-chip full-speed PHY and ULPI

  - 10/100 Ethernet MAC with dedicated DMA:
supports IEEE 1588v2 hardware, MII/RMII



<u>March 2026</u> <u>DS8626 Rev 12</u> <u>1/206</u>



This is information on a product in full production.



_[www.st.com](http://www.st.com)_


- 8- to 14-bit parallel camera interface up to
54 Mbytes/s

- True random number generator

- CRC calculation unit



**STM32F405xx, STM32F407xx**


- 96-bit unique ID

- RTC: subsecond accuracy, hardware calendar

- All packages are ECOPACK2 compliant



|Col1|Table 1. Device summary|
|---|---|
|**Reference**|**Part number**|
|STM32F405xx|STM32F405RG, STM32F405VG, STM32F405ZG, STM32F405OG, STM32F405OE|
|STM32F407xx|STM32F407VG, STM32F407IG, STM32F407ZG, STM32F407VE, STM32F407ZE,<br>STM32F407IE|


<u>2/206</u> <u>DS8626 Rev 12</u>


# **STM32F405xx, STM32F407xx Contents** **Contents**

**1** **Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13**


**2** **Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14**


2.1 Full compatibility throughout the family . . . . . . . . . . . . . . . . . . . . . . . . . . 17


**3** **Functional overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20**

3.1 Arm <sup>®</sup> Cortex <sup>®</sup> -M4 core with FPU and embedded flash and SRAM . . . . . 21


3.2 Adaptive real-time memory accelerator (ART Accelerator) . . . . . . . . . . . 21


3.3 Memory protection unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21


3.4 Embedded flash memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22


3.5 CRC (cyclic redundancy check) calculation unit . . . . . . . . . . . . . . . . . . . 22


3.6 Embedded SRAM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22


3.7 Multi-AHB bus matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22


3.8 DMA controller (DMA) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23


3.9 Flexible static memory controller (FSMC) . . . . . . . . . . . . . . . . . . . . . . . . 24


3.9.1 LCD parallel interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24


3.10 Nested vectored interrupt controller (NVIC) . . . . . . . . . . . . . . . . . . . . . . . 24


3.11 External interrupt/event controller (EXTI) . . . . . . . . . . . . . . . . . . . . . . . . . 25


3.12 Clocks and startup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


3.13 Boot modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


3.14 Power supply schemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


3.15 Power supply supervisor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26


3.15.1 Internal reset ON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26


3.15.2 Internal reset OFF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26


3.16 Voltage regulator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28


3.16.1 Regulator ON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28


3.16.2 Regulator OFF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29


3.17 Regulator ON/OFF and internal reset ON/OFF availability . . . . . . . . . . . 31


3.18 Real-time clock (RTC), backup SRAM and backup registers . . . . . . . . . . 31


3.19 Low-power modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

3.20 VBAT operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

3.21 Timers and watchdogs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33


<u>DS8626 Rev 12</u> <u>3/206</u>



6


**Contents** **STM32F405xx, STM32F407xx**


3.21.1 Advanced-control timers (TIM1, TIM8) . . . . . . . . . . . . . . . . . . . . . . . . . 34


3.21.2 General-purpose timers (TIMx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35


3.21.3 Basic timers TIM6 and TIM7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35


3.22 Inter-integrated circuit interface (I²C) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36


3.23 Universal synchronous/asynchronous receiver transmitters (USART) . . 36


3.24 Serial peripheral interface (SPI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37


3.25 Inter-integrated sound (I2S) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37


3.26 Audio PLL (PLLI2S) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38


3.27 Secure digital input/output interface (SDIO) . . . . . . . . . . . . . . . . . . . . . . . 38


3.28 Ethernet MAC interface with dedicated DMA and IEEE 1588 support . . . 38


3.29 Controller area network (bxCAN) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39


3.30 Universal serial bus on-the-go full-speed (OTG_FS) . . . . . . . . . . . . . . . . 39


3.31 Universal serial bus on-the-go high-speed (OTG_HS) . . . . . . . . . . . . . . . 40


3.32 Digital camera interface (DCMI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40


3.33 True random number generator (RNG) . . . . . . . . . . . . . . . . . . . . . . . . . . 40


3.34 General-purpose input/outputs (GPIOs) . . . . . . . . . . . . . . . . . . . . . . . . . . 41


3.35 Analog-to-digital converters (ADCs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41


3.36 Temperature sensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41


3.37 Digital-to-analog converter (DAC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41


3.38 Serial wire JTAG debug port (SWJ-DP) . . . . . . . . . . . . . . . . . . . . . . . . . . 42


3.39 Embedded Trace Macrocell™ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42


**4** **Pinouts and pin description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43**


**5** **Memory mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73**


**6** **Electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78**


6.1 Parameter conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


6.1.1 Minimum and maximum values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


6.1.2 Typical values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


6.1.3 Typical curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


6.1.4 Loading capacitor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


6.1.5 Pin input voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


6.1.6 Power supply scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79


6.1.7 Current consumption measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . 80


<u>4/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Contents**


6.2 Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80


6.3 Operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81


6.3.1 General operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81


6.3.2 VCAP_1/VCAP_2 external capacitor . . . . . . . . . . . . . . . . . . . . . . . . . . . 84


6.3.3 Operating conditions at power-up / power-down (regulator ON) . . . . . . 84


6.3.4 Operating conditions at power-up / power-down (regulator OFF) . . . . . 84


6.3.5 Embedded reset and power control block characteristics . . . . . . . . . . . 85


6.3.6 Supply current characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86


6.3.7 Wakeup time from low-power mode . . . . . . . . . . . . . . . . . . . . . . . . . . 100


6.3.8 External clock source characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 101


6.3.9 Internal clock source characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 105


6.3.10 PLL characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106


6.3.11 PLL spread spectrum clock generation (SSCG) characteristics . . . . . 108


6.3.12 Memory characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110


6.3.13 EMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112


6.3.14 Absolute maximum ratings (electrical sensitivity) . . . . . . . . . . . . . . . . 114


6.3.15 I/O current injection characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 115


6.3.16 I/O port characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116


6.3.17 NRST pin characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121


6.3.18 TIM timer characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121


6.3.19 Communications interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123


6.3.20 CAN (controller area network) interface . . . . . . . . . . . . . . . . . . . . . . . 135


6.3.21 12-bit ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135


6.3.22 Temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

6.3.23 VBAT monitoring characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141

6.3.24 Embedded reference voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141


6.3.25 DAC electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141


6.3.26 FSMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144


6.3.27 Camera interface (DCMI) timing specifications . . . . . . . . . . . . . . . . . . 162


6.3.28 SD/SDIO MMC card host interface (SDIO) characteristics . . . . . . . . . 163


6.3.29 RTC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164


**7** **Package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165**


7.1 Device marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165


7.2 WLCSP90 package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166


7.3 LQFP64 package information (5W) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169


<u>DS8626 Rev 12</u> <u>5/206</u>



6


**Contents** **STM32F405xx, STM32F407xx**


7.4 LQFP100 package information (1L) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172


7.5 LQFP144 package information (1A) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175


7.6 UFBGA(176+25) package information (A0E7) . . . . . . . . . . . . . . . . . . . . 179


7.7 LQFP176 package information (1T) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181


7.8 Thermal characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185


**8** **Ordering information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186**


**Appendix A** **Application block diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187**


A.1 USB OTG full speed (FS) interface solutions . . . . . . . . . . . . . . . . . . . . . 187


A.2 USB OTG high speed (HS) interface solutions . . . . . . . . . . . . . . . . . . . . 189


A.3 Ethernet interface solutions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190


**9** **Important security notice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192**


**10** **Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193**


<u>6/206</u> <u>DS8626 Rev 12</u>


# **STM32F405xx, STM32F407xx List of tables** **List of tables**

Table 1. Device summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Table 2. STM32F405xx and STM32F407xx: features and peripheral counts. . . . . . . . . . . . . . . . . . 15
Table 3. Regulator ON/OFF and internal reset ON/OFF availability. . . . . . . . . . . . . . . . . . . . . . . . . 31
Table 4. Timer feature comparison. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
Table 5. USART feature comparison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
Table 6. Legend/abbreviations used in the pinout table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Table 7. STM32F40xxx pin and ball definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
Table 8. FSMC pin definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
Table 9. Alternate function mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
Table 10. Register boundary addresses. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
Table 11. Voltage characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
Table 12. Current characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Table 13. Thermal characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Table 14. General operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Table 15. Limitations depending on the operating power supply range . . . . . . . . . . . . . . . . . . . . . . . 83
Table 16. VCAP_1/VCAP_2 operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
Table 17. Operating conditions at power-up / power-down (regulator ON) . . . . . . . . . . . . . . . . . . . . 84
Table 18. Operating conditions at power-up / power-down (regulator OFF). . . . . . . . . . . . . . . . . . . . 84
Table 19. Embedded reset and power control block characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . 85
Table 20. Typical and maximum current consumption in Run mode, code with data processing
running from flash memory (ART accelerator enabled) or RAM . . . . . . . . . . . . . . . . . . . . 87
Table 21. Typical and maximum current consumption in Run mode, code with data processing
running from flash memory (ART accelerator disabled) . . . . . . . . . . . . . . . . . . . . . . . . . . 88
Table 22. Typical and maximum current consumption in Sleep mode . . . . . . . . . . . . . . . . . . . . . . . . 91
Table 23. Typical and maximum current consumptions in Stop mode . . . . . . . . . . . . . . . . . . . . . . . . 92
Table 24. Typical and maximum current consumptions in Standby mode . . . . . . . . . . . . . . . . . . . . . 92
Table 25. Typical and maximum current consumptions in VBAT mode. . . . . . . . . . . . . . . . . . . . . . . . 93
Table 26. Typical current consumption in Run mode, code with data processing
running from flash memory, regulator ON (ART accelerator enabled
except prefetch), VDD = 1.8 V. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
Table 27. Switching output I/O current consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
Table 28. Peripheral current consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
Table 29. Low-power mode wakeup timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
Table 30. High-speed external user clock characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
Table 31. Low-speed external user clock characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Table 32. HSE 4-26 MHz oscillator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
Table 33. LSE oscillator characteristics (fLSE = 32.768 kHz) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Table 34. HSI oscillator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
Table 35. LSI oscillator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
Table 36. Main PLL characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
Table 37. PLLI2S (audio PLL) characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
Table 38. SSCG parameters constraint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
Table 39. Flash memory characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
Table 40. Flash memory programming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
Table 41. Flash memory programming with VPP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Table 42. Flash memory endurance and data retention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Table 43. EMS characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
Table 44. EMI characteristics for fHSE = 25 MH and fCPU = 168 MHz . . . . . . . . . . . . . . . . . . . . . . 114


<u>DS8626 Rev 12</u> <u>7/206</u>



9


**List of tables** **STM32F405xx, STM32F407xx**


Table 45. ESD absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
Table 46. Electrical sensitivities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
Table 47. I/O current injection susceptibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
Table 48. I/O static characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
Table 49. Output voltage characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
Table 50. I/O AC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
Table 51. NRST pin characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Table 52. Characteristics of TIMx connected to the APB1 domain . . . . . . . . . . . . . . . . . . . . . . . . . 122
Table 53. Characteristics of TIMx connected to the APB2 domain . . . . . . . . . . . . . . . . . . . . . . . . . 123
Table 54. I2C analog filter characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
Table 55. SPI dynamic characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
Table 56. I2S dynamic characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
Table 57. USB OTG FS startup time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
Table 58. USB OTG FS DC electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
Table 59. USB OTG FS electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
Table 60. USB HS DC electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
Table 61. USB HS clock timing parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
Table 62. ULPI timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Table 63. Ethernet DC electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
Table 64. Dynamic characteristics: Ethernet MAC signals for SMI. . . . . . . . . . . . . . . . . . . . . . . . . . 133
Table 65. Dynamic characteristics: Ethernet MAC signals for RMII . . . . . . . . . . . . . . . . . . . . . . . . . 134
Table 66. Dynamic characteristics: Ethernet MAC signals for MII . . . . . . . . . . . . . . . . . . . . . . . . . . 135
Table 67. ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
Table 68. ADC accuracy at fADC = 30 MHz . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
Table 69. Temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
Table 70. Temperature sensor calibration values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
Table 71. VBAT monitoring characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
Table 72. Embedded internal reference voltage. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
Table 73. Internal reference voltage calibration values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
Table 74. DAC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
Table 75. Asynchronous non-multiplexed SRAM/PSRAM/NOR read timings . . . . . . . . . . . . . . . . . 145
Table 76. Asynchronous non-multiplexed SRAM/PSRAM/NOR write timings . . . . . . . . . . . . . . . . . 146
Table 77. Asynchronous multiplexed PSRAM/NOR read timings. . . . . . . . . . . . . . . . . . . . . . . . . . . 147
Table 78. Asynchronous multiplexed PSRAM/NOR write timings . . . . . . . . . . . . . . . . . . . . . . . . . . 148
Table 79. Synchronous multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
Table 80. Synchronous multiplexed PSRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
Table 81. Synchronous non-multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . 153
Table 82. Synchronous non-multiplexed PSRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
Table 83. Switching characteristics for PC Card/CF read and write cycles
in attribute/common space. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
Table 84. Switching characteristics for PC Card/CF read and write cycles
in I/O space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
Table 85. Switching characteristics for NAND flash read cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
Table 86. Switching characteristics for NAND flash write cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Table 87. DCMI characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Table 88. Dynamic characteristics: SD/MMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
Table 89. RTC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
Table 90. WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch wafer level chip scale
package mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
Table 91. WLCSP90 recommended PCB design rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
Table 92. LQFP64 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
Table 93. LQFP100 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173


<u>8/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **List of tables**


Table 94. LQFP144 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
Table 95. UFBGA(176+25) - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
Table 96. UFBGA(176+25) - Example of PCB design rules (0.65 mm pitch BGA) . . . . . . . . . . . . . 180
Table 97. LQFP176 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
Table 98. Package thermal characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
Table 99. Document revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193


<u>DS8626 Rev 12</u> <u>9/206</u>



9


# **List of figures STM32F405xx, STM32F407xx** **List of figures**

Figure 1. Compatible board design between STM32F10xx/STM32F40xxx for LQFP64 . . . . . . . . . . 17
Figure 2. Compatible board design STM32F10xx/STM32F2/STM32F40xxx
for LQFP100 package. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Figure 3. Compatible board design between STM32F10xx/STM32F2/STM32F40xxx
for LQFP144 package. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Figure 4. Compatible board design between STM32F2 and STM32F40xxx
for LQFP176 and BGA176 packages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
Figure 5. STM32F40xxx block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
Figure 6. Multi-AHB matrix. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
Figure 7. Power supply supervisor interconnection with internal reset OFF . . . . . . . . . . . . . . . . . . . 27
Figure 8. PDR_ON and NRST control with internal reset OFF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
Figure 9. Regulator OFF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
Figure 10. Startup in regulator OFF mode: slow VDD slope

        - power-down reset risen after VCAP_1/VCAP_2 stabilization . . . . . . . . . . . . . . . . . . . . . . . . 30
Figure 11. Startup in regulator OFF mode: fast VDD slope

        - power-down reset risen before VCAP_1/VCAP_2 stabilization . . . . . . . . . . . . . . . . . . . . . . 31
Figure 12. STM32F40xxx LQFP64 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
Figure 13. STM32F40xxx LQFP100 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
Figure 14. STM32F40xxx LQFP144 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
Figure 15. STM32F40xxx LQFP176 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
Figure 16. STM32F40xxx UFBGA176 ballout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
Figure 17. STM32F40xxx WLCSP90 ballout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Figure 18. STM32F40xxx memory map. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
Figure 19. Pin loading conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
Figure 20. Pin input voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
Figure 21. Power supply scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
Figure 22. Current consumption measurement scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
Figure 23. External capacitor CEXT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
Figure 24. Typical current consumption versus temperature, Run mode, code with data
processing running from flash (ART accelerator ON) or RAM, and peripherals OFF. . . . . 89
Figure 25. Typical current consumption versus temperature, Run mode, code with data
processing running from flash (ART accelerator ON) or RAM, and peripherals ON. . . . . . 89
Figure 26. Typical current consumption versus temperature, Run mode, code with data
processing running from flash (ART accelerator OFF) or RAM, and peripherals OFF. . . . 90
Figure 27. Typical current consumption versus temperature, Run mode, code with data
processing running from flash (ART accelerator OFF) or RAM, and peripherals ON. . . . . 90
Figure 28. Typical VBAT current consumption (LSE and RTC ON/backup RAM OFF) . . . . . . . . . . . . 93
Figure 29. Typical VBAT current consumption (LSE and RTC ON/backup RAM ON) . . . . . . . . . . . . . 94
Figure 30. High-speed external clock source AC timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Figure 31. Low-speed external clock source AC timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
Figure 32. Typical application with an 8 MHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Figure 33. Typical application with a 32.768 kHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
Figure 34. ACCLSI versus temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
Figure 35. PLL output clock waveforms in center spread mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
Figure 36. PLL output clock waveforms in down spread mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
Figure 37. I/O AC characteristics definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
Figure 38. Recommended NRST pin protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Figure 39. SPI timing diagram - slave mode and CPHA = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126


<u>10/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **List of figures**


Figure 40. SPI timing diagram - slave mode and CPHA = 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
Figure 41. SPI timing diagram - master mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Figure 42. I2S slave timing diagram (Philips protocol) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
Figure 43. I2S master timing diagram (Philips protocol) <sup>(1)</sup> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
Figure 44. USB OTG FS timings: definition of data signal rise and fall time . . . . . . . . . . . . . . . . . . . 131
Figure 45. ULPI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Figure 46. Ethernet SMI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
Figure 47. Ethernet RMII timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
Figure 48. Ethernet MII timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
Figure 49. ADC accuracy characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
Figure 50. Typical connection diagram when using the ADC with FT/TT pins featuring
analog switch function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
Figure 51. Power supply and reference decoupling (VREF+ not connected to VDDA). . . . . . . . . . . . . 139
Figure 52. Power supply and reference decoupling (VREF+ connected to VDDA). . . . . . . . . . . . . . . . 140
Figure 53. 12-bit buffered /non-buffered DAC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
Figure 54. Asynchronous non-multiplexed SRAM/PSRAM/NOR read waveforms . . . . . . . . . . . . . . 145
Figure 55. Asynchronous non-multiplexed SRAM/PSRAM/NOR write waveforms . . . . . . . . . . . . . . 146
Figure 56. Asynchronous multiplexed PSRAM/NOR read waveforms. . . . . . . . . . . . . . . . . . . . . . . . 147
Figure 57. Asynchronous multiplexed PSRAM/NOR write waveforms . . . . . . . . . . . . . . . . . . . . . . . 148
Figure 58. Synchronous multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
Figure 59. Synchronous multiplexed PSRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
Figure 60. Synchronous non-multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . 152
Figure 61. Synchronous non-multiplexed PSRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
Figure 62. PC Card/CompactFlash controller waveforms for common memory read access . . . . . . 155
Figure 63. PC Card/CompactFlash controller waveforms for common memory write access. . . . . . 156
Figure 64. PC Card/CompactFlash controller waveforms for attribute memory read
access. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
Figure 65. PC Card/CompactFlash controller waveforms for attribute memory write
access. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
Figure 66. PC Card/CompactFlash controller waveforms for I/O space read access . . . . . . . . . . . . 158
Figure 67. PC Card/CompactFlash controller waveforms for I/O space write access . . . . . . . . . . . . 159
Figure 68. NAND controller waveforms for read access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
Figure 69. NAND controller waveforms for write access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
Figure 70. DCMI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Figure 71. SDIO high-speed mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
Figure 72. SD default mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
Figure 73. WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch wafer level chip scale
package outline. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
Figure 74. WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch wafer level chip scale
package recommended footprint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
Figure 75. WLCSP90 marking example (package top view) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
Figure 76. LQFP64 - Outline <sup>(15)</sup> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
Figure 77. LQFP100 - Outline <sup>(15)</sup> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
Figure 78. LQFP100 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
Figure 79. LQFP144 - Outline <sup>(15)</sup> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
Figure 80. LQFP144 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
Figure 81. UFBGA(176+25) - Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
Figure 82. UFBGA(176+25) - Footprint example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
Figure 83. LQFP176 - Outline <sup>(15)</sup> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
Figure 84. LQFP176 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
Figure 85. USB controller configured as peripheral-only and used
in Full speed mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187


<u>DS8626 Rev 12</u> <u>11/206</u>



12


**List of figures** **STM32F405xx, STM32F407xx**


Figure 86. USB controller configured as host-only and used in full speed mode. . . . . . . . . . . . . . . . 187
Figure 87. USB controller configured in dual mode and used in full speed mode . . . . . . . . . . . . . . . 188
Figure 88. USB controller configured as peripheral, host, or dual-mode
and used in high speed mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
Figure 89. MII mode using a 25 MHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
Figure 90. RMII with a 50 MHz oscillator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
Figure 91. RMII with a 25 MHz crystal and PHY with PLL. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191


<u>12/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Introduction**

# **1 Introduction**


This datasheet provides the description of the STM32F405xx and STM32F407xx lines of
microcontrollers. For more details on the whole STMicroelectronics STM32™ family, refer to
_Section 2.1: Full compatibility throughout the family_ .


The STM32F405xx and STM32F407xx datasheet should be read in conjunction with the
STM32F4xx reference manual which is available from the STMicroelectronics website
_www.st.com_ .


For information on the device errata with respect to the datasheet and reference manual,
refer to the STM32F405xx and STM32F407xx errata sheet (ES0182), which is available
from the STMicroelectronics website _www.st.com_ .

For information on the Arm <sup>®</sup> Cortex <sup>®</sup> -M4 core, refer to the Cortex <sup>®</sup> -M4 programming
manual (PM0214) available from _www.st.com_ .


_Note:_ _Arm and Cortex are registered trademarks of Arm Limited (or its subsidiaries or affiliates) in_
_the US and/or elsewhere._

_The Arm word and logo are trademarks of Arm Limited (or its subsidiaries) in the US and/or_
_elsewhere. All rights reserved._


<u>DS8626 Rev 12</u> <u>13/206</u>



191


**Description** **STM32F405xx, STM32F407xx**

# **2 Description**


The STM32F405xx and STM32F407xx family is based on the high-performance Arm <sup>®</sup>
Cortex <sup>®</sup> -M4 32-bit RISC core operating at a frequency of up to 168 MHz. The Cortex <sup>®</sup> -M4
core features a floating-point unit (FPU) single precision which supports all Arm singleprecision data-processing instructions and data types. It also implements a full set of DSP
instructions and a memory protection unit (MPU) which enhances application security.


The STM32F405xx and STM32F407xx family incorporates high-speed embedded
memories (flash memory up to 1 Mbyte, up to 192 Kbytes of SRAM), up to 4 Kbytes of
backup SRAM, and an extensive range of enhanced I/Os and peripherals connected to two
APB buses, three AHB buses and a 32-bit multi-AHB bus matrix.


All devices offer three 12-bit ADCs, two DACs, a low-power RTC, 12 general-purpose 16-bit
timers including two PWM timers for motor control, two general-purpose 32-bit timers. a true
random number generator (RNG). They also feature standard and advanced
communication interfaces.
# • Up to three I 2 Cs • Three SPIs, two I 2 Ss full duplex. To achieve audio class accuracy, the I2S peripherals

can be clocked via a dedicated internal audio PLL or via an external clock to allow
synchronization

      - Four USARTs plus two UARTs

      - A USB OTG full speed and a USB OTG high speed with full-speed capability (with the
ULPI)

      - Two CANs

      - An SDIO/MMC interface

      - Ethernet and the camera interface available on STM32F407xx devices only


New advanced peripherals include an SDIO, an enhanced flexible static memory control
(FSMC) interface (for devices offered in packages of 100 pins and more), a camera
interface for CMOS sensors. Refer to _Table 2: STM32F405xx and STM32F407xx: features_
_and peripheral counts_ for the list of peripherals available on each part number.


The STM32F405xx and STM32F407xx family operates in the –40 to +105 °C temperature
range from a 1.8 to 3.6 V power supply. The supply voltage can drop to 1.7 V when the
device operates in the 0 to 70 °C temperature range using an external power supply
supervisor: refer to _Section 3.15.2: Internal reset OFF_ . A comprehensive set of powersaving mode allows the design of low-power applications.


The STM32F405xx and STM32F407xx family offers devices in various packages ranging
from 64 pins to 176 pins. The set of included peripherals changes with the device chosen.


These features make the STM32F405xx and STM32F407xx microcontroller family suitable
for a wide range of applications:

      - Motor drive and application control

      - Medical equipment

      - Industrial applications: PLC, inverters, circuit breakers

      - Printers, and scanners

      - Alarm systems, video intercom, and HVAC

      - Home audio appliances


<u>14/206</u> <u>DS8626 Rev 12</u>


_Figure 5_ shows the general block diagram of the device family.

## **Table 2. STM32F405xx and STM32F407xx: features and peripheral counts**














|Peripherals|Col2|STM32F405RG|STM32F405OG|STM32F405VG|STM32F405ZG|STM32F405OE|STM32F407Vx|Col9|STM32F407Zx|Col11|STM32F407Ix|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Flash memory in<br>Kbytes|Flash memory in<br>Kbytes|1024|1024|1024|1024|512|512|1024|512|1024|512|1024|
|SRAM in<br>Kbytes|System|192(112+16+64)|192(112+16+64)|192(112+16+64)|192(112+16+64)|192(112+16+64)|192(112+16+64)|192(112+16+64)|192(112+16+64)|192(112+16+64)|192(112+16+64)|192(112+16+64)|
|SRAM in<br>Kbytes|Backup|4|4|4|4|4|4|4|4|4|4|4|
|FSMC memory<br>controller|FSMC memory<br>controller|No|Yes(1)|Yes(1)|Yes(1)|Yes(1)|Yes(1)|Yes(1)|Yes(1)|Yes(1)|Yes(1)|Yes(1)|
|Ethernet|Ethernet|No|No|No|No|No|Yes|Yes|Yes|Yes|Yes|Yes|
|Timers|General-<br>purpose|10|10|10|10|10|10|10|10|10|10|10|
|Timers|Advanced<br>-control|2|2|2|2|2|2|2|2|2|2|2|
|Timers|Basic|2|2|2|2|2|2|2|2|2|2|2|
|Timers|IWDG|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Timers|WWDG|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Timers|RTC|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|True random number<br>generator|True random number<br>generator|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|


**<u>Table 2. STM32F405xx and STM32F407xx: features and peripheral counts (continued)</u>**



















|Peripherals|Col2|STM32F405RG|STM32F405OG|STM32F405VG|STM32F405ZG|STM32F405OE|STM32F407Vx|STM32F407Zx|STM32F407Ix|
|---|---|---|---|---|---|---|---|---|---|
|Communi<br>cation<br>interfaces|SPI / I2S|3/2 (full duplex)(2)|3/2 (full duplex)(2)|3/2 (full duplex)(2)|3/2 (full duplex)(2)|3/2 (full duplex)(2)|3/2 (full duplex)(2)|3/2 (full duplex)(2)|3/2 (full duplex)(2)|
|Communi<br>cation<br>interfaces|I2C|3|3|3|3|3|3|3|3|
|Communi<br>cation<br>interfaces|USART/<br>UART|4/2|4/2|4/2|4/2|4/2|4/2|4/2|4/2|
|Communi<br>cation<br>interfaces|USB<br>OTG FS|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Communi<br>cation<br>interfaces|USB<br>OTG HS|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Communi<br>cation<br>interfaces|CAN|2|2|2|2|2|2|2|2|
|Communi<br>cation<br>interfaces|SDIO|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Camera interface|Camera interface|No|No|No|No|No|Yes|Yes|Yes|
|GPIOs|GPIOs|51|72|82|114|72|82|114|140|
|12-bit ADC<br>Number of channels|12-bit ADC<br>Number of channels|3|3|3|3|3|3|3|3|
|12-bit ADC<br>Number of channels|12-bit ADC<br>Number of channels|16|13|16|24|13|16|24|24|
|12-bit DAC <br>Number of channels|12-bit DAC <br>Number of channels|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|
|Maximum CPU<br>frequency|Maximum CPU<br>frequency|168 MHz|168 MHz|168 MHz|168 MHz|168 MHz|168 MHz|168 MHz|168 MHz|
|Operating voltage|Operating voltage|1.8 to 3.6 V(3)|1.8 to 3.6 V(3)|1.8 to 3.6 V(3)|1.8 to 3.6 V(3)|1.8 to 3.6 V(3)|1.8 to 3.6 V(3)|1.8 to 3.6 V(3)|1.8 to 3.6 V(3)|
|Operating<br>temperatures|Operating<br>temperatures|Ambient temperatures: –40 to +85 °C /–40 to +105 °C|Ambient temperatures: –40 to +85 °C /–40 to +105 °C|Ambient temperatures: –40 to +85 °C /–40 to +105 °C|Ambient temperatures: –40 to +85 °C /–40 to +105 °C|Ambient temperatures: –40 to +85 °C /–40 to +105 °C|Ambient temperatures: –40 to +85 °C /–40 to +105 °C|Ambient temperatures: –40 to +85 °C /–40 to +105 °C|Ambient temperatures: –40 to +85 °C /–40 to +105 °C|
|Operating<br>temperatures|Operating<br>temperatures|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|
|Package|Package|LQFP64|WLCSP90|LQFP100|LQFP144|WLCSP90|LQFP100|LQFP144|UFBGA176<br>LQFP176|


1. For the LQFP100 and WLCSP90 packages, only FSMC Bank1 or Bank2 are available. Bank1 can only support a multiplexed NOR/PSRAM memory using the NE1 Chip
Select. Bank2 can only support a 16- or 8-bit NAND flash memory using the NCE2 Chip Select. The interrupt line cannot be used since Port G is not available in this
package.

2. The SPI2 and SPI3 interfaces give the flexibility to work in an exclusive way in either the SPI mode or the I <sup>2</sup> S audio mode.

3. VDD/VDDA minimum value of 1.7 V is obtained when the device operates in reduced temperature range, and with the use of an external power supply supervisor (refer to
_Section 3.15.2: Internal reset OFF_ ).


**STM32F405xx, STM32F407xx** **Description**

## **2.1 Full compatibility throughout the family**


The STM32F405xx and STM32F407xx are part of the STM32F4 family. They are fully pinto-pin, software and feature compatible with the STM32F2xx devices, allowing the user to
try different memory densities, peripherals, and performances (FPU, higher frequency) for a
greater degree of freedom during the development cycle.


The STM32F405xx and STM32F407xx devices maintain a close compatibility with the
whole STM32F10xxx family. All functional pins are pin-to-pin compatible. The
STM32F405xx and STM32F407xx, however, are not drop-in replacements for the
STM32F10xxx devices: the two families do not have the same power scheme, and so their
power pins are different. Nonetheless, transition from the STM32F10xxx to the
STM32F40xxx family remains simple as only a few pins are impacted.

### Figure 4, Figure 3, Figure 2, and Figure 1 give compatible board designs between the

STM32F40xxx, STM32F2, and STM32F10xxx families.

### **Figure 1. Compatible board design between STM32F10xx/STM32F40xxx for LQFP64**



















<u>DS8626 Rev 12</u> <u>17/206</u>



191


**Description** **STM32F405xx, STM32F407xx**

### **Figure 2. Compatible board design STM32F10xx/STM32F2/STM32F40xxx**


































### **Figure 3. Compatible board design between STM32F10xx/STM32F2/STM32F40xxx**

**<u>for LQFP144 package</u>**











































<u>18/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Description**

### **Figure 4. Compatible board design between STM32F2 and STM32F40xxx**

**<u>for LQFP176 and BGA176 packages</u>**













<u>DS8626 Rev 12</u> <u>19/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**

# **3 Functional overview**

## **Figure 5. STM32F40xxx block diagram**












































|CCM data RAM 64 KB External memory<br>controller (FSMC)<br>JTAG & SW MPU AHB3 SRAM, PSRAM, NOR Flash,<br>ETM NVIC PC Card (ATA), NAND Flash<br>D-BUS<br>Arm Cortex-M4<br>168 MHz I-BUS<br>FPU Flash ACCEL/ CACHE<br>S-BUS up to<br>RNG ART<br>Ethernet MAC DMA/ 1 MB 8S7M<br>10/100 FIFO Camera FIFO<br>SRAM 112 KB interface bus-matrix<br>USB DMA/ SRAM 16 KB PHY<br>OTG HS FIFO USB AHB FIFO PHY<br>DMA2 8 Stre Fa IFm Os AHB2 168 MHz OTG FS<br>DMA1 8 Stre Fa IFm Os AHB1 168 MHz VDD Power managmt<br>Voltage<br>regulator<br>3.3 to 1.2 V<br>@VDD<br>@VDDA<br>POR Supply<br>GPIO PORT A RC HS reset supervision<br>RC L S Int PO BR O/P RDR<br>GPIO PORT B<br>P L L1&2<br>PVD<br>GPIO PORT C<br>@VDDA @VDD<br>GPIO PORT D<br>XTAL OSC<br>4- 16MHz<br>GPIO PORT E Reset &<br>IWDG<br>M AclNoc kA G T<br>GPIO PORT F control<br>PWR<br>interface<br>GPIO PORT G @VBAT FCLK HCLKx PCLKx<br>GPIO PORT H XTAL 32 kHz LS<br>RTC<br>GPIO PORT I AWU<br>Backup register<br>LS<br>4 KB BKPSRAM<br>TIM2 32b<br>TIM3 16b<br>EXT IT. WKUP DMA2 DMA1 TIM4 16b<br>TIM5 32b FIFO<br>SDIO / MMC<br>AHB/APB2 AHB/APB1 TIM12 16b<br>TIM1 / PWM 16b TIM13 16b<br>TIM14 16b<br>TIM8 / PWM 16b<br>USART2 smcard<br>irDA TIM9 16b USART3 smcard (max) Hz<br>irDA TIM10 16b MHz a3 x0) M|Col2|Col3|
|---|---|---|
|GPIO PORT A<br>AHB/APB2<br>TIM1 / PWM<br>3 0 M Hz<br>4 KB BKPSRAM<br>16b<br>SDIO / MMC<br>DMA2<br>JTAG & SW<br>Arm Cortex-M4<br>168 MHz<br>NVIC<br>ETM<br>MPU<br>Ethernet MAC<br>10/100<br>DMA/<br>FIFO<br>USB<br>OTG HS<br>DMA2<br>8 Streams<br>FIFO<br>ART ACCEL/<br>CACHE<br>SRAM 112 KB<br>RNG<br>Camera<br>interface<br>PHY<br>USB<br>OTG FS<br>FIFO<br>AHB1 168 MHz<br>PHY<br>FIFO<br>POR/PDR<br>BOR<br>Supply<br>supervision<br>@VDDA<br>PVD<br>Int<br>POR<br>reset<br>XTAL 32 kHz<br>M AN A G T<br>RTC<br>RC<br>HS<br>FCLK<br>RC<br>L S<br>PWR<br>interface<br>IWDG<br>@VBAT<br>AWU<br>Reset &<br>clock<br>control<br>P L L1&2<br>PCLKx<br>Voltage<br>regulator<br>3.3 to 1.2 V<br>VDD<br>Power managmt<br>Backup register<br>AHB bus-matrix 8S7M<br>LS<br>Flash<br>up to<br>1 MB<br>SRAM, PSRAM, NOR Flash,<br>PC Card (ATA), NAND Flash<br>External memory<br>controller (FSMC)<br>TIM2<br>TIM3<br>TIM4<br>TIM5<br>TIM12<br>TIM13<br>TIM14<br>USART2<br>USART3<br><br>EXT IT. WKUP<br>D-BUS<br>FPU<br>    ax)<br>SRAM 16 KB<br>CCM data RAM 64 KB<br>AHB3<br>AHB2 168 MHz<br>I-BUS<br>S-BUS<br>DMA/<br>FIFO<br>DMA1<br>8 Streams<br>FIFO<br>GPIO PORT B<br>GPIO PORT C<br>GPIO PORT D<br>GPIO PORT E<br>GPIO PORT F<br>GPIO PORT G<br>GPIO PORT H<br>GPIO PORT I<br>TIM8 / PWM<br>16b<br>smcard<br>irDA<br>smcard<br>irDA<br>16b<br>16b<br>16b<br>32b<br>16b<br>16b<br>32b<br>DMA1<br>AHB/APB1<br>LS<br>HCLKx<br>XTAL OSC<br>4- 16MHz<br>FIFO<br>TIM9<br>16b<br>TIM10<br>16b<br>  MHz (max)<br>@VDD<br>@VDD<br>@VDDA||XTAL OSC<br>4- 16MHz|
|GPIO PORT A<br>AHB/APB2<br>TIM1 / PWM<br>3 0 M Hz<br>4 KB BKPSRAM<br>16b<br>SDIO / MMC<br>DMA2<br>JTAG & SW<br>Arm Cortex-M4<br>168 MHz<br>NVIC<br>ETM<br>MPU<br>Ethernet MAC<br>10/100<br>DMA/<br>FIFO<br>USB<br>OTG HS<br>DMA2<br>8 Streams<br>FIFO<br>ART ACCEL/<br>CACHE<br>SRAM 112 KB<br>RNG<br>Camera<br>interface<br>PHY<br>USB<br>OTG FS<br>FIFO<br>AHB1 168 MHz<br>PHY<br>FIFO<br>POR/PDR<br>BOR<br>Supply<br>supervision<br>@VDDA<br>PVD<br>Int<br>POR<br>reset<br>XTAL 32 kHz<br>M AN A G T<br>RTC<br>RC<br>HS<br>FCLK<br>RC<br>L S<br>PWR<br>interface<br>IWDG<br>@VBAT<br>AWU<br>Reset &<br>clock<br>control<br>P L L1&2<br>PCLKx<br>Voltage<br>regulator<br>3.3 to 1.2 V<br>VDD<br>Power managmt<br>Backup register<br>AHB bus-matrix 8S7M<br>LS<br>Flash<br>up to<br>1 MB<br>SRAM, PSRAM, NOR Flash,<br>PC Card (ATA), NAND Flash<br>External memory<br>controller (FSMC)<br>TIM2<br>TIM3<br>TIM4<br>TIM5<br>TIM12<br>TIM13<br>TIM14<br>USART2<br>USART3<br><br>EXT IT. WKUP<br>D-BUS<br>FPU<br>    ax)<br>SRAM 16 KB<br>CCM data RAM 64 KB<br>AHB3<br>AHB2 168 MHz<br>I-BUS<br>S-BUS<br>DMA/<br>FIFO<br>DMA1<br>8 Streams<br>FIFO<br>GPIO PORT B<br>GPIO PORT C<br>GPIO PORT D<br>GPIO PORT E<br>GPIO PORT F<br>GPIO PORT G<br>GPIO PORT H<br>GPIO PORT I<br>TIM8 / PWM<br>16b<br>smcard<br>irDA<br>smcard<br>irDA<br>16b<br>16b<br>16b<br>32b<br>16b<br>16b<br>32b<br>DMA1<br>AHB/APB1<br>LS<br>HCLKx<br>XTAL OSC<br>4- 16MHz<br>FIFO<br>TIM9<br>16b<br>TIM10<br>16b<br>  MHz (max)<br>@VDD<br>@VDD<br>@VDDA|IWDG<br>|IWDG<br>|
|GPIO PORT A<br>AHB/APB2<br>TIM1 / PWM<br>3 0 M Hz<br>4 KB BKPSRAM<br>16b<br>SDIO / MMC<br>DMA2<br>JTAG & SW<br>Arm Cortex-M4<br>168 MHz<br>NVIC<br>ETM<br>MPU<br>Ethernet MAC<br>10/100<br>DMA/<br>FIFO<br>USB<br>OTG HS<br>DMA2<br>8 Streams<br>FIFO<br>ART ACCEL/<br>CACHE<br>SRAM 112 KB<br>RNG<br>Camera<br>interface<br>PHY<br>USB<br>OTG FS<br>FIFO<br>AHB1 168 MHz<br>PHY<br>FIFO<br>POR/PDR<br>BOR<br>Supply<br>supervision<br>@VDDA<br>PVD<br>Int<br>POR<br>reset<br>XTAL 32 kHz<br>M AN A G T<br>RTC<br>RC<br>HS<br>FCLK<br>RC<br>L S<br>PWR<br>interface<br>IWDG<br>@VBAT<br>AWU<br>Reset &<br>clock<br>control<br>P L L1&2<br>PCLKx<br>Voltage<br>regulator<br>3.3 to 1.2 V<br>VDD<br>Power managmt<br>Backup register<br>AHB bus-matrix 8S7M<br>LS<br>Flash<br>up to<br>1 MB<br>SRAM, PSRAM, NOR Flash,<br>PC Card (ATA), NAND Flash<br>External memory<br>controller (FSMC)<br>TIM2<br>TIM3<br>TIM4<br>TIM5<br>TIM12<br>TIM13<br>TIM14<br>USART2<br>USART3<br><br>EXT IT. WKUP<br>D-BUS<br>FPU<br>    ax)<br>SRAM 16 KB<br>CCM data RAM 64 KB<br>AHB3<br>AHB2 168 MHz<br>I-BUS<br>S-BUS<br>DMA/<br>FIFO<br>DMA1<br>8 Streams<br>FIFO<br>GPIO PORT B<br>GPIO PORT C<br>GPIO PORT D<br>GPIO PORT E<br>GPIO PORT F<br>GPIO PORT G<br>GPIO PORT H<br>GPIO PORT I<br>TIM8 / PWM<br>16b<br>smcard<br>irDA<br>smcard<br>irDA<br>16b<br>16b<br>16b<br>32b<br>16b<br>16b<br>32b<br>DMA1<br>AHB/APB1<br>LS<br>HCLKx<br>XTAL OSC<br>4- 16MHz<br>FIFO<br>TIM9<br>16b<br>TIM10<br>16b<br>  MHz (max)<br>@VDD<br>@VDD<br>@VDDA|XTAL 32 kHz<br>PWR<br>interface<br>@VBAT<br>|XTAL 32 kHz<br>PWR<br>interface<br>@VBAT<br>|
|GPIO PORT A<br>AHB/APB2<br>TIM1 / PWM<br>3 0 M Hz<br>4 KB BKPSRAM<br>16b<br>SDIO / MMC<br>DMA2<br>JTAG & SW<br>Arm Cortex-M4<br>168 MHz<br>NVIC<br>ETM<br>MPU<br>Ethernet MAC<br>10/100<br>DMA/<br>FIFO<br>USB<br>OTG HS<br>DMA2<br>8 Streams<br>FIFO<br>ART ACCEL/<br>CACHE<br>SRAM 112 KB<br>RNG<br>Camera<br>interface<br>PHY<br>USB<br>OTG FS<br>FIFO<br>AHB1 168 MHz<br>PHY<br>FIFO<br>POR/PDR<br>BOR<br>Supply<br>supervision<br>@VDDA<br>PVD<br>Int<br>POR<br>reset<br>XTAL 32 kHz<br>M AN A G T<br>RTC<br>RC<br>HS<br>FCLK<br>RC<br>L S<br>PWR<br>interface<br>IWDG<br>@VBAT<br>AWU<br>Reset &<br>clock<br>control<br>P L L1&2<br>PCLKx<br>Voltage<br>regulator<br>3.3 to 1.2 V<br>VDD<br>Power managmt<br>Backup register<br>AHB bus-matrix 8S7M<br>LS<br>Flash<br>up to<br>1 MB<br>SRAM, PSRAM, NOR Flash,<br>PC Card (ATA), NAND Flash<br>External memory<br>controller (FSMC)<br>TIM2<br>TIM3<br>TIM4<br>TIM5<br>TIM12<br>TIM13<br>TIM14<br>USART2<br>USART3<br><br>EXT IT. WKUP<br>D-BUS<br>FPU<br>    ax)<br>SRAM 16 KB<br>CCM data RAM 64 KB<br>AHB3<br>AHB2 168 MHz<br>I-BUS<br>S-BUS<br>DMA/<br>FIFO<br>DMA1<br>8 Streams<br>FIFO<br>GPIO PORT B<br>GPIO PORT C<br>GPIO PORT D<br>GPIO PORT E<br>GPIO PORT F<br>GPIO PORT G<br>GPIO PORT H<br>GPIO PORT I<br>TIM8 / PWM<br>16b<br>smcard<br>irDA<br>smcard<br>irDA<br>16b<br>16b<br>16b<br>32b<br>16b<br>16b<br>32b<br>DMA1<br>AHB/APB1<br>LS<br>HCLKx<br>XTAL OSC<br>4- 16MHz<br>FIFO<br>TIM9<br>16b<br>TIM10<br>16b<br>  MHz (max)<br>@VDD<br>@VDD<br>@VDDA|4 KB BKPSRAM<br>RTC<br>AWU<br>Backup register<br>LS<br>TIM2<br>TIM3<br>TIM4<br>TIM5<br>TIM12<br>TIM13<br>TIM14<br>USART2<br>USART3<br><br>smcard<br>irDA<br>smcard<br>irDA<br>16b<br>16b<br>16b<br>32b<br>16b<br>16b<br>32b<br>LS|4 KB BKPSRAM<br>RTC<br>AWU<br>Backup register<br>LS<br>TIM2<br>TIM3<br>TIM4<br>TIM5<br>TIM12<br>TIM13<br>TIM14<br>USART2<br>USART3<br><br>smcard<br>irDA<br>smcard<br>irDA<br>16b<br>16b<br>16b<br>32b<br>16b<br>16b<br>32b<br>LS|





































1. The camera interface and ethernet are available only on STM32F407xx devices.


<u>20/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**

## 3.1 Arm ® Cortex ® -M4 core with FPU and embedded flash and

**SRAM**


The Arm Cortex-M4 processor with FPU is the latest generation of Arm processors for
embedded systems. It was developed to provide a low-cost platform that meets the needs of
MCU implementation, with a reduced pin count and low-power consumption, while
delivering outstanding computational performance and an advanced response to interrupts.


The Arm Cortex-M4 32-bit RISC processor with FPU features exceptional code-efficiency,
delivering the high-performance expected from an Arm core in the memory size usually
associated with 8- and 16-bit devices.


The processor supports a set of DSP instructions which allow efficient signal processing and
complex algorithm execution.


Its single precision FPU (floating point unit) speeds up software development by using
metalanguage development tools, while avoiding saturation.


The STM32F405xx and STM32F407xx family is compatible with all Arm tools and software.


_Figure 5_ shows the general block diagram of the STM32F40xxx family.


_Note:_ _Cortex-M4 with FPU is binary compatible with Cortex-M3._

## **3.2 Adaptive real-time memory accelerator (ART Accelerator)**


The ART Accelerator is a memory accelerator which is optimized for STM32 industrystandard Arm <sup>®</sup> Cortex <sup>®</sup> -M4 with FPU processors. It balances the inherent performance
advantage of the Arm Cortex-M4 with FPU over flash memory technologies, which normally
requires the processor to wait for the flash memory at higher frequencies.


To release the processor full 210 DMIPS performance at this frequency, the accelerator
implements an instruction prefetch queue and branch cache, which increases program
execution speed from the 128-bit flash memory. Based on CoreMark benchmark, the
performance achieved thanks to the ART accelerator is equivalent to 0 wait state program
execution from flash memory at a CPU frequency up to 168 MHz.

## **3.3 Memory protection unit**


The memory protection unit (MPU) is used to manage the CPU accesses to memory to
prevent one task to accidentally corrupt the memory or resources used by any other active
task. This memory area is organized into up to 8 protected areas that can in turn be divided
up into 8 subareas. The protection area sizes are between 32 bytes and the whole 4
gigabytes of addressable memory.


The MPU is especially helpful for applications where some critical or certified code has to be
protected against the misbehavior of other tasks. It is usually managed by an RTOS (realtime operating system). If a program accesses a memory location that is prohibited by the
MPU, the RTOS can detect it and take action. In an RTOS environment, the kernel can
dynamically update the MPU area setting, based on the process to be executed.


The MPU is optional and can be bypassed for applications that do not need it.


<u>DS8626 Rev 12</u> <u>21/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**

## **3.4 Embedded flash memory**


The STM32F40xxx devices embed a flash memory of 512 Kbytes or 1 Mbytes available for
storing programs and data, plus 512 bytes of OTP memory.

## **3.5 CRC (cyclic redundancy check) calculation unit**


The CRC (cyclic redundancy check) calculation unit is used to get a CRC code from a 32-bit
data word and a fixed generator polynomial.


Among other applications, CRC-based techniques are used to verify data transmission or
storage integrity. In the scope of the EN/IEC 60335-1 standard, they offer a means of
verifying the flash memory integrity. The CRC calculation unit helps compute a software
signature during runtime, to be compared with a reference signature generated at link-time
and stored at a given memory location.

## **3.6 Embedded SRAM**


All STM32F40xxx products embed:

      - Up to 192 Kbytes of system SRAM including 64 Kbytes of CCM (core coupled memory)
data RAM

RAM memory is accessed (read/write) at CPU clock speed with 0 wait states.

      - 4 Kbytes of backup SRAM

This area is accessible only from the CPU. Its content is protected against possible
unwanted write accesses, and is retained in Standby or VBAT mode.

## **3.7 Multi-AHB bus matrix**


The 32-bit multi-AHB bus matrix interconnects all the masters (CPU, DMAs, Ethernet, USB
HS) and the slaves (flash memory, RAM, FSMC, AHB, and APB peripherals) and ensures a
seamless and efficient operation even when several high-speed peripherals work
simultaneously.


<u>22/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**

### **Figure 6. Multi-AHB matrix**














|GP<br>DMA2|Col2|Col3|Col4|
|---|---|---|---|
|GP<br>DMA2|DMA_P2|DMA_P2|DMA_P2|
|GP<br>DMA2|DMA_P2|E||






|Col1|ICODE|
|---|---|
||DCODE|
|||




|Col1|Col2|APB1|
|---|---|---|
||||


## **3.8 DMA controller (DMA)**





The devices feature two general-purpose dual-port DMAs (DMA1 and DMA2) with 8
streams each. They are able to manage memory-to-memory, peripheral-to-memory and
memory-to-peripheral transfers. They feature dedicated FIFOs for APB/AHB peripherals,
support burst transfer and are designed to provide the maximum peripheral bandwidth
(AHB/APB).


The two DMA controllers support circular buffer management, so that no specific code is
needed when the controller reaches the end of the buffer. The two DMA controllers also
have a double buffering feature, which automates the use and switching of two memory
buffers without requiring any special code.


Each stream is connected to dedicated hardware DMA requests, with support for software
trigger on each stream. Configuration is made by software and transfer sizes between
source and destination are independent.


<u>DS8626 Rev 12</u> <u>23/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**


The DMA can be used with the main peripherals:

      - SPI and I <sup>2</sup> S

      - I <sup>2</sup> C

      - USART

      - General-purpose, basic and advanced-control timers TIMx

      - DAC

      - SDIO

      - Camera interface (DCMI)

      - ADC.

## **3.9 Flexible static memory controller (FSMC)**


The FSMC is embedded in the STM32F405xx and STM32F407xx family. It has four Chip
Select outputs supporting the following modes: PCCard/CompactFlash, SRAM, PSRAM,
NOR flash and NAND flash.


Functionality overview:

      - Write FIFO

      - Maximum FSMC_CLK frequency for synchronous accesses is 60 MHz.

### **3.9.1 LCD parallel interface**


The FSMC can be configured to interface seamlessly with most graphic LCD controllers. It
supports the Intel 8080 and Motorola 6800 modes, and is flexible enough to adapt to
specific LCD interfaces. This LCD parallel interface capability makes it easy to build costeffective graphic applications using LCD modules with embedded controllers or high
performance solutions using external controllers with dedicated acceleration.

## **3.10 Nested vectored interrupt controller (NVIC)**


The STM32F405xx and STM32F407xx embed a nested vectored interrupt controller able to
manage 16 priority levels, and handle up to 82 maskable interrupt channels plus the 16
interrupt lines of the Cortex <sup>®</sup> -M4 with FPU core.

      - Closely coupled NVIC gives low-latency interrupt processing

      - Interrupt entry vector table address passed directly to the core

      - Allows early processing of interrupts

      - Processing of late arriving, higher-priority interrupts

      - Support tail chaining

      - Processor state automatically saved

      - Interrupt entry restored on interrupt exit with no instruction overhead


This hardware block provides flexible interrupt management features with minimum interrupt
latency.


<u>24/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**

## **3.11 External interrupt/event controller (EXTI)**


The external interrupt/event controller consists of 23 edge-detector lines used to generate
interrupt/event requests. Each line can be independently configured to select the trigger
event (rising edge, falling edge, both) and can be masked independently. A pending register
maintains the status of the interrupt requests. The EXTI can detect an external line with a
pulse width shorter than the Internal APB2 clock period. Up to 140 GPIOs can be connected
to the 16 external interrupt lines.

## **3.12 Clocks and startup**


On reset the 16 MHz internal RC oscillator is selected as the default CPU clock. The
16 MHz internal RC oscillator is factory-trimmed to offer 1% accuracy over the full
temperature range. The application can then select as system clock either the RC oscillator
or an external 4-26 MHz clock source. This clock can be monitored for failure. If a failure is
detected, the system automatically switches back to the internal RC oscillator and a
software interrupt is generated (if enabled). This clock source is input to a PLL thus allowing
to increase the frequency up to 168 MHz. Similarly, full interrupt management of the PLL
clock entry is available when necessary (for example if an indirectly used external oscillator
fails).


Several prescalers allow the configuration of the three AHB buses, the high-speed APB
(APB2) and the low-speed APB (APB1) domains. The maximum frequency of the three AHB
buses is 168 MHz while the maximum frequency of the high-speed APB domains is
84 MHz. The maximum allowed frequency of the low-speed APB domain is 42 MHz.


The devices embed a dedicated PLL (PLLI2S) which allows to achieve audio class
performance. In this case, the I <sup>2</sup> S master clock can generate all standard sampling
frequencies from 8 kHz to 192 kHz.

## **3.13 Boot modes**


At startup, boot pins are used to select one out of three boot options:

      - Boot from user flash

      - Boot from system memory

      - Boot from embedded SRAM


The boot loader is located in system memory. It is used to reprogram the flash memory by
using USART1 (PA9/PA10), USART3 (PC10/PC11 or PB10/PB11), CAN2 (PB5/PB13), USB
OTG FS in Device mode (PA11/PA12) through DFU (device firmware upgrade).

## **3.14 Power supply schemes**


      - VDD = 1.8 to 3.6 V: external power supply for I/Os and the internal regulator (when
enabled), provided externally through VDD pins.

      - VSSA, VDDA = 1.8 to 3.6 V: external analog power supplies for ADC, DAC, Reset
blocks, RCs and PLL. VDDA and VSSA must be connected to VDD and VSS, respectively.

      - VBAT = 1.65 to 3.6 V: power supply for RTC, external clock 32 kHz oscillator and
backup registers (through power switch) when VDD is not present.


<u>DS8626 Rev 12</u> <u>25/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**


Refer to _Figure 21: Power supply scheme_ for more details.


_Note:_ _VDD/VDDA minimum value of 1.7 V is obtained when the device operates in reduced_
_temperature range, and with the use of an external power supply supervisor (refer to_
_Section 3.15.2: Internal reset OFF)._

_Refer to Table 2 in order to identify the packages supporting this option._

## **3.15 Power supply supervisor**

### **3.15.1 Internal reset ON**


On packages embedding the PDR_ON pin, the power supply supervisor is enabled by
holding PDR_ON high. On all other packages, the power supply supervisor is always
enabled.


The device has an integrated power-on reset (POR) / power-down reset (PDR) circuitry
coupled with a Brownout reset (BOR) circuitry. At power-on, POR/PDR is always active and
ensures proper operation starting from 1.8 V. After the 1.8 V POR threshold level is
reached, the option byte loading process starts, either to confirm or modify default BOR
threshold levels, or to disable BOR permanently. Three BOR thresholds are available
through option bytes. The device remains in reset mode when VDD is below a specified
threshold, VPOR/PDR or VBOR, without the need for an external reset circuit.

The device also features an embedded programmable voltage detector (PVD) that monitors
the VDD/VDDA power supply and compares it to the VPVD threshold. An interrupt can be
generated when VDD/VDDA drops below the VPVD threshold and/or when VDD/VDDA is
higher than the VPVD threshold. The interrupt service routine can then generate a warning
message and/or put the MCU into a safe state. The PVD is enabled by software.

### **3.15.2 Internal reset OFF**


This feature is available only on packages featuring the PDR_ON pin. The internal power-on
reset (POR) / power-down reset (PDR) circuitry is disabled with the PDR_ON pin.


An external power supply supervisor should monitor VDD and should maintain the device in
reset mode as long as VDD is below a specified threshold. PDR_ON should be connected to
this external power supply supervisor. Refer to _Figure 7: Power supply supervisor_
_interconnection with internal reset OFF_ .


<u>26/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**

#### **Figure 7. Power supply supervisor interconnection with internal reset OFF**











1. PDR = 1.7 V for reduce temperature range; PDR = 1.8 V for all temperature range.

The VDD specified threshold, below which the device must be maintained under reset, is
#### 1.8 V (see Figure 7 ). This supply voltage can drop to 1.7 V when the device operates in the

0 to 70 °C temperature range.


A comprehensive set of power-saving mode allows to design low-power applications.


When the internal reset is OFF, the following integrated features are no more supported:

- The integrated power-on reset (POR) / power-down reset (PDR) circuitry is disabled

- The brownout reset (BOR) circuitry is disabled

- The embedded programmable voltage detector (PVD) is disabled

- VBAT functionality is no more available and VBAT pin should be connected to VDD

All packages, except for the LQFP64 and LQFP100, allow to disable the internal reset
through the PDR_ON signal.


<u>DS8626 Rev 12</u> <u>27/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**

#### **Figure 8. PDR_ON and NRST control with internal reset OFF**





1. PDR = 1.7 V for reduce temperature range; PDR = 1.8 V for all temperature range.

## **3.16 Voltage regulator**


The regulator has four operating modes:

      - Regulator ON

       - Main regulator mode (MR)

       - Low-power regulator (LPR)

       - Power-down

      - Regulator OFF

### **3.16.1 Regulator ON**


On packages embedding the BYPASS_REG pin, the regulator is enabled by holding
BYPASS_REG low. On all other packages, the regulator is always enabled.


There are three power modes configured by software when regulator is ON:

      - MR is used in the nominal regulation mode (With different voltage scaling in Run)

In Main regulator mode (MR mode), different voltage scaling are provided to reach the
best compromise between maximum frequency and dynamic power consumption.
Refer to _Table 14: General operating conditions_ .

      - LPR is used in the Stop modes

The LP regulator mode is configured by software when entering Stop mode.

      - Power-down is used in Standby mode.

The Power-down mode is activated only when entering in Standby mode. The regulator
output is in high impedance and the kernel circuitry is powered down, inducing zero
consumption. The contents of the registers and SRAM are lost)


<u>28/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**


Two external ceramic capacitors should be connected on VCAP_1 & VCAP_2 pin. Refer to
_Figure 21: Power supply scheme_ and _Figure 16: VCAP_1/VCAP_2 operating conditions_ .


All packages have regulator ON feature.

### **3.16.2 Regulator OFF**


This feature is available only on packages featuring the BYPASS_REG pin. The regulator is
disabled by holding BYPASS_REG high. The regulator OFF mode allows to supply
externally a V12 voltage source through VCAP_1 and VCAP_2 pins.

Since the internal voltage scaling is not manage internally, the external voltage value must
be aligned with the targeted maximum frequency. Refer to _Table 14: General operating_
_conditions_ .


The two 2.2 µF ceramic capacitors should be replaced by two 100 nF decoupling
capacitors.


Refer to _Figure 21: Power supply scheme_


When the regulator is OFF, there is no more internal monitoring on V12. An external power
supply supervisor should be used to monitor the V12 of the logic power domain. PA0 pin
should be used for this purpose, and act as power-on reset on V12 power domain.

In regulator OFF mode the following features are no more supported:

      - PA0 cannot be used as a GPIO pin since it allows to reset a part of the V12 logic power
domain which is not reset by the NRST pin.

      - As long as PA0 is kept low, the debug mode cannot be used under power-on reset. As
a consequence, PA0 and NRST pins must be managed separately if the debug
connection under reset or pre-reset is required.

      - The standby mode is not available

#### **Figure 9. Regulator OFF**





















<u>DS8626 Rev 12</u> <u>29/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**


The following conditions must be respected:

      - VDD should always be higher than VCAP_1 and VCAP_2 to avoid current injection
between power domains.

      - If the time for VCAP_1 and VCAP_2 to reach V12 minimum value is faster than the time for
VDD to reach 1.8 V, then PA0 should be kept low to cover both conditions: until VCAP_1
#### and VCAP_2 reach V12 minimum value and until VDD reaches 1.8 V (see Figure 10 ).

      - Otherwise, if the time for VCAP_1 and VCAP_2 to reach V12 minimum value is slower
than the time for VDD to reach 1.8 V, then PA0 could be asserted low externally (see
_Figure 11_ ).

      - If VCAP_1 and VCAP_2 go below V12 minimum value and VDD is higher than 1.8 V, then
a reset must be asserted on PA0 pin.


_Note:_ _The minimum value of_ V12 _depends on the maximum frequency targeted in the application_
_(see Table 14: General operating conditions)._

#### **Figure 10. Startup in regulator OFF mode: slow VDD slope**



|Col1|Col2|Col3|
|---|---|---|
||||
||||
|||NRST|


1. This figure is valid both whatever the internal reset mode (ON or OFF).

2. PDR = 1.7 V for reduced temperature range; PDR = 1.8 V for all temperature ranges.


<u>30/206</u> <u>DS8626 Rev 12</u>






**STM32F405xx, STM32F407xx** **Functional overview**

#### **Figure 11. Startup in regulator OFF mode: fast VDD slope**

|Col1|Col2|Col3|
|---|---|---|
||||
||||
|||PA0 asserted externally<br>NRST|



1. This figure is valid both whatever the internal reset mode (ON or OFF).

2. PDR = 1.7 V for a reduced temperature range; PDR = 1.8 V for all temperature ranges.

## **3.17 Regulator ON/OFF and internal reset ON/OFF availability**

### **Table 3. Regulator ON/OFF and internal reset ON/OFF availability**
















|Col1|Regulator ON|Regulator OFF|Internal reset ON|Internal reset<br>OFF|
|---|---|---|---|---|
|LQFP64<br>LQFP100|Yes|No|Yes|No|
|LQFP144|LQFP144|LQFP144|Yes<br>PDR_ON set to<br>VDD|Yes<br>PDR_ON<br>connected to an<br>external power<br>supply supervisor|
|WLCSP90<br>UFBGA176<br>LQFP176|Yes<br>BYPASS_REG set<br>to VSS|Yes<br>BYPASS_REG set<br>to VDD|Yes<br>BYPASS_REG set<br>to VDD|Yes<br>BYPASS_REG set<br>to VDD|


## **3.18 Real-time clock (RTC), backup SRAM and backup registers**

The backup domain of the STM32F405xx and STM32F407xx includes:

      - The real-time clock (RTC)

      - 4 Kbytes of backup SRAM

      - 20 backup registers


The real-time clock (RTC) is an independent BCD timer/counter. Dedicated registers contain
the second, minute, hour (in 12/24 hour), week day, date, month, year, in BCD (binarycoded decimal) format. Correction for 28, 29 (leap year), 30, and 31 day of the month are
performed automatically. The RTC provides a programmable alarm and programmable
periodic interrupts with wakeup from Stop and Standby modes. The sub-seconds value is
also available in binary format.


It is clocked by a 32.768 kHz external crystal, resonator or oscillator, the internal low-power
RC oscillator or the high-speed external clock divided by 2 to 31. The internal low-speed RC


<u>DS8626 Rev 12</u> <u>31/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**


has a typical frequency of 32 kHz. The RTC can be calibrated using an external 512 Hz
output to compensate for any natural quartz deviation.


Two alarm registers are used to generate an alarm at a specific time and calendar fields can
be independently masked for alarm comparison. To generate a periodic interrupt, a 16-bit
programmable binary auto-reload downcounter with programmable resolution is available
and allows automatic wakeup and periodic alarms from every 120 µs to every 36 hours.


A 20-bit prescaler is used for the time base clock. It is by default configured to generate a
time base of 1 second from a clock at 32.768 kHz.


The 4-Kbyte backup SRAM is an EEPROM-like memory area. It can be used to store data
which need to be retained in VBAT and standby mode. This memory area is disabled by
default to minimize power consumption (see _Section 3.19: Low-power modes_ ). It can be
enabled by software.


The backup registers are 32-bit registers used to store 80 bytes of user application data
when VDD power is not present. Backup registers are not reset by a system, a power reset,
or when the device wakes up from the Standby mode (see _Section 3.19: Low-power_
_modes_ ).


Additional 32-bit registers contain the programmable alarm subseconds, seconds, minutes,
hours, day, and date.


Like backup SRAM, the RTC and backup registers are supplied through a switch that is
powered either from the VDD supply when present or from the VBAT pin.

## **3.19 Low-power modes**


The STM32F405xx and STM32F407xx support three low-power modes to achieve the best
compromise between low-power consumption, short startup time and available wakeup
sources:

      - **Sleep mode**

In Sleep mode, only the CPU is stopped. All peripherals continue to operate and can
wake up the CPU when an interrupt/event occurs.

      - **Stop mode**

The Stop mode achieves the lowest power consumption while retaining the contents of
SRAM and registers. All clocks in the V12 domain are stopped, the PLL, the HSI RC
and the HSE crystal oscillators are disabled. The voltage regulator can also be put
either in normal or in low-power mode.

The device can be woken up from the Stop mode by any of the EXTI line (the EXTI line
source can be one of the 16 external lines, the PVD output, the RTC alarm / wakeup /
tamper / time stamp events, the USB OTG FS/HS wakeup or the Ethernet wakeup).

      - **Standby mode**

The Standby mode is used to achieve the lowest power consumption. The internal
voltage regulator is switched off so that the entire V12 domain is powered off. The PLL,
the HSI RC and the HSE crystal oscillators are also switched off. After entering


<u>32/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**


Standby mode, the SRAM and register contents are lost except for registers in the
backup domain and the backup SRAM when selected.

The device exits the Standby mode when an external reset (NRST pin), an IWDG reset,
a rising edge on the WKUP pin, or an RTC alarm / wakeup / tamper /time stamp event
occurs.

The standby mode is not supported when the embedded voltage regulator is bypassed
and the V12 domain is controlled by an external power.

## **3.20 VBAT operation**

The VBAT pin allows to power the device VBAT domain from an external battery, an external
supercapacitor, or from VDD when no external battery and an external supercapacitor are
present.


VBAT operation is activated when VDD is not present.

The VBAT pin supplies the RTC, the backup registers and the backup SRAM.

_Note:_ _When the microcontroller is supplied from VBAT, external interrupts and RTC alarm/events_
_do not exit it from VBAT operation._

_When PDR_ON pin is not connected to VDD (internal reset OFF), the VBAT functionality is no_
_more available and VBAT pin should be connected to VDD._

## **3.21 Timers and watchdogs**


The STM32F405xx and STM32F407xx devices include two advanced-control timers, eight
general-purpose timers, two basic timers and two watchdog timers.


All timer counters can be frozen in debug mode.

### Table 4 compares the features of the advanced-control, general-purpose and basic timers. **Table 4. Timer feature comparison**
























|Timer<br>type|Timer|Counter<br>resolution|Counter<br>type|Prescaler<br>factor|DMA<br>request<br>generation|Capture/<br>compare<br>channels|Complemen-<br>tary output|Max<br>interface<br>clock<br>(MHz)|Max<br>timer<br>clock<br>(MHz)|
|---|---|---|---|---|---|---|---|---|---|
|Advanced<br>-control|TIM1,<br>TIM8|16-bit|Up,<br>Down,<br>Up/down|Any integer<br>between 1<br>and 65536|Yes|4|Yes|84|168|



<u>DS8626 Rev 12</u> <u>33/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**


**<u>Table 4. Timer feature comparison (continued)</u>**










































|Timer<br>type|Timer|Counter<br>resolution|Counter<br>type|Prescaler<br>factor|DMA<br>request<br>generation|Capture/<br>compare<br>channels|Complemen-<br>tary output|Max<br>interface<br>clock<br>(MHz)|Max<br>timer<br>clock<br>(MHz)|
|---|---|---|---|---|---|---|---|---|---|
|General<br>purpose|TIM2,<br>TIM5|32-bit|Up,<br>Down,<br>Up/down|Any integer<br>between 1<br>and 65536|Yes|4|No|42|84|
|General<br>purpose|TIM3,<br>TIM4|16-bit|Up,<br>Down,<br>Up/down|Any integer<br>between 1<br>and 65536|Yes|4|No|42|84|
|General<br>purpose|TIM9|16-bit|Up|Any integer<br>between 1<br>and 65536|No|2|No|84|168|
|General<br>purpose|TIM10<br>, <br>TIM11|16-bit|Up|Any integer<br>between 1<br>and 65536|No|1|No|84|168|
|General<br>purpose|TIM12|16-bit|Up|Any integer<br>between 1<br>and 65536|No|2|No|42|84|
|General<br>purpose|TIM13<br>, <br>TIM14|16-bit|Up|Any integer<br>between 1<br>and 65536|No|1|No|42|84|
|Basic|TIM6,<br>TIM7|16-bit|Up|Any integer<br>between 1<br>and 65536|Yes|0|No|42|84|


### **3.21.1 Advanced-control timers (TIM1, TIM8)**

The advanced-control timers (TIM1, TIM8) can be seen as three-phase PWM generators
multiplexed on 6 channels. They have complementary PWM outputs with programmable
inserted dead times. They can also be considered as complete general-purpose timers.
Their 4 independent channels can be used for:

      - Input capture

      - Output compare

      - PWM generation (edge- or center-aligned modes)

      - One-pulse mode output


If configured as standard 16-bit timers, they have the same features as the general-purpose
TIMx timers. If configured as 16-bit PWM generators, they have full modulation capability (0100%).


The advanced-control timer can work together with the TIMx timers via the Timer Link
feature for synchronization or event chaining.


TIM1 and TIM8 support independent DMA request generation.


<u>34/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**

### **3.21.2 General-purpose timers (TIMx)**


There are ten synchronizable general-purpose timers embedded in the STM32F40xxx
devices (see _Table 4_ for differences).

      - **TIM2, TIM3, TIM4, TIM5**

The STM32F40xxx include 4 full-featured general-purpose timers: TIM2, TIM5, TIM3,
and TIM4.The TIM2 and TIM5 timers are based on a 32-bit auto-reload
up/downcounter and a 16-bit prescaler. The TIM3 and TIM4 timers are based on a 16bit auto-reload up/downcounter and a 16-bit prescaler. They all feature 4 independent
channels for input capture/output compare, PWM or one-pulse mode output. This gives
up to 16 input capture/output compare/PWMs on the largest packages.

The TIM2, TIM3, TIM4, TIM5 general-purpose timers can work together, or with the
other general-purpose timers and the advanced-control timers TIM1 and TIM8 via the
Timer Link feature for synchronization or event chaining.

Any of these general-purpose timers can be used to generate PWM outputs.

TIM2, TIM3, TIM4, TIM5 all have independent DMA request generation. They are
capable of handling quadrature (incremental) encoder signals and the digital outputs
from 1 to 4 hall-effect sensors.

      - **TIM9, TIM10, TIM11, TIM12, TIM13, and TIM14**

These timers are based on a 16-bit auto-reload upcounter and a 16-bit prescaler.
TIM10, TIM11, TIM13, and TIM14 feature one independent channel, whereas TIM9
and TIM12 have two independent channels for input capture/output compare, PWM or
one-pulse mode output. They can be synchronized with the TIM2, TIM3, TIM4, TIM5
full-featured general-purpose timers. They can also be used as simple time bases.

### **3.21.3 Basic timers TIM6 and TIM7**


These timers are mainly used for DAC trigger and waveform generation. They can also be
used as a generic 16-bit time base.


TIM6 and TIM7 support independent DMA request generation.


**Independent watchdog**


The independent watchdog is based on a 12-bit downcounter and 8-bit prescaler. It is
clocked from an independent 32 kHz internal RC and as it operates independently from the
main clock, it can operate in Stop and Standby modes. It can be used either as a watchdog
to reset the device when a problem occurs, or as a free-running timer for application timeout
management. It is hardware- or software-configurable through the option bytes.


**Window watchdog**


The window watchdog is based on a 7-bit downcounter that can be set as free-running. It
can be used as a watchdog to reset the device when a problem occurs. It is clocked from
the main clock. It has an early warning interrupt capability and the counter can be frozen in
debug mode.


<u>DS8626 Rev 12</u> <u>35/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**


**SysTick timer**


This timer is dedicated to real-time operating systems, but could also be used as a standard
downcounter. It features:

      - A 24-bit downcounter

      - Autoreload capability

      - Maskable system interrupt generation when the counter reaches 0

      - Programmable clock source.

## **3.22 Inter-integrated circuit interface (I²C)**


Up to three I²C bus interfaces can operate in multimaster and slave modes. They can
support the Standard-mode (up to 100 kHz) and Fast-mode (up to 400 kHz). They support
the 7/10-bit addressing mode and the 7-bit dual addressing mode (as slave). A hardware
CRC generation/verification is embedded.


They can be served by DMA and they support SMBus 2.0/PMBus.

## **3.23 Universal synchronous/asynchronous receiver transmitters**

**(USART)**


The STM32F405xx and STM32F407xx embed four universal synchronous/asynchronous
receiver transmitters (USART1, USART2, USART3 and USART6) and two universal
asynchronous receiver transmitters (UART4 and UART5).


These six interfaces provide asynchronous communication, IrDA SIR ENDEC support,
multiprocessor communication mode, single-wire half-duplex communication mode and
have LIN Master/Slave capability. The USART1 and USART6 interfaces are able to
communicate at speeds of up to 10.5 Mbit/s. The other available interfaces communicate at
up to 5.25 Mbit/s.


USART1, USART2, USART3 and USART6 also provide hardware management of the CTS
and RTS signals, Smart Card mode (ISO 7816 compliant) and SPI-like communication
capability. All interfaces can be served by the DMA controller.


<u>36/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**

### **Table 5. USART feature comparison**

















|USART<br>name|Standard<br>features|Modem<br>(RTS/<br>CTS)|LIN|SPI<br>master|irDA|Smartcard<br>(ISO 7816)|Max. baud rate<br>in Mbit/s<br>(oversampling<br>by 16)|Max. baud rate<br>in Mbit/s<br>(oversampling<br>by 8)|APB<br>mapping|
|---|---|---|---|---|---|---|---|---|---|
|USART1|X|X|X|X|X|X|5.25|10.5|APB2<br>(max.<br>84 MHz)|
|USART2|X|X|X|X|X|X|2.62|5.25|APB1<br>(max.<br>42 MHz)|
|USART3|X|X|X|X|X|X|2.62|5.25|APB1<br>(max.<br>42 MHz)|
|UART4|X|-|X|-|X|-|2.62|5.25|APB1<br>(max.<br>42 MHz)|
|UART5|X|-|X|-|X|-|2.62|5.25|APB1<br>(max.<br>42 MHz)|
|USART6|X|X|X|X|X|X|5.25|10.5|APB2<br>(max.<br>84 MHz)|

## **3.24 Serial peripheral interface (SPI)**

The STM32F40xxx feature up to three SPIs in slave and master modes in full-duplex and
simplex communication modes. SPI1 can communicate at up to 42 Mbits/s, SPI2 and SPI3
can communicate at up to 21 Mbit/s. The 3-bit prescaler gives 8 master mode frequencies
and the frame is configurable to 8 bits or 16 bits. The hardware CRC generation/verification
supports basic SD Card/MMC modes. All SPIs can be served by the DMA controller.


The SPI interface can be configured to operate in TI mode for communications in master
mode and slave mode.

## **3.25 Inter-integrated sound (I 2 S)**

Two standard I <sup>2</sup> S interfaces (multiplexed with SPI2 and SPI3) are available. They can be
operated in master or slave mode, in full duplex and half-duplex communication modes, and
can be configured to operate with a 16-/32-bit resolution as an input or output channel.
Audio sampling frequencies from 8 kHz up to 192 kHz are supported. When either or both of
the I <sup>2</sup> S interfaces is/are configured in master mode, the master clock can be output to the
external DAC/CODEC at 256 times the sampling frequency.

All I <sup>2</sup> Sx can be served by the DMA controller.


<u>DS8626 Rev 12</u> <u>37/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**

## **3.26 Audio PLL (PLLI2S)**

The devices feature an additional dedicated PLL for audio I <sup>2</sup> S application. It allows to
achieve error-free I <sup>2</sup> S sampling clock accuracy without compromising on the CPU
performance, while using USB peripherals.

The PLLI2S configuration can be modified to manage an I <sup>2</sup> S sample rate change without
disabling the main PLL (PLL) used for CPU, USB and Ethernet interfaces.


The audio PLL can be programmed with very low error to obtain sampling rates ranging
from 8 KHz to 192 KHz.

In addition to the audio PLL, a master clock input pin can be used to synchronize the I <sup>2</sup> S
flow with an external PLL (or Codec output).

## **3.27 Secure digital input/output interface (SDIO)**


An SD/SDIO/MMC host interface is available, that supports MultiMediaCard System
Specification Version 4.2 in three different databus modes: 1-bit (default), 4-bit and 8-bit.


The interface allows data transfer at up to 48 MHz, and is compliant with the SD Memory
Card Specification Version 2.0.


The SDIO Card Specification Version 2.0 is also supported with two different databus
modes: 1-bit (default) and 4-bit.


The current version supports only one SD/SDIO/MMC4.2 card at any one time and a stack
of MMC4.1 or previous.


In addition to SD/SDIO/MMC, this interface is fully compliant with the CE-ATA digital
protocol Rev1.1.

## **3.28 Ethernet MAC interface with dedicated DMA and IEEE 1588**

**support**


Peripheral available only on the STM32F407xx devices.


The STM32F407xx devices provide an IEEE-802.3-2002-compliant media access controller
(MAC) for ethernet LAN communications through an industry-standard mediumindependent interface (MII) or a reduced medium-independent interface (RMII). The
STM32F407xx requires an external physical interface device (PHY) to connect to the
physical LAN bus (twisted-pair, fiber, etc.). the PHY is connected to the STM32F407xx MII
port using 17 signals for MII or 9 signals for RMII, and can be clocked using the 25 MHz
(MII) from the STM32F407xx.


<u>38/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**


The STM32F407xx includes the following features:

      - Supports 10 and 100 Mbit/s rates

      - Dedicated DMA controller allowing high-speed transfers between the dedicated SRAM
and the descriptors (see the STM32F40xxx/41xxx reference manual for details)

      - Tagged MAC frame support (VLAN support)

      - Half-duplex (CSMA/CD) and full-duplex operation

      - MAC control sublayer (control frames) support

      - 32-bit CRC generation and removal

      - Several address filtering modes for physical and multicast address (multicast and
group addresses)

      - 32-bit status code for each transmitted or received frame

      - Internal FIFOs to buffer transmit and receive frames. The transmit FIFO and the
receive FIFO are both 2 Kbytes.

      - Supports hardware PTP (precision time protocol) in accordance with IEEE 1588 2008
(PTP V2) with the time stamp comparator connected to the TIM2 input

      - Triggers interrupt when system time becomes greater than target time

## **3.29 Controller area network (bxCAN)**


The two CANs are compliant with the 2.0A and B (active) specifications with a bitrate up to 1
Mbit/s. They can receive and transmit standard frames with 11-bit identifiers as well as
extended frames with 29-bit identifiers. Each CAN has three transmit mailboxes, two receive
FIFOS with 3 stages and 28 shared scalable filter banks (all of them can be used even if one
CAN is used). 256 bytes of SRAM are allocated for each CAN.

## **3.30 Universal serial bus on-the-go full-speed (OTG_FS)**


The STM32F405xx and STM32F407xx embed an USB OTG full-speed device/host/OTG
peripheral with integrated transceivers. The USB OTG FS peripheral is compliant with the
USB 2.0 specification and with the OTG 1.0 specification. It has software-configurable
endpoint setting and supports suspend/resume. The USB OTG full-speed controller
requires a dedicated 48 MHz clock that is generated by a PLL connected to the HSE
oscillator. The major features are:

      - Combined Rx and Tx FIFO size of 320 × 35 bits with dynamic FIFO sizing

      - Supports the session request protocol (SRP) and host negotiation protocol (HNP)

      - 4 bidirectional endpoints

      - 8 host channels with periodic OUT support

      - HNP/SNP/IP inside (no need for any external resistor)

      - For OTG/Host modes, a power switch is needed in case bus-powered devices are
connected


<u>DS8626 Rev 12</u> <u>39/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**

## **3.31 Universal serial bus on-the-go high-speed (OTG_HS)**


The STM32F405xx and STM32F407xx devices embed a USB OTG high-speed (up to
480 Mb/s) device/host/OTG peripheral. The USB OTG HS supports both full-speed and
high-speed operations. It integrates the transceivers for full-speed operation (12 MB/s) and
features a UTMI low-pin interface (ULPI) for high-speed operation (480 MB/s). When using
the USB OTG HS in HS mode, an external PHY device connected to the ULPI is required.


The USB OTG HS peripheral is compliant with the USB 2.0 specification and with the OTG
1.0 specification. It has software-configurable endpoint setting and supports
suspend/resume. The USB OTG full-speed controller requires a dedicated 48 MHz clock
that is generated by a PLL connected to the HSE oscillator.


The major features are:

      - Combined Rx and Tx FIFO size of 1 Kbit × 35 with dynamic FIFO sizing

      - Supports the session request protocol (SRP) and host negotiation protocol (HNP)

      - 6 bidirectional endpoints

      - 12 host channels with periodic OUT support

      - Internal FS OTG PHY support

      - External HS or HS OTG operation supporting ULPI in SDR mode. The OTG PHY is
connected to the microcontroller ULPI port through 12 signals. It can be clocked using
the 60 MHz output.

      - Internal USB DMA

      - HNP/SNP/IP inside (no need for any external resistor)

      - for OTG/Host modes, a power switch is needed in case bus-powered devices are
connected

## **3.32 Digital camera interface (DCMI)**


The camera interface is _not_ available in STM32F405xx devices.


STM32F407xx products embed a camera interface that can connect with camera modules
and CMOS sensors through an 8-bit to 14-bit parallel interface, to receive video data. The
camera interface can sustain a data transfer rate up to 54 Mbyte/s at 54 MHz. It features:

      - Programmable polarity for the input pixel clock and synchronization signals

      - Parallel data communication can be 8-, 10-, 12- or 14-bit

      - Supports 8-bit progressive video monochrome or raw bayer format, YCbCr 4:2:2
progressive video, RGB 565 progressive video or compressed data (like JPEG)

      - Supports continuous mode or snapshot (a single frame) mode

      - Capability to automatically crop the image

## **3.33 True random number generator (RNG)**


All STM32F405xx and STM32F407xx products embed a true random number generator
(RNG) that provides full entropy outputs to the application as 32-bit samples. It is composed
of a live entropy source (analog) and an internal conditioning component.


<u>40/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Functional overview**

## **3.34 General-purpose input/outputs (GPIOs)**


Each of the GPIO pins can be configured by software as output (push-pull or open-drain,
with or without pull-up or pull-down), as input (floating, with or without pull-up or pull-down)
or as peripheral alternate function. Most of the GPIO pins are shared with digital or analog
alternate functions. All GPIOs are high-current-capable and have speed selection to better
manage internal noise, power consumption and electromagnetic emission.


The I/O configuration can be locked if needed by following a specific sequence in order to
avoid spurious writing to the I/Os registers.


Fast I/O handling allowing maximum I/O toggling up to 84 MHz.

## **3.35 Analog-to-digital converters (ADCs)**


Three 12-bit analog-to-digital converters are embedded and each ADC shares up to 16
external channels, performing conversions in the single-shot or scan mode. In scan mode,
automatic conversion is performed on a selected group of analog inputs.


Additional logic functions embedded in the ADC interface allow:

      - Simultaneous sample and hold

      - Interleaved sample and hold


The ADC can be served by the DMA controller. An analog watchdog feature allows very
precise monitoring of the converted voltage of one, some or all selected channels. An
interrupt is generated when the converted voltage is outside the programmed thresholds.


To synchronize A/D conversion and timers, the ADCs could be triggered by any of TIM1,
TIM2, TIM3, TIM4, TIM5, or TIM8 timer.

## **3.36 Temperature sensor**


The temperature sensor has to generate a voltage that varies linearly with temperature. The
conversion range is between 1.8 V and 3.6 V. The temperature sensor is internally
connected to the ADC1_IN16 input channel which is used to convert the sensor output
voltage into a digital value.


As the offset of the temperature sensor varies from chip to chip due to process variation, the
internal temperature sensor is mainly suitable for applications that detect temperature
changes instead of absolute temperatures. If an accurate temperature reading is needed,
then an external temperature sensor part should be used.

## **3.37 Digital-to-analog converter (DAC)**


The two 12-bit buffered DAC channels can be used to convert two digital signals into two
analog voltage signal outputs.


<u>DS8626 Rev 12</u> <u>41/206</u>



191


**Functional overview** **STM32F405xx, STM32F407xx**


This dual digital Interface supports the following features:

      - two DAC converters: one for each output channel

      - 8-bit or 12-bit monotonic output

      - left or right data alignment in 12-bit mode

      - synchronized update capability

      - noise-wave generation

      - triangular-wave generation

      - dual DAC channel independent or simultaneous conversions

      - DMA capability for each channel

      - external triggers for conversion

      - input voltage reference VREF+

Eight DAC trigger inputs are used in the device. The DAC channels are triggered through
the timer update outputs that are also connected to different DMA streams.

## **3.38 Serial wire JTAG debug port (SWJ-DP)**


The Arm SWJ-DP interface is embedded, and is a combined JTAG and serial wire debug
port that enables either a serial wire debug or a JTAG probe to be connected to the target.


Debug is performed using 2 pins only instead of 5 required by the JTAG (JTAG pins could
be re-use as GPIO with alternate function): the JTAG TMS and TCK pins are shared with
SWDIO and SWCLK, respectively, and a specific sequence on the TMS pin is used to
switch between JTAG-DP and SW-DP.

## **3.39 Embedded Trace Macrocell™**


The Arm Embedded Trace Macrocell provides a greater visibility of the instruction and data
flow inside the CPU core by streaming compressed data at a very high rate from the
STM32F40xxx through a small number of ETM pins to an external hardware trace port
analyser (TPA) device. The TPA is connected to a host computer using USB, Ethernet, or
any other high-speed channel. Real-time instruction and data flow activity can be recorded
and then formatted for display on the host computer that runs the debugger software. TPA
hardware is commercially available from common development tool vendors.


The Embedded Trace Macrocell operates with third party debugger software tools.


<u>42/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Pinouts and pin description**

# **4 Pinouts and pin description**

## **Figure 12. STM32F40xxx LQFP64 pinout**













1. The above figure shows the package top view.


<u>DS8626 Rev 12</u> <u>43/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**

## **Figure 13. STM32F40xxx LQFP100 pinout**













1. The above figure shows the package top view.


<u>44/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Pinouts and pin description**

## **Figure 14. STM32F40xxx LQFP144 pinout**





















1. The above figure shows the package top view.



<u>DS8626 Rev 12</u> <u>45/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**

## **Figure 15. STM32F40xxx LQFP176 pinout**





























1. The above figure shows the package top view.


<u>46/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Pinouts and pin description**

## **Figure 16. STM32F40xxx UFBGA176 ballout**


1 2 **3** 4 5 6 7 8 9 10 11 12 13 14 15


|VSS|VSS|VSS|VSS|VSS|
|---|---|---|---|---|
|VSS|VSS|VSS|VSS|VSS|
|VSS|VSS|VSS|VSS|VSS|
|VSS|VSS|VSS|VSS|VSS|
|VSS|VSS|VSS|VSS|VSS|







|PE3|PE2|PE1|PE0|PB8|PB5|PG14|PG13|PB4|PB3|PD7|PC12|PA15|PA14|PA13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PE4|PE5|PE6|PB9|PB7|PB6|PG15|PG12|PG11|PG10|PD6|PD0|PC11|PC10|PA12|
|VBAT|PI7|PI6|PI5|VDD|PDR_ON|VDD|VDD|VDD|PG9|PD5|PD1|PI3|PI2|PA11|
|PC13|PI8|PI9|PI4|VSS|BOOT0|VSS|VSS|VSS|PD4|PD3|PD2|PH15|PI1|PA10|
|PC14|PF0|PI10|PI11|VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS|VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS|VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS|VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS|VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS|VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS|VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS|PH13|PH14|PI0|PA9|
|PC15|VSS|VDD|PH2|PH2|PH2|PH2|PH2|PH2|PH2|PH2|VSS|VCAP_2|PC9|PA8|
|PH0|VSS|VDD|PH3|PH3|PH3|PH3|PH3|PH3|PH3|PH3|VSS|VDD|PC8|PC7|
|PH1|PF2|PF1|PH4|PH4|PH4|PH4|PH4|PH4|PH4|PH4|VSS|VDD|PG8|PC6|
|NRST|PF3|PF4|PH5|PH5|PH5|PH5|PH5|PH5|PH5|PH5|VDD|VDD|PG7|PG6|
|PF7|PF6|PF5|VDD|VDD|VDD|VDD|VDD|VDD|VDD|VDD|PH12|PG5|PG4|PG3|
|PF10|PF9|PF8|BYPASS_<br>REG|BYPASS_<br>REG|BYPASS_<br>REG|BYPASS_<br>REG|BYPASS_<br>REG|BYPASS_<br>REG|BYPASS_<br>REG|BYPASS_<br>REG|PH11|PH10|PD15|PG2|
|VSSA|PC0|PC1|PC2|PC3|PB2|PG1|VSS|VSS|VCAP_1|PH6|PH8|PH9|PD14|PD13|
|VREF-|PA1|PA0|PA4|PC4|PF13|PG0|VDD|VDD|VDD|PE13|PH7|PD12|PD11|PD10|
|VREF+|PA2|PA6|PA5|PC5|PF12|PF15|PE8|PE9|PE11|PE14|PB12|PB13|PD9|PD8|
|VDDA|PA3|PA7|PB1|PB0|PF11|PF14|PE7|PE10|PE12|PE15|PB10|PB11|PB14|PB15|


ai18497b


1. This figure shows the package top view.


<u>DS8626 Rev 12</u> <u>47/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**

## **Figure 17. STM32F40xxx WLCSP90 ballout**


























































|10|9|8|7|6|5|4|3|2|1|
|---|---|---|---|---|---|---|---|---|---|
|VBAT|PC13|PDR_ON|BOOT0|PB4|PD7|PD4|PC12|PA14|VDD|
|PC14|PC15|VDD|PB7|PB3|PD6|PD2|PA15|PI1|VCAP_2|
|PA0|VSS|PB9|PB6|PD5|PD1|PC11|PI0|PA12|PA11|
|PC2|BYPASS_<br>REG|PB8<br>|PB5|PD0|PC10|PA13|PA10|PA9|PA8|
|PC0|PC3|VSS|VSS|VDD|VSS|VDD|PC9|PC8|PC7|
|PH0|PH1|PA1|VDD|PE10|PE14|VCAP_1|PC6|PD14|PD15|
|NRST|VDDA|PA5|PB0|PE7|PE13|PE15|PD10|PD12|PD11|
|VSSA|PA3|PA6|PB1|PE8|PE12|PB10|PD9|PD8|PB15|
|PA2|PA4<br>|PA7|PB2|PE9|PE11|PB11|PB12|PB14|PB13|



MS30402V1


1. This figure shows the package bump view.

## **Table 6. Legend/abbreviations used in the pinout table**







|Name|Abbreviation|Definition|
|---|---|---|
|Pin name|Unless otherwise specified in brackets below the pin name, the pin function during and after<br>reset is the same as the actual pin name|Unless otherwise specified in brackets below the pin name, the pin function during and after<br>reset is the same as the actual pin name|
|Pin type|S|Supply pin|
|Pin type|I|Input only pin|
|Pin type|I/O|Input / output pin|
|I/O structure|FT|5 V tolerant I/O|
|I/O structure|TTa|3.3 V tolerant I/O directly connected to ADC|
|I/O structure|B|Dedicated BOOT0 pin|
|I/O structure|RST|Bidirectional reset pin with embedded weak pull-up resistor|
|Notes|Unless otherwise specified by a note, all I/Os are set as floating inputs during and after reset|Unless otherwise specified by a note, all I/Os are set as floating inputs during and after reset|
|Alternate<br>functions|Functions selected through GPIOx_AFR registers|Functions selected through GPIOx_AFR registers|
|Additional<br>functions|Functions directly selected/enabled through peripheral registers|Functions directly selected/enabled through peripheral registers|


<u>48/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Pinouts and pin description**

## **Table 7. STM32F40xxx pin and ball definitions (1)**







































|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|-|-|1|1|A2|1|PE2|I/O|FT|-|TRACECLK/ FSMC_A23 /<br>ETH_MII_TXD3 /<br>EVENTOUT|-|
|-|-|2|2|A1|2|PE3|I/O|FT|-|TRACED0/FSMC_A19 /<br>EVENTOUT|-|
|-|-|3|3|B1|3|PE4|I/O|FT|-|TRACED1/FSMC_A20 /<br>DCMI_D4/ EVENTOUT|-|
|-|-|4|4|B2|4|PE5|I/O|FT|-|TRACED2 / FSMC_A21 /<br>TIM9_CH1 / DCMI_D6 /<br>EVENTOUT|-|
|-|-|5|5|B3|5|PE6|I/O|FT|-|TRACED3 / FSMC_A22 /<br>TIM9_CH2 / DCMI_D7 /<br>EVENTOUT|-|
|1|A10|6|6|C1|6|VBAT|S|-|-|-|-|
|-|-|-|-|D2|7|PI8|I/O|FT|(3)(<br>4)|-|RTC_TAMP1,<br>RTC_TAMP2,<br>RTC_TS|
|2|A9|7|7|D1|8|PC13|I/O|FT|(3)<br>(4)|-|RTC_OUT,<br>RTC_TAMP1,<br>RTC_TS|
|3|B10|8|8|E1|9|PC14/OSC32_IN<br>(PC14)|I/O|FT|(3)(<br>4)|-|OSC32_IN(5)|
|4|B9|9|9|F1|10|PC15/<br>OSC32_OUT<br>(PC15)|I/O|FT|(3)(<br>4)|-|OSC32_OUT(5)|
|-|-|-|-|D3|11|PI9|I/O|FT|-|CAN1_RX / EVENTOUT|-|
|-|-|-|-|E3|12|PI10|I/O|FT|-|ETH_MII_RX_ER /<br>EVENTOUT|-|
|-|-|-|-|E4|13|PI11|I/O|FT|-|OTG_HS_ULPI_DIR /<br>EVENTOUT|-|
|-|-|-|-|F2|14|VSS|S|-|-|-|-|
|-|-|-|-|F3|15|VDD|S|-|-|-|-|
|-|-|-|10|E2|16|PF0|I/O|FT|-|FSMC_A0 / I2C2_SDA /<br>EVENTOUT|-|


<u>DS8626 Rev 12</u> <u>49/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**



























|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|-|-|-|11|H3|17|PF1|I/O|FT|-|FSMC_A1 / I2C2_SCL /<br>EVENTOUT|-|
|-|-|-|12|H2|18|PF2|I/O|FT|-|FSMC_A2 / I2C2_SMBA /<br>EVENTOUT|-|
|-|-|-|13|J2|19|PF3|I/O|FT|(5)|FSMC_A3/EVENTOUT|ADC3_IN9|
|-|-|-|14|J3|20|PF4|I/O|FT|(5)|FSMC_A4/EVENTOUT|ADC3_IN14|
|-|-|-|15|K3|21|PF5|I/O|FT|(5)|FSMC_A5/EVENTOUT|ADC3_IN15|
|-|C9|10|16|G2|22|VSS|S|-|-|-|-|
|-|B8|11|17|G3|23|VDD|S|-|-|-|-|
|-|-|-|18|K2|24|PF6|I/O|FT|(5)|TIM10_CH1 /<br>FSMC_NIORD/<br>EVENTOUT|ADC3_IN4|
|-|-|-|19|K1|25|PF7|I/O|FT|(5)|TIM11_CH1/FSMC_NREG/<br>EVENTOUT|ADC3_IN5|
|-|-|-|20|L3|26|PF8|I/O|FT|(5)|TIM13_CH1 /<br>FSMC_NIOWR/<br>EVENTOUT|ADC3_IN6|
|-|-|-|21|L2|27|PF9|I/O|FT|(5)|TIM14_CH1 / FSMC_CD/<br>EVENTOUT|ADC3_IN7|
|-|-|-|22|L1|28|PF10|I/O|FT|(5)|FSMC_INTR/ EVENTOUT|ADC3_IN8|
|5|F10|12|23|G1|29|PH0/OSC_IN<br>(PH0)|I/O|FT|-|EVENTOUT|OSC_IN(5)|
|6|F9|13|24|H1|30|PH1/OSC_OUT<br>(PH1)|I/O|FT|-|EVENTOUT|OSC_OUT(5)|
|7|G10|14|25|J1|31|NRST|I/O|RST|-|-|-|
|8|E10|15|26|M2|32|PC0|I/O|FT|(5)|OTG_HS_ULPI_STP/<br>EVENTOUT|ADC123_IN10|
|9|-|16|27|M3|33|PC1|I/O|FT|(5)|ETH_MDC/ EVENTOUT|ADC123_IN11|
|10|D10|17|28|M4|34|PC2|I/O|FT|(5)|SPI2_MISO /<br>OTG_HS_ULPI_DIR /<br>ETH_MII_TXD2<br>/I2S2ext_SD/ EVENTOUT|ADC123_IN12|


<u>50/206</u> <u>DS8626 Rev 12</u>






**STM32F405xx, STM32F407xx** **Pinouts and pin description**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**



































|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|11|E9|18|29|M5|35|PC3|I/O|FT|(5)|SPI2_MOSI / I2S2_SD /<br>OTG_HS_ULPI_NXT /<br>ETH_MII_TX_CLK**/** <br>EVENTOUT|ADC123_IN13|
|-|-|19|30|-|36|VDD|S|-|-|-|-|
|12|H10|20|31|M1|37|VSSA|S|-|-|-|-|
|-|-|-|-|N1|-|VREF–|S|-|-|-|-|
|-|-|21|32|P1|38|VREF+|S|-|-|-|-|
|13|G9|22|33|R1|39|VDDA|S|-|-|-|-|
|14|C10|23|34|N3|40|PA0/WKUP<br>(PA0)|I/O|FT|(6)|USART2_CTS/<br>UART4_TX/<br>ETH_MII_CRS /<br>TIM2_CH1_ETR/<br>TIM5_CH1 / TIM8_ETR/<br>EVENTOUT|ADC123_IN0/WK<br>UP(5)|
|15|F8|24|35|N2|41|PA1|I/O|FT|(5)|USART2_RTS /<br>UART4_RX/<br>ETH_RMII_REF_CLK /<br>ETH_MII_RX_CLK /<br>TIM5_CH2 / TIM2_CH2/<br>EVENTOUT|ADC123_IN1|
|16|J10|25|36|P2|42|PA2|I/O|FT|(5)|USART2_TX/TIM5_CH3 /<br>TIM9_CH1 / TIM2_CH3 /<br>ETH_MDIO/ EVENTOUT|ADC123_IN2|
|-|-|-|-|F4|43|PH2|I/O|FT|-|ETH_MII_CRS/EVENTOUT|-|
|-|-|-|-|G4|44|PH3|I/O|FT|-|ETH_MII_COL/EVENTOUT|-|
|-|-|-|-|H4|45|PH4|I/O|FT|-|I2C2_SCL /<br>OTG_HS_ULPI_NXT/<br>EVENTOUT|-|
|-|-|-|-|J4|46|PH5|I/O|FT|-|I2C2_SDA/ EVENTOUT|-|
|17|H9|26|37|R2|47|PA3|I/O|FT|(5)|USART2_RX/TIM5_CH4 /<br>TIM9_CH2 / TIM2_CH4 /<br>OTG_HS_ULPI_D0 /<br>ETH_MII_COL/<br>EVENTOUT|ADC123_IN3|
|18|E5|27|38|-|-|VSS|S|-|-|-|-|


<u>DS8626 Rev 12</u> <u>51/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**















|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|-|D9|-|-|L4|48|BYPASS_REG|I|FT|-|-|-|
|19|E4|28|39|K4|49|VDD|S|-|-|-|-|
|20|J9|29|40|N4|50|PA4|I/O|TTa|(5)|SPI1_NSS / SPI3_NSS /<br>USART2_CK /<br>DCMI_HSYNC /<br>OTG_HS_SOF/ I2S3_WS/<br>EVENTOUT|ADC12_IN4<br>/DAC_OUT1|
|21|G8|30|41|P4|51|PA5|I/O|TTa|(5)|SPI1_SCK/<br>OTG_HS_ULPI_CK /<br>TIM2_CH1_ETR/<br>TIM8_CH1N/ EVENTOUT|ADC12_IN5/DAC<br>_OUT2|
|22|H8|31|42|P3|52|PA6|I/O|FT|(5)|SPI1_MISO /<br>TIM8_BKIN/TIM13_CH1 /<br>DCMI_PIXCLK / TIM3_CH1<br>/ TIM1_BKIN**/** EVENTOUT|ADC12_IN6|
|23|J8|32|43|R3|53|PA7|I/O|FT|(5)|SPI1_MOSI/ TIM8_CH1N /<br>TIM14_CH1/TIM3_CH2/<br>ETH_MII_RX_DV /<br>TIM1_CH1N /<br>ETH_RMII_CRS_DV/<br>EVENTOUT|ADC12_IN7|
|24|-|33|44|N5|54|PC4|I/O|FT|(5)|ETH_RMII_RX_D0 /<br>ETH_MII_RX_D0/<br>EVENTOUT|ADC12_IN14|
|25|-|34|45|P5|55|PC5|I/O|FT|(5)|ETH_RMII_RX_D1 /<br>ETH_MII_RX_D1/<br>EVENTOUT|ADC12_IN15|
|26|G7|35|46|R5|56|PB0|I/O|FT|(5)|TIM3_CH3 / TIM8_CH2N/<br>OTG_HS_ULPI_D1/<br>ETH_MII_RXD2 /<br>TIM1_CH2N/ EVENTOUT|ADC12_IN8|
|27|H7|36|47|R4|57|PB1|I/O|FT|(5)|TIM3_CH4 / TIM8_CH3N/<br>OTG_HS_ULPI_D2/<br>ETH_MII_RXD3 /<br>TIM1_CH3N/ EVENTOUT|ADC12_IN9|
|28|J7|37|48|M6|58|PB2/BOOT1<br>(PB2)|I/O|FT|-|EVENTOUT|-|


<u>52/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Pinouts and pin description**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**







|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|-|-|-|49|R6|59|PF11|I/O|FT|-|DCMI_D12/ EVENTOUT|-|
|-|-|-|50|P6|60|PF12|I/O|FT|-|FSMC_A6/ EVENTOUT|-|
|-|-|-|51|M8|61|VSS|S|-|-|-|-|
|-|-|-|52|N8|62|VDD|S|-|-|-|-|
|-|-|-|53|N6|63|PF13|I/O|FT|-|FSMC_A7/ EVENTOUT|-|
|-|-|-|54|R7|64|PF14|I/O|FT|-|FSMC_A8/ EVENTOUT|-|
|-|-|-|55|P7|65|PF15|I/O|FT|-|FSMC_A9/ EVENTOUT|-|
|-|-|-|56|N7|66|PG0|I/O|FT|-|FSMC_A10/ EVENTOUT|-|
|-|-|-|57|M7|67|PG1|I/O|FT|-|FSMC_A11/ EVENTOUT|-|
|-|G6|38|58|R8|68|PE7|I/O|FT|-|FSMC_D4/TIM1_ETR/<br>EVENTOUT|-|
|-|H6|39|59|P8|69|PE8|I/O|FT|-|FSMC_D5/ TIM1_CH1N/<br>EVENTOUT|-|
|-|J6|40|60|P9|70|PE9|I/O|FT|-|FSMC_D6/TIM1_CH1/<br>EVENTOUT|-|
|-|-|-|61|M9|71|VSS|S|-|-|-|-|
|-|-|-|62|N9|72|VDD|S|-|-|-|-|
|-|F6|41|63|R9|73|PE10|I/O|FT|-|FSMC_D7/TIM1_CH2N/<br>EVENTOUT|-|
|-|J5|42|64|P10|74|PE11|I/O|FT|-|FSMC_D8/TIM1_CH2/<br>EVENTOUT|-|
|-|H5|43|65|R10|75|PE12|I/O|FT|-|FSMC_D9/TIM1_CH3N/<br>EVENTOUT|-|
|-|G5|44|66|N11|76|PE13|I/O|FT|-|FSMC_D10/TIM1_CH3/<br>EVENTOUT|-|
|-|F5|45|67|P11|77|PE14|I/O|FT|-|FSMC_D11/TIM1_CH4/<br>EVENTOUT|-|
|-|G4|46|68|R11|78|PE15|I/O|FT|-|FSMC_D12/TIM1_BKIN/<br>EVENTOUT|-|


<u>DS8626 Rev 12</u> <u>53/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**



























|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|29|H4|47|69|R12|79|PB10|I/O|FT|-|SPI2_SCK / I2S2_CK /<br>I2C2_SCL/ USART3_TX /<br>OTG_HS_ULPI_D3 /<br>ETH_MII_RX_ER /<br>TIM2_CH3/ EVENTOUT|-|
|30|J4|48|70|R13|80|PB11|I/O|FT|-|I2C2_SDA/USART3_RX/<br>OTG_HS_ULPI_D4 /<br>ETH_RMII_TX_EN/<br>ETH_MII_TX_EN /<br>TIM2_CH4/ EVENTOUT|-|
|31|F4|49|71|M10|81|VCAP_1|S|-|-|-|-|
|32|-|50|72|N10|82|VDD|S|-|-|-|-|
|-|-|-|-|M11|83|PH6|I/O|FT|-|I2C2_SMBA / TIM12_CH1 /<br>ETH_MII_RXD2/<br>EVENTOUT|-|
|-|-|-|-|N12|84|PH7|I/O|FT|-|I2C3_SCL /<br>ETH_MII_RXD3/<br>EVENTOUT|-|
|-|-|-|-|M12|85|PH8|I/O|FT|-|I2C3_SDA /<br>DCMI_HSYNC/<br>EVENTOUT|-|
|-|-|-|-|M13|86|PH9|I/O|FT|-|I2C3_SMBA / TIM12_CH2/<br>DCMI_D0/ EVENTOUT|-|
|-|-|-|-|L13|87|PH10|I/O|FT|-|TIM5_CH1 / DCMI_D1/<br>EVENTOUT|-|
|-|-|-|-|L12|88|PH11|I/O|FT|-|TIM5_CH2 / DCMI_D2/<br>EVENTOUT|-|
|-|-|-|-|K12|89|PH12|I/O|FT|-|TIM5_CH3 / DCMI_D3/<br>EVENTOUT|-|
|-|-|-|-|H12|90|VSS|S|-|-|-|-|
|-|-|-|-|J12|91|VDD|S|-|-|-|-|


<u>54/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Pinouts and pin description**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**






















|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|33|J3|51|73|P12|92|PB12|I/O|FT|-|SPI2_NSS / I2S2_WS /<br>I2C2_SMBA/<br>USART3_CK/ TIM1_BKIN /<br>CAN2_RX /<br>OTG_HS_ULPI_D5/<br>ETH_RMII_TXD0 /<br>ETH_MII_TXD0/<br>OTG_HS_ID/ EVENTOUT|-|
|34|J1|52|74|P13|93|PB13|I/O|FT|-|SPI2_SCK / I2S2_CK /<br>USART3_CTS/<br>TIM1_CH1N /CAN2_TX /<br>OTG_HS_ULPI_D6 /<br>ETH_RMII_TXD1 /<br>ETH_MII_TXD1/<br>EVENTOUT|OTG_HS_VBUS|
|35|J2|53|75|R14|94|PB14|I/O|FT|-|SPI2_MISO/ TIM1_CH2N /<br>TIM12_CH1 /<br>OTG_HS_DM/<br>USART3_RTS /<br>TIM8_CH2N/I2S2ext_SD/<br>EVENTOUT|-|
|36|H1|54|76|R15|95|PB15|I/O|FT|-|SPI2_MOSI / I2S2_SD/<br>TIM1_CH3N / TIM8_CH3N<br>/ TIM12_CH2 /<br>OTG_HS_DP/ EVENTOUT|RTC_REFIN|
|-|H2|55|77|P15|96|PD8|I/O|FT|-|FSMC_D13 / USART3_TX/<br>EVENTOUT|-|
|-|H3|56|78|P14|97|PD9|I/O|FT|-|FSMC_D14 / USART3_RX/<br>EVENTOUT|-|
|-|G3|57|79|N15|98|PD10|I/O|FT|-|FSMC_D15 / USART3_CK/<br>EVENTOUT|-|
|-|G1|58|80|N14|99|PD11|I/O|FT|-|FSMC_CLE /<br>FSMC_A16/USART3_CTS/<br>EVENTOUT|-|
|-|G2|59|81|N13|100|PD12|I/O|FT|-|FSMC_ALE/<br>FSMC_A17/TIM4_CH1 /<br>USART3_RTS/<br>EVENTOUT|-|



<u>DS8626 Rev 12</u> <u>55/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**

















|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|-|-|60|82|M15|101|PD13|I/O|FT|-|FSMC_A18/TIM4_CH2/<br>EVENTOUT|-|
|-|-|-|83|-|102|VSS|S|-|-|-|-|
|-|-|-|84|J13|103|VDD|S|-|-|-|-|
|-|F2|61|85|M14|104|PD14|I/O|FT|-|FSMC_D0/TIM4_CH3/<br>EVENTOUT/ EVENTOUT|-|
|-|F1|62|86|L14|105|PD15|I/O|FT|-|FSMC_D1/TIM4_CH4/<br>EVENTOUT|-|
|-|-|-|87|L15|106|PG2|I/O|FT|-|FSMC_A12/ EVENTOUT|-|
|-|-|-|88|K15|107|PG3|I/O|FT|-|FSMC_A13/ EVENTOUT|-|
|-|-|-|89|K14|108|PG4|I/O|FT|-|FSMC_A14/ EVENTOUT|-|
|-|-|-|90|K13|109|PG5|I/O|FT|-|FSMC_A15/ EVENTOUT|-|
|-|-|-|91|J15|110|PG6|I/O|FT|-|FSMC_INT2/ EVENTOUT|-|
|-|-|-|92|J14|111|PG7|I/O|FT|-|FSMC_INT3 /USART6_CK/<br>EVENTOUT|-|
|-|-|-|93|H14|112|PG8|I/O|FT|-|USART6_RTS /<br>ETH_PPS_OUT/<br>EVENTOUT|-|
|-|-|-|94|G12|113|VSS|S||-|-|-|
|-|-|-|95|H13|114|VDD|S||-|-|-|
|37|F3|63|96|H15|115|PC6|I/O|FT|-|I2S2_MCK /<br>TIM8_CH1/SDIO_D6 /<br>USART6_TX /<br>DCMI_D0/TIM3_CH1/<br>EVENTOUT|-|
|38|E1|64|97|G15|116|PC7|I/O|FT|-|I2S3_MCK /<br>TIM8_CH2/SDIO_D7 /<br>USART6_RX /<br>DCMI_D1/TIM3_CH2/<br>EVENTOUT|-|
|39|E2|65|98|G14|117|PC8|I/O|FT|-|TIM8_CH3/SDIO_D0<br>/TIM3_CH3/ USART6_CK /<br>DCMI_D2/ EVENTOUT|-|


<u>56/206</u> <u>DS8626 Rev 12</u>






**STM32F405xx, STM32F407xx** **Pinouts and pin description**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**



















|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|40|E3|66|99|F14|118|PC9|I/O|FT|-|I2S_CKIN/ MCO2 /<br>TIM8_CH4/SDIO_D1 /<br>/I2C3_SDA / DCMI_D3 /<br>TIM3_CH4/ EVENTOUT|-|
|41|D1|67|100|F15|119|PA8|I/O|FT|-|MCO1 / USART1_CK/<br>TIM1_CH1/ I2C3_SCL/<br>OTG_FS_SOF/<br>EVENTOUT|-|
|42|D2|68|101|E15|120|PA9|I/O|FT|-|USART1_TX/ TIM1_CH2 /<br>I2C3_SMBA / DCMI_D0/<br>EVENTOUT|OTG_FS_VBUS|
|43|D3|69|102|D15|121|PA10|I/O|FT|-|USART1_RX/ TIM1_CH3/<br>OTG_FS_ID/DCMI_D1/<br>EVENTOUT|-|
|44|C1|70|103|C15|122|PA11|I/O|FT|-|USART1_CTS / CAN1_RX<br>/ TIM1_CH4 /<br>OTG_FS_DM/ EVENTOUT|-|
|45|C2|71|104|B15|123|PA12|I/O|FT|-|USART1_RTS / CAN1_TX/<br>TIM1_ETR/ OTG_FS_DP/<br>EVENTOUT|-|
|46|D4|72|105|A15|124|PA13<br>(JTMS-SWDIO)|I/O|FT|-|JTMS-SWDIO/ EVENTOUT|-|
|47|B1|73|106|F13|125|VCAP_2|S|-|-|-|-|
|-|E7|74|107|F12|126|VSS|S|-|-|-|-|
|48|E6|75|108|G13|127|VDD|S|-|-|-|-|
|-|-|-|-|E12|128|PH13|I/O|FT|-|TIM8_CH1N / CAN1_TX/<br>EVENTOUT|-|
|-|-|-|-|E13|129|PH14|I/O|FT|-|TIM8_CH2N / DCMI_D4/<br>EVENTOUT|-|
|-|-|-|-|D13|130|PH15|I/O|FT|-|TIM8_CH3N / DCMI_D11/<br>EVENTOUT|-|
|-|C3|-|-|E14|131|PI0|I/O|FT|-|TIM5_CH4 / SPI2_NSS /<br>I2S2_WS / DCMI_D13/<br>EVENTOUT|-|
|-|B2|-|-|D14|132|PI1|I/O|FT|-|SPI2_SCK / I2S2_CK /<br>DCMI_D8/ EVENTOUT|-|


<u>DS8626 Rev 12</u> <u>57/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**























|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|-|-|-|-|C14|133|PI2|I/O|FT|-|TIM8_CH4 /SPI2_MISO /<br>DCMI_D9 / I2S2ext_SD/<br>EVENTOUT|-|
|-|-|-|-|C13|134|PI3|I/O|FT|-|TIM8_ETR / SPI2_MOSI /<br>I2S2_SD / DCMI_D10/<br>EVENTOUT|-|
|-|-|-|-|D9|135|VSS|S|-|-|-|-|
|-|-|-|-|C9|136|VDD|S|-|-|-|-|
|49|A2|76|109|A14|137|PA14<br>(JTCK/SWCLK)|I/O|FT|-|JTCK-SWCLK/ EVENTOUT|-|
|50|B3|77|110|A13|138|PA15<br>(JTDI)|I/O|FT|-|JTDI/ SPI3_NSS/<br>I2S3_WS/TIM2_CH1_ETR<br>/ SPI1_NSS / EVENTOUT|-|
|51|D5|78|111|B14|139|PC10|I/O|FT|-|SPI3_SCK / I2S3_CK/<br>UART4_TX/SDIO_D2 /<br>DCMI_D8 / USART3_TX/<br>EVENTOUT|-|
|52|C4|79|112|B13|140|PC11|I/O|FT|-|UART4_RX/ SPI3_MISO /<br>SDIO_D3 /<br>DCMI_D4/USART3_RX /<br>I2S3ext_SD/ EVENTOUT|-|
|53|A3|80|113|A12|141|PC12|I/O|FT|-|UART5_TX/SDIO_CK /<br>DCMI_D9 / SPI3_MOSI<br>/I2S3_SD / USART3_CK/<br>EVENTOUT|-|
|-|D6|81|114|B12|142|PD0|I/O|FT|-|FSMC_D2/CAN1_RX/<br>EVENTOUT|-|
|-|C5|82|115|C12|143|PD1|I/O|FT|-|FSMC_D3 / CAN1_TX/<br>EVENTOUT|-|
|54|B4|83|116|D12|144|PD2|I/O|FT|-|TIM3_ETR/UART5_RX/<br>SDIO_CMD / DCMI_D11/<br>EVENTOUT|-|
|-|-|84|117|D11|145|PD3|I/O|FT|-|FSMC_CLK/<br>USART2_CTS/<br>EVENTOUT|-|


<u>58/206</u> <u>DS8626 Rev 12</u>






**STM32F405xx, STM32F407xx** **Pinouts and pin description**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**



























|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|-|A4|85|118|D10|146|PD4|I/O|FT|-|FSMC_NOE/<br>USART2_RTS/<br>EVENTOUT|-|
|-|C6|86|119|C11|147|PD5|I/O|FT|-|FSMC_NWE/USART2_TX/<br>EVENTOUT|-|
|-|-|-|120|D8|148|VSS|S|-|-|-|-|
|-|-|-|121|C8|149|VDD|S|-|-|-|-|
|-|B5|87|122|B11|150|PD6|I/O|FT|-|FSMC_NWAIT/<br>USART2_RX/ EVENTOUT|-|
|-|A5|88|123|A11|151|PD7|I/O|FT|-|USART2_CK/FSMC_NE1/<br>FSMC_NCE2/ EVENTOUT|-|
|-|-|-|124|C10|152|PG9|I/O|FT|-|USART6_RX /<br>FSMC_NE2/FSMC_NCE3/<br>EVENTOUT|-|
|-|-|-|125|B10|153|PG10|I/O|FT|-|FSMC_NCE4_1/<br>FSMC_NE3/ EVENTOUT|-|
|-|-|-|126|B9|154|PG11|I/O|FT|-|FSMC_NCE4_2 /<br>ETH_MII_TX_EN/<br>ETH _RMII_TX_EN/<br>EVENTOUT|-|
|-|-|-|127|B8|155|PG12|I/O|FT|-|FSMC_NE4 /<br>USART6_RTS/<br>EVENTOUT|-|
|-|-|-|128|A8|156|PG13|I/O|FT|-|FSMC_A24 /<br>USART6_CTS<br>/ETH_MII_TXD0/<br>ETH_RMII_TXD0/<br>EVENTOUT|-|
|-|-|-|129|A7|157|PG14|I/O|FT|-|FSMC_A25 / USART6_TX<br>/ETH_MII_TXD1/<br>ETH_RMII_TXD1/<br>EVENTOUT|-|
|-|E8|-|130|D7|158|VSS|S|-|-|-|-|
|-|F7|-|131|C7|159|VDD|S|-|-|-|-|
|-|-|-|132|B7|160|PG15|I/O|FT|-|USART6_CTS /<br>DCMI_D13/ EVENTOUT|-|


<u>DS8626 Rev 12</u> <u>59/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**



























|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|55|B6|89|133|A10|161|PB3<br>(JTDO/<br>TRACESWO)|I/O|FT|-|JTDO/ TRACESWO/<br>SPI3_SCK / I2S3_CK /<br>TIM2_CH2 / SPI1_SCK/<br>EVENTOUT|-|
|56|A6|90|134|A9|162|PB4<br>(NJTRST)|I/O|FT|-|NJTRST/ SPI3_MISO /<br>TIM3_CH1 / SPI1_MISO /<br>I2S3ext_SD/ EVENTOUT|-|
|57|D7|91|135|A6|163|PB5|I/O|FT|-|I2C1_SMBA/ CAN2_RX /<br>OTG_HS_ULPI_D7 /<br>ETH_PPS_OUT/TIM3_CH2<br>/ SPI1_MOSI/ SPI3_MOSI /<br>DCMI_D10 / I2S3_SD/<br>EVENTOUT|-|
|58|C7|92|136|B6|164|PB6|I/O|FT|-|I2C1_SCL/ TIM4_CH1 /<br>CAN2_TX /<br>DCMI_D5/USART1_TX/<br>EVENTOUT|-|
|59|B7|93|137|B5|165|PB7|I/O|FT|-|I2C1_SDA / FSMC_NL /<br>DCMI_VSYNC /<br>USART1_RX/ TIM4_CH2/<br>EVENTOUT|-|
|60|A7|94|138|D6|166|BOOT0|I|B|-|-|VPP|
|61|D8|95|139|A5|167|PB8|I/O|FT|-|TIM4_CH3/SDIO_D4/<br>TIM10_CH1 / DCMI_D6 /<br>ETH_MII_TXD3 /<br>I2C1_SCL/ CAN1_RX/<br>EVENTOUT|-|
|62|C8|96|140|B4|168|PB9|I/O|FT|-|SPI2_NSS/ I2S2_WS /<br>TIM4_CH4/ TIM11_CH1/<br>SDIO_D5 / DCMI_D7 /<br>I2C1_SDA / CAN1_TX/<br>EVENTOUT|-|
|-|-|97|141|A4|169|PE0|I/O|FT|-|TIM4_ETR / FSMC_NBL0 /<br>DCMI_D2/ EVENTOUT|-|
|-|-|98|142|A3|170|PE1|I/O|FT|-|FSMC_NBL1 / DCMI_D3/<br>EVENTOUT|-|
|63|-|99|-|D5|-|VSS|S|-|-|-|-|


<u>60/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Pinouts and pin description**


**<u>Table 7. STM32F40xxx pin and ball definitions</u>** <sup>**(1)**</sup> **<u>(continued)</u>**


















|Pin number|Col2|Col3|Col4|Col5|Col6|Pin name<br>(function after<br>reset)(2)|Pin type|I / O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP64**|**WLCSP90**|**LQFP100**|**LQFP144**|**UFBGA176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|**LQFP176**|
|-|A8|-|143|C6|171|PDR_ON|I|FT|-|-|-|
|64|A1|10<br>0|144|C5|172|VDD|S|-|-|-|-|
|-|-|-|-|D4|173|PI4|I/O|FT|-|TIM8_BKIN / DCMI_D5/<br>EVENTOUT|-|
|-|-|-|-|C4|174|PI5|I/O|FT|-|TIM8_CH1 /<br>DCMI_VSYNC/<br>EVENTOUT|-|
|-|-|-|-|C3|175|PI6|I/O|FT|-|TIM8_CH2 / DCMI_D6/<br>EVENTOUT|-|
|-|-|-|-|C2|176|PI7|I/O|FT|-|TIM8_CH3 / DCMI_D7/<br>EVENTOUT|-|



1. UFBGA176 F6, F7, F8, F9, F10, G6, G7, G8, G9, G10, H6, H7, H8, H9, H10, J6, J7, J8, J9, J10, K6, K7, K8, K9 and K10
balls are connected to VSS for heat dissipation and package mechanical stability.

2. Function availability depends on the chosen device.


3. PC13, PC14, PC15 and PI8 are supplied through the power switch. Since the switch only sinks a limited amount of current
(3 mA), the use of GPIOs PC13 to PC15 and PI8 in output mode is limited:

  - The speed should not exceed 2 MHz with a maximum load of 30 pF.

  - These I/Os must not be used as a current source (e.g. to drive an LED).


4. Main function after the first backup domain power-up. Later on, it depends on the contents of the RTC registers even after
reset (because these registers are not reset by the main reset). For details on how to manage these I/Os, refer to the RTC
register description sections in the STM32F4xx reference manual, available from the STMicroelectronics website:
_www.st.com_ .


5. FT = 5 V tolerant except when in analog mode or oscillator mode (for PC14, PC15, PH0 and PH1).


6. If the device is delivered in an UFBGA176 or WLCSP90 and the BYPASS_REG pin is set to VDD (Regulator off/internal
reset ON mode), then PA0 is used as an internal Reset (active low).











|Col1|Table 8. FSMC pin definition|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Pins(1)**|**FSMC**|**FSMC**|**FSMC**|**FSMC**|**LQFP100(2)**|**WLCSP90**<br>**(2)**|
|**Pins(1)**|**CF**|**NOR/PSRAM/**<br>**SRAM**|**NOR/PSRAM Mux**|**NAND 16 bit**|**NAND 16 bit**|**NAND 16 bit**|
|PE2|-|A23|A23|-|Yes|-|
|PE3|-|A19|A19|-|Yes|-|
|PE4|-|A20|A20|-|Yes|-|
|PE5|-|A21|A21|-|Yes|-|
|PE6|-|A22|A22|-|Yes|-|


<u>DS8626 Rev 12</u> <u>61/206</u>



191


**Pinouts and pin description** **STM32F405xx, STM32F407xx**


**<u>Table 8. FSMC pin definition (continued)</u>**











|Pins(1)|FSMC|Col3|Col4|Col5|LQFP100(2)|WLCSP90<br>(2)|
|---|---|---|---|---|---|---|
|**Pins(1)**|**CF**|**NOR/PSRAM/**<br>**SRAM**|**NOR/PSRAM Mux**|**NAND 16 bit**|**NAND 16 bit**|**NAND 16 bit**|
|PF0|A0|A0|-|-|-|-|
|PF1|A1|A1|-|-|-|-|
|PF2|A2|A2|-|-|-|-|
|PF3|A3|A3|-|-|-|-|
|PF4|A4|A4|-|-|-|-|
|PF5|A5|A5|-|-|-|-|
|PF6|NIORD|-|-|-|-|-|
|PF7|NREG|-|-|-|-|-|
|PF8|NIOWR|-|-|-|-|-|
|PF9|CD|-|-|-|-|-|
|PF10|INTR|-|-|-|-|-|
|PF12|A6|A6|-|-|-|-|
|PF13|A7|A7|-|-|-|-|
|PF14|A8|A8|-|-|-|-|
|PF15|A9|A9|-|-|-|-|
|PG0|A10|A10|-|-|-|-|
|PG1|-|A11|-|-|-|-|
|PE7|D4|D4|DA4|D4|Yes|Yes|
|PE8|D5|D5|DA5|D5|Yes|Yes|
|PE9|D6|D6|DA6|D6|Yes|Yes|
|PE10|D7|D7|DA7|D7|Yes|Yes|
|PE11|D8|D8|DA8|D8|Yes|Yes|
|PE12|D9|D9|DA9|D9|Yes|Yes|
|PE13|D10|D10|DA10|D10|Yes|Yes|
|PE14|D11|D11|DA11|D11|Yes|Yes|
|PE15|D12|D12|DA12|D12|Yes|Yes|
|PD8|D13|D13|DA13|D13|Yes|Yes|
|PD9|D14|D14|DA14|D14|Yes|Yes|
|PD10|D15|D15|DA15|D15|Yes|Yes|
|PD11|-|A16|A16|CLE|Yes|Yes|
|PD12|-|A17|A17|ALE|Yes|Yes|
|PD13|-|A18|A18|-|Yes|-|
|PD14|D0|D0|DA0|D0|Yes|Yes|


<u>62/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Pinouts and pin description**


**<u>Table 8. FSMC pin definition (continued)</u>**











|Pins(1)|FSMC|Col3|Col4|Col5|LQFP100(2)|WLCSP90<br>(2)|
|---|---|---|---|---|---|---|
|**Pins(1)**|**CF**|**NOR/PSRAM/**<br>**SRAM**|**NOR/PSRAM Mux**|**NAND 16 bit**|**NAND 16 bit**|**NAND 16 bit**|
|PD15|D1|D1|DA1|D1|Yes|Yes|
|PG2|-|A12|-|-|-|-|
|PG3|-|A13|-|-|-|-|
|PG4|-|A14|-|-|-|-|
|PG5|-|A15|-|-|-|-|
|PG6|-|-|-|INT2|-|-|
|PG7|-|-|-|INT3|-|-|
|PD0|D2|D2|DA2|D2|Yes|Yes|
|PD1|D3|D3|DA3|D3|Yes|Yes|
|PD3|-|CLK|CLK|-|Yes|-|
|PD4|NOE|NOE|NOE|NOE|Yes|Yes|
|PD5|NWE|NWE|NWE|NWE|Yes|Yes|
|PD6|NWAIT|NWAIT|NWAIT|NWAIT|Yes|Yes|
|PD7|-|NE1|NE1|NCE2|Yes|Yes|
|PG9|-|NE2|NE2|NCE3|-|-|
|PG10|NCE4_1|NE3|NE3|-|-|-|
|PG11|NCE4_2|-|-|-|-|-|
|PG12|-|NE4|NE4|-|-|-|
|PG13|-|A24|A24|-|-|-|
|PG14|-|A25|A25|-|-|-|
|PB7|-|NADV|NADV|-|Yes|Yes|
|PE0|-|NBL0|NBL0|-|Yes|-|
|PE1|-|NBL1|NBL1|-|Yes|-|


1. Full FSMC features are available on LQFP144, LQFP176, and UFBGA176. The features available on
smaller packages are given in the dedicated package column.


2. Ports F and G are not available in devices delivered in 100-pin packages.


<u>DS8626 Rev 12</u> <u>63/206</u>



191


## **Table 9. Alternate function mapping**


























































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port A|PA0|-|TIM2_CH1_<br>ETR|TIM 5_CH1|TIM8_ETR|-|-|-|USART2_CTS|UART4_TX|-|-|ETH_MII_CRS|-|-|-|EVENTOUT|
|Port A|PA1|-|TIM2_CH2|TIM5_CH2|-|-|-|-|USART2_RTS|UART4_RX|-|-|ETH_MII<br>_RX_CLK<br>ETH_RMII__REF<br>_CLK|-|-|-|EVENTOUT|
|Port A|PA2|-|TIM2_CH3|TIM5_CH3|TIM9_CH1|-|-|-|USART2_TX|-|-|-|ETH_MDIO|-|-|-|EVENTOUT|
|Port A|PA3|-|TIM2_CH4|TIM5_CH4|TIM9_CH2|-|-|-|USART2_RX|-|-|OTG_HS_ULPI_<br>D0|ETH _MII_COL|-|-|-|EVENTOUT|
|Port A|PA4|-|-|-|-|-|SPI1_NSS|SPI3_NSS<br>I2S3_WS|USART2_CK|-|-|-|-|OTG_HS_SOF|DCMI_<br>HSYNC|-|EVENTOUT|
|Port A|PA5|-|TIM2_CH1_<br>ETR|-|TIM8_CH1N|-|SPI1_SCK|-|-|-|-|OTG_HS_ULPI_<br>CK|-|-|-|-|EVENTOUT|
|Port A|PA6|-|TIM1_BKIN|TIM3_CH1|TIM8_BKIN|-|SPI1_MISO|-|-|-|TIM13_CH1|-|-|-|DCMI_<br>PIXCLK|-|EVENTOUT|
|Port A|PA7|-|TIM1_CH1N|TIM3_CH2|TIM8_CH1N|-|SPI1_MOSI|-|-|-|TIM14_CH1|-|ETH_MII _RX_DV<br>ETH_RMII<br>_CRS_DV|-|-|-|EVENTOUT|
|Port A|PA8|MCO1|TIM1_CH1|-|-|I2C3_SCL|-|-|USART1_CK|-|-|OTG_FS_SOF|-|-|-|-|EVENTOUT|
|Port A|PA9|-|TIM1_CH2|-|-|I2C3_<br>SMBA|-|-|USART1_TX|-|-|-|-|-|DCMI_D0|-|EVENTOUT|
|Port A|PA10|-|TIM1_CH3|-|-|-|-|-|USART1_RX|-|-|OTG_FS_ID|-|-|DCMI_D1|-|EVENTOUT|
|Port A|PA11|-|TIM1_CH4|-|-|-|-|-|USART1_CTS|-|CAN1_RX|OTG_FS_DM|-|-|-|-|EVENTOUT|
|Port A|PA12|-|TIM1_ETR|-|-|-|-|-|USART1_RTS|-|CAN1_TX|OTG_FS_DP|-|-|-|-|EVENTOUT|
|Port A|PA13|JTMS-<br>SWDIO|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENTOUT|
|Port A|PA14|JTCK-<br>SWCLK|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENTOUT|
|Port A|PA15|JTDI|TIM 2_CH1<br>TIM 2_ETR|-|-|-|SPI1_NSS|SPI3_NSS/<br>I2S3_WS|-|-|-|-|-|-|-|-|EVENTOUT|


**<u>Table 9. Alternate function mapping (continued)</u>**


















































































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port B|PB0|-|TIM1_CH2N|TIM3_CH3|TIM8_CH2N|-|-|-|-|-|-|OTG_HS_ULPI_<br>D1|ETH _MII_RXD2|-|-|-|EVENTOUT|
|Port B|PB1|-|TIM1_CH3N|TIM3_CH4|TIM8_CH3N||-|-|-|-|-|OTG_HS_ULPI_<br>D2|ETH _MII_RXD3|-|-|-|EVENTOUT|
|Port B|PB2|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENTOUT|
|Port B|PB3|JTDO/<br>TRACES<br>WO|TIM2_CH2|-|-|-|SPI1_SCK|SPI3_SCK<br>I2S3_CK|-|-|-|-|-|-|-|-|EVENTOUT|
|Port B|PB4|NJTRST|-|TIM3_CH1||-|SPI1_MISO|SPI3_MISO|I2S3ext_SD|-|-|-|-|-|-|-|EVENTOUT|
|Port B|PB5|-|-|TIM3_CH2||I2C1_SMB<br>A|SPI1_MOSI|SPI3_MOSI<br>I2S3_SD|-|-|CAN2_RX|OTG_HS_ULPI_<br>D7|ETH _PPS_OUT|-|DCMI_D10|-|EVENTOUT|
|Port B|PB6|-|-|TIM4_CH1||I2C1_SCL|-|-|USART1_TX|-|CAN2_TX|-|-|-|DCMI_D5|-|EVENTOUT|
|Port B|PB7|-|-|TIM4_CH2||I2C1_SDA|-|-|USART1_RX|-|-|-|-|FSMC_NL|DCMI_VSYN<br>C|-|EVENTOUT|
|Port B|PB8|-|-|TIM4_CH3|TIM10_CH1|I2C1_SCL|-|-|-|-|CAN1_RX|-|ETH _MII_TXD3|SDIO_D4|DCMI_D6|-|EVENTOUT|
|Port B|PB9|-|-|TIM4_CH4|TIM11_CH1|I2C1_SDA|SPI2_NSS<br>I2S2_WS|-|-|-|CAN1_TX|-|-|SDIO_D5|DCMI_D7|-|EVENTOUT|
|Port B|PB10|-|TIM2_CH3|-|-|I2C2_SCL|SPI2_SCK<br>I2S2_CK|-|USART3_TX|-|-|OTG_HS_ULPI_<br>D3|ETH_ MII_RX_ER|-|-|-|EVENTOUT|
|Port B|PB11|-|TIM2_CH4|-|-|I2C2_SDA|-|-|USART3_RX|-|-|OTG_HS_ULPI_<br>D4|ETH _MII_TX_EN<br>ETH<br>_RMII_TX_EN|-|-|-|EVENTOUT|
|Port B|PB12|-|TIM1_BKIN|-|-|I2C2_<br>SMBA|SPI2_NSS<br>I2S2_WS|-|USART3_CK|-|CAN2_RX|OTG_HS_ULPI_<br>D5|ETH _MII_TXD0<br>ETH _RMII_TXD0|OTG_HS_ID|-|-|EVENTOUT|
|Port B|PB13|-|TIM1_CH1N|-|-|-|SPI2_SCK<br>I2S2_CK|-|USART3_CTS|-|CAN2_TX|OTG_HS_ULPI_<br>D6|ETH _MII_TXD1<br>ETH _RMII_TXD1|-|-|-|EVENTOUT|
|Port B|PB14|-|TIM1_CH2N|-|TIM8_CH2N|-|SPI2_MISO|I2S2ext_SD|USART3_RTS|-|TIM12_CH1|-|-|OTG_HS_DM|-|-|EVENTOUT|
|Port B|PB15|RTC_<br>REFIN|TIM1_CH3N|-|TIM8_CH3N|-|SPI2_MOSI<br>I2S2_SD|-|-|-|TIM12_CH2|-|-|OTG_HS_DP|-|-|EVENTOUT|


**<u>Table 9. Alternate function mapping (continued)</u>**












































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port C|PC0|-|-|-|-|-|-|-|-|-|-|OTG_HS_ULPI_<br>STP|-|-|-|-|EVENTOUT|
|Port C|PC1|-|-|-|-|-|-|-|-|-|-|-|ETH_MDC|-|-|-|EVENTOUT|
|Port C|PC2|-|-|-|-|-|SPI2_MISO|I2S2ext_SD|-|-|-|OTG_HS_ULPI_<br>DIR|ETH _MII_TXD2|-|-|-|EVENTOUT|
|Port C|PC3|-|-|-|-|-|SPI2_MOSI<br>I2S2_SD|-|-|-|-|OTG_HS_ULPI_<br>NXT|ETH<br>_MII_TX_CLK|-|-|-|EVENTOUT|
|Port C|PC4|-|-|-|-|-|-|-|-|-|-|-|ETH_MII_RXD0<br>ETH_RMII_RXD0|-|-|-|EVENTOUT|
|Port C|PC5|-|-|-|-|-|-|-|-|-|-|-|ETH _MII_RXD1<br>ETH _RMII_RXD1|-|-|-|EVENTOUT|
|Port C|PC6|-|-|TIM3_CH1|TIM8_CH1||I2S2_MCK||-|USART6_TX|-|-|-|SDIO_D6|DCMI_D0|-|EVENTOUT|
|Port C|PC7|-|-|TIM3_CH2|TIM8_CH2|-|-|I2S3_MCK|-|USART6_RX|-|-|-|SDIO_D7|DCMI_D1|-|EVENTOUT|
|Port C|PC8|-|-|TIM3_CH3|TIM8_CH3|-|-|-|-|USART6_CK|-|-|-|SDIO_D0|DCMI_D2|-|EVENTOUT|
|Port C|PC9|MCO2|-|TIM3_CH4|TIM8_CH4|I2C3_SDA|I2S_CKIN|-|-|-|-|-|-|SDIO_D1|DCMI_D3|-|EVENTOUT|
|Port C|PC10|-|-|-|-|-|-|SPI3_SCK/<br>I2S3_CK|USART3_TX/|UART4_TX|-|-|-|SDIO_D2|DCMI_D8|-|EVENTOUT|
|Port C|PC11|-|-|-|-|-|I2S3ext_SD|SPI3_MISO/|USART3_RX|UART4_RX|-|-|-|SDIO_D3|DCMI_D4|-|EVENTOUT|
|Port C|PC12|-|-|-|-|-|-|SPI3_MOSI<br>I2S3_SD|USART3_CK|UART5_TX|-|-|-|SDIO_CK|DCMI_D9|-|EVENTOUT|
|Port C|PC13|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Port C|PC14|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Port C|PC15|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|


**<u>Table 9. Alternate function mapping (continued)</u>**


































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port D|PD0|-|-|-|-|-|-|-|-|-|CAN1_RX|-|-|FSMC_D2|-|-|EVENTOUT|
|Port D|PD1|-|-|-|-|-|-|-|-|-|CAN1_TX|-|-|FSMC_D3|-|-|EVENTOUT|
|Port D|PD2|-|-|TIM3_ETR|-|-|-|-|-|UART5_RX|-|-|-|SDIO_CMD|DCMI_D11|-|EVENTOUT|
|Port D|PD3|-|-|-|-|-|-|-|USART2_CTS|-|-|-|-|FSMC_CLK|-|-|EVENTOUT|
|Port D|PD4|-|-|-|-|-|-|-|USART2_RTS|-|-|-|-|FSMC_NOE|-|-|EVENTOUT|
|Port D|PD5|-|-|-|-|-|-|-|USART2_TX|-|-|-|-|FSMC_NWE|-|-|EVENTOUT|
|Port D|PD6|-|-|-|-|-|-|-|USART2_RX|-|-|-|-|FSMC_NWAIT|-|-|EVENTOUT|
|Port D|PD7|-|-|-|-|-|-|-|USART2_CK|-|-|-|-|FSMC_NE1/<br>FSMC_NCE2|-|-|EVENTOUT|
|Port D|PD8|-|-|-|-|-|-|-|USART3_TX|-|-|-|-|FSMC_D13|-|-|EVENTOUT|
|Port D|PD9|-|-|-|-|-|-|-|USART3_RX|-|-|-|-|FSMC_D14|-|-|EVENTOUT|
|Port D|PD10|-|-|-|-|-|-|-|USART3_CK|-|-|-|-|FSMC_D15|-|-|EVENTOUT|
|Port D|PD11|-|-|-|-|-|-|-|USART3_CTS|-|-|-|-|FSMC_A16|-|-|EVENTOUT|
|Port D|PD12|-|-|TIM4_CH1|-|-|-|-|USART3_RTS|-|-|-|-|FSMC_A17|-|-|EVENTOUT|
|Port D|PD13|-|-|TIM4_CH2|-|-|-|-|-|-|-|-|-|FSMC_A18|-|-|EVENTOUT|
|Port D|PD14|-|-|TIM4_CH3|-|-|-|-|-|-|-|-|-|FSMC_D0|-|-|EVENTOUT|
|Port D|PD15|-|-|TIM4_CH4|-|-|-|-|-|-|-|-|-|FSMC_D1|-|-|EVENTOUT|


**<u>Table 9. Alternate function mapping (continued)</u>**


































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port E|PE0|-|-|TIM4_ETR|-|-|-|-|-|-|-|-|-|FSMC_NBL0|DCMI_D2|-|EVENTOUT|
|Port E|PE1|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_NBL1|DCMI_D3|-|EVENTOUT|
|Port E|PE2|TRACECL<br>K|-|-|-|-|-|-|-|-|-|-|ETH _MII_TXD3|FSMC_A23|-|-|EVENTOUT|
|Port E|PE3|TRACED0|-|-|-|-|-|-|-|-|-|-|-|FSMC_A19|-|-|EVENTOUT|
|Port E|PE4|TRACED1|-|-|-|-|-|-|-|-|-|-|-|FSMC_A20|DCMI_D4|-|EVENTOUT|
|Port E|PE5|TRACED2|-|-|TIM9_CH1|-|-|-|-|-|-|-|-|FSMC_A21|DCMI_D6|-|EVENTOUT|
|Port E|PE6|TRACED3|-|-|TIM9_CH2|-|-|-|-|-|-|-|-|FSMC_A22|DCMI_D7|-|EVENTOUT|
|Port E|PE7|-|TIM1_ETR|-|-|-|-|-|-|-|-|-|-|FSMC_D4|-|-|EVENTOUT|
|Port E|PE8|-|TIM1_CH1N|-|-|-|-|-|-|-|-|-|-|FSMC_D5|-|-|EVENTOUT|
|Port E|PE9|-|TIM1_CH1|-|-|-|-|-|-|-|-|-|-|FSMC_D6|-|-|EVENTOUT|
|Port E|PE10|-|TIM1_CH2N|-|-|-|-|-|-|-|-|-|-|FSMC_D7|-|-|EVENTOUT|
|Port E|PE11|-|TIM1_CH2|-|-|-|-|-|-|-|-|-|-|FSMC_D8|-|-|EVENTOUT|
|Port E|PE12|-|TIM1_CH3N|-|-|-|-|-|-|-|-|-|-|FSMC_D9|-|-|EVENTOUT|
|Port E|PE13|-|TIM1_CH3|-|-|-|-|-|-|-|-|-|-|FSMC_D10|-|-|EVENTOUT|
|Port E|PE14|-|TIM1_CH4|-|-|-|-|-|-|-|-|-|-|FSMC_D11|-|-|EVENTOUT|
|Port E|PE15|-|TIM1_BKIN|-|-|-|-|-|-|-|-|-|-|FSMC_D12|-|-|EVENTOUT|


**<u>Table 9. Alternate function mapping (continued)</u>**


































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port F|PF0|-|-|-|-|I2C2_SDA|-|-|-|-|-|-|-|FSMC_A0|-|-|EVENTOUT|
|Port F|PF1|-|-|-|-|I2C2_SCL|-|-|-|-|-|-|-|FSMC_A1|-|-|EVENTOUT|
|Port F|PF2|-|-|-|-|I2C2_<br>SMBA|-|-|-|-|-|-|-|FSMC_A2|-|-|EVENTOUT|
|Port F|PF3|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A3|-|-|EVENTOUT|
|Port F|PF4|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A4|-|-|EVENTOUT|
|Port F|PF5|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A5|-|-|EVENTOUT|
|Port F|PF6|-|-|-|TIM10_CH1|-|-|-|-|-|-|-|-|FSMC_NIORD|-|-|EVENTOUT|
|Port F|PF7|-|-|-|TIM11_CH1|-|-|-|-|-|-|-|-|FSMC_NREG|-|-|EVENTOUT|
|Port F|PF8|-|-|-|-|-|-|-|-|-|TIM13_CH1|-|-|FSMC_<br>NIOWR|-|-|EVENTOUT|
|Port F|PF9|-|-|-|-|-|-|-|-|-|TIM14_CH1|-|-|FSMC_CD|-|-|EVENTOUT|
|Port F|PF10|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_INTR|-|-|EVENTOUT|
|Port F|PF11|-|-|-|-|-|-|-|-|-|-|-|-||DCMI_D12|-|EVENTOUT|
|Port F|PF12|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A6|-|-|EVENTOUT|
|Port F|PF13|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A7|-|-|EVENTOUT|
|Port F|PF14|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A8|-|-|EVENTOUT|
|Port F|PF15|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A9|-|-|EVENTOUT|


**<u>Table 9. Alternate function mapping (continued)</u>**
















































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port G|PG0|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A10|-|-|EVENTOUT|
|Port G|PG1|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A11|-|-|EVENTOUT|
|Port G|PG2|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A12|-|-|EVENTOUT|
|Port G|PG3|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A13|-|-|EVENTOUT|
|Port G|PG4|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A14|-|-|EVENTOUT|
|Port G|PG5|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_A15|-|-|EVENTOUT|
|Port G|PG6|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_INT2|-|-|EVENTOUT|
|Port G|PG7|-|-|-|-|-|-|-|-|USART6_CK|-|-|-|FSMC_INT3|-|-|EVENTOUT|
|Port G|PG8|-|-|-|-|-|-|-|-|USART6_<br>RTS|-|-|ETH _PPS_OUT|-|-|-|EVENTOUT|
|Port G|PG9|-|-|-|-|-|-|-|-|USART6_RX|-|-|-|FSMC_NE2/<br>FSMC_NCE3|-|-|EVENTOUT|
|Port G|PG10|-|-|-|-|-|-|-|-|-|-|-|-|FSMC_<br>NCE4_1/<br>FSMC_NE3|-|-|EVENTOUT|
|Port G|PG11|-|-|-|-|-|-|-|-|-|-|-|ETH _MII_TX_EN<br>ETH _RMII_<br>TX_EN|FSMC_NCE4_<br>2|-|-|EVENTOUT|
|Port G|PG12|-|-|-|-|-|-|-|-|USART6_<br>RTS|-|-|-|FSMC_NE4|-|-|EVENTOUT|
|Port G|PG13|-|-|-|-|-|-|-|-|UART6_CTS|-|-|ETH _MII_TXD0<br>ETH _RMII_TXD0|FSMC_A24|-|-|EVENTOUT|
|Port G|PG14|-|-|-|-|-|-|-|-|USART6_TX|-|-|ETH _MII_TXD1<br>ETH _RMII_TXD1|FSMC_A25|-|-|EVENTOUT|
|Port G|PG15|-|-|-|-|-|-|-|-|USART6_<br>CTS|-|-|-|-|DCMI_D13|-|EVENTOUT|


**<u>Table 9. Alternate function mapping (continued)</u>**


































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port H|PH0|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENTOUT|
|Port H|PH1|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENTOUT|
|Port H|PH2|-|-|-|-|-|-|-|-|-|-|-|ETH _MII_CRS|-|-|-|EVENTOUT|
|Port H|PH3|-|-|-|-|-|-|-|-|-|-|-|ETH _MII_COL|-|-|-|EVENTOUT|
|Port H|PH4|-|-|-|-|I2C2_SCL|-|-|-|-|-|OTG_HS_ULPI_<br>NXT|-|-|-|-|EVENTOUT|
|Port H|PH5|-|-|-|-|I2C2_SDA|-|-|-|-|-|-|-|-|-|-|EVENTOUT|
|Port H|PH6|-|-|-|-|I2C2_<br>SMBA|-|-|-|-|TIM12_CH1|-|ETH _MII_RXD2|-|-|-|EVENTOUT|
|Port H|PH7|-|-|-|-|I2C3_SCL|-|-|-|-|-|-|ETH _MII_RXD3|-|-|-|EVENTOUT|
|Port H|PH8|-|-|-|-|I2C3_SDA|-|-|-|-|-|-|-|-|DCMI_<br>HSYNC|-|EVENTOUT|
|Port H|PH9|-|-|-|-|I2C3_<br>SMBA|-|-|-|-|TIM12_CH2|-|-|-|DCMI_D0|-|EVENTOUT|
|Port H|PH10|-|-|TIM5_CH1|-|-|-|-|-|-|-|-|-|-|DCMI_D1|-|EVENTOUT|
|Port H|PH11|-|-|TIM5_CH2|-|-|-|-|-|-|-|-|-|-|DCMI_D2|-|EVENTOUT|
|Port H|PH12|-|-|TIM5_CH3|-|-|-|-|-|-|-|-|-|-|DCMI_D3|-|EVENTOUT|
|Port H|PH13|-|-|-|TIM8_CH1N|-|-|-|-|-|CAN1_TX|-|-|-|-|-|EVENTOUT|
|Port H|PH14|-|-|-|TIM8_CH2N|-|-|-|-|-|-|-|-|-|DCMI_D4|-|EVENTOUT|
|Port H|PH15|-|-|-|TIM8_CH3N|-|-|-|-|-|-|-|-|-|DCMI_D11|-|EVENTOUT|


**<u>Table 9. Alternate function mapping (continued)</u>**








































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Port**|**Port**|**SYS**|**TIM1/2**|**TIM3/4/5**|**TIM8/9/10**<br>**/11**|**I2C1/2/3**|**SPI1/SPI2/**<br>**I2S2/I2S2e**<br>**xt**|**SPI3/I2Sext**<br>**/I2S3**|**USART1/2/3/**<br>**I2S3ext**|**UART4/5/**<br>**USART6**|**CAN1/2**<br>**TIM12/13/**<br>**14**|**OTG_FS/**<br>**OTG_HS**|**ETH**|**FSMC/SDIO**<br>**/OTG_FS**|**DCMI**|**DCMI**|**DCMI**|
|Port I|PI0|-|-|TIM5_CH4|-|-|SPI2_NSS<br>I2S2_WS|-|-|-|-|-|-|-|DCMI_D13|-|EVENTOUT|
|Port I|PI1|-|-|-|-|-|SPI2_SCK<br>I2S2_CK|-|-|-|-|-|-|-|DCMI_D8|-|EVENTOUT|
|Port I|PI2|-|-|-|TIM8_CH4|-|SPI2_MISO|I2S2ext_SD|-|-|-|-|-|-|DCMI_D9|-|EVENTOUT|
|Port I|PI3|-|-|-|TIM8_ETR|-|SPI2_MOSI<br>I2S2_SD|-|-|-|-|-|-|-|DCMI_D10|-|EVENTOUT|
|Port I|PI4|-|-|-|TIM8_BKIN|-|-|-|-|-|-|-|-|-|DCMI_D5|-|EVENTOUT|
|Port I|PI5|-|-|-|TIM8_CH1|-|-|-|-|-|-|-|-|-|DCMI_<br>VSYNC|-|EVENTOUT|
|Port I|PI6|-|-|-|TIM8_CH2|-|-|-|-|-|-|-|-|-|DCMI_D6|-|EVENTOUT|
|Port I|PI7|-|-|-|TIM8_CH3|-|-|-|-|-|-|-|-|-|DCMI_D7|-|EVENTOUT|
|Port I|PI8|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Port I|PI9|-|-|-|-|-|-|-|-|-|CAN1_RX|-|-|-|-|-|EVENTOUT|
|Port I|PI10|-|-|-|-|-|-|-|-|-|-|-|ETH _MII_RX_ER|-|-|-|EVENTOUT|
|Port I|PI11|-|-|-|-|-|-|-|-|-|-|OTG_HS_ULPI_<br>DIR|-|-|-|-|EVENTOUT|


**STM32F405xx, STM32F407xx** **Memory mapping**

# **5 Memory mapping**

## The memory map is shown in Figure 18 . **Figure 18. STM32F40xxx memory map**





















































<u>DS8626 Rev 12</u> <u>73/206</u>



191


**Memory mapping** **STM32F405xx, STM32F407xx**

## **Table 10. Register boundary addresses**






|Bus|Boundary address|Peripheral|
|---|---|---|
||0xE00F FFFF - 0xFFFF FFFF|Reserved|
|Cortex-M4|0xE000 0000 - 0xE00F FFFF|Cortex-M4 internal peripherals|
||0xA000 1000 - 0xDFFF FFFF|Reserved|
|AHB3|0xA000 0000 - 0xA000 0FFF|FSMC control register|
|AHB3|0x9000 0000 - 0x9FFF FFFF|FSMC bank 4|
|AHB3|0x8000 0000 - 0x8FFF FFFF|FSMC bank 3|
|AHB3|0x7000 0000 - 0x7FFF FFFF|FSMC bank 2|
|AHB3|0x6000 0000 - 0x6FFF FFFF|FSMC bank 1|
||0x5006 0C00- 0x5FFF FFFF|Reserved|
|AHB2|0x5006 0800 - 0x5006 0BFF|RNG|
|AHB2|0x5005 0400 - 0x5006 07FF|Reserved|
|AHB2|0x5005 0000 - 0x5005 03FF|DCMI|
||0x5004 0000- 0x5004 FFFF|Reserved|
||0x5000 0000 - 0x5003 FFFF|USB OTG FS|
||0x4008 0000- 0x4FFF FFFF|Reserved|



<u>74/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Memory mapping**


**<u>Table 10. Register boundary addresses (continued)</u>**









|Bus|Boundary address|Peripheral|
|---|---|---|
|AHB1|0x4004 0000 - 0x4007 FFFF|USB OTG HS|
|AHB1|0x4002 9400 - 0x4003 FFFF|Reserved|
|AHB1|0x4002 9000 - 0x4002 93FF|ETHERNET MAC|
|AHB1|0x4002 8C00 - 0x4002 8FFF|0x4002 8C00 - 0x4002 8FFF|
|AHB1|0x4002 8800 - 0x4002 8BFF|0x4002 8800 - 0x4002 8BFF|
|AHB1|0x4002 8400 - 0x4002 87FF|0x4002 8400 - 0x4002 87FF|
|AHB1|0x4002 8000 - 0x4002 83FF|0x4002 8000 - 0x4002 83FF|
|AHB1|0x4002 6800 - 0x4002 7FFF|Reserved|
|AHB1|0x4002 6400 - 0x4002 67FF|DMA2|
|AHB1|0x4002 6000 - 0x4002 63FF|DMA1|
|AHB1|0x4002 5000 - 0x4002 5FFF|Reserved|
|AHB1|0x4002 4000 - 0x4002 4FFF|BKPSRAM|
|AHB1|0x4002 3C00 - 0x4002 3FFF|Flash interface register|
|AHB1|0x4002 3800 - 0x4002 3BFF|RCC|
|AHB1|0x4002 3400 - 0x4002 37FF|Reserved|
|AHB1|0x4002 3000 - 0x4002 33FF|CRC|
|AHB1|0x4002 2400 - 0x4002 2FFF|Reserved|
|AHB1|0x4002 2000 - 0x4002 23FF|GPIOI|
|AHB1|0x4002 1C00 - 0x4002 1FFF|GPIOH|
|AHB1|0x4002 1800 - 0x4002 1BFF|GPIOG|
|AHB1|0x4002 1400 - 0x4002 17FF|GPIOF|
|AHB1|0x4002 1000 - 0x4002 13FF|GPIOE|
|AHB1|0x4002 0C00 - 0x4002 0FFF|GPIOD|
|AHB1|0x4002 0800 - 0x4002 0BFF|GPIOC|
|AHB1|0x4002 0400 - 0x4002 07FF|GPIOB|
|AHB1|0x4002 0000 - 0x4002 03FF|GPIOA|
||0x4001 5800- 0x4001 FFFF|Reserved|


<u>DS8626 Rev 12</u> <u>75/206</u>



191


**Memory mapping** **STM32F405xx, STM32F407xx**


**<u>Table 10. Register boundary addresses (continued)</u>**






|Bus|Boundary address|Peripheral|
|---|---|---|
|APB2|0x4001 4C00 - 0x4001 57FF|Reserved|
|APB2|0x4001 4800 - 0x4001 4BFF|TIM11|
|APB2|0x4001 4400 - 0x4001 47FF|TIM10|
|APB2|0x4001 4000 - 0x4001 43FF|TIM9|
|APB2|0x4001 3C00 - 0x4001 3FFF|EXTI|
|APB2|0x4001 3800 - 0x4001 3BFF|SYSCFG|
|APB2|0x4001 3400 - 0x4001 37FF|Reserved|
|APB2|0x4001 3000 - 0x4001 33FF|SPI1|
|APB2|0x4001 2C00 - 0x4001 2FFF|SDIO|
|APB2|0x4001 2400 - 0x4001 2BFF|Reserved|
|APB2|0x4001 2000 - 0x4001 23FF|ADC1 - ADC2 - ADC3|
|APB2|0x4001 1800 - 0x4001 1FFF|Reserved|
|APB2|0x4001 1400 - 0x4001 17FF|USART6|
|APB2|0x4001 1000 - 0x4001 13FF|USART1|
|APB2|0x4001 0800 - 0x4001 0FFF|Reserved|
|APB2|0x4001 0400 - 0x4001 07FF|TIM8|
|APB2|0x4001 0000 - 0x4001 03FF|TIM1|
||0x4000 7800- 0x4000 FFFF|Reserved|



<u>76/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Memory mapping**


**<u>Table 10. Register boundary addresses (continued)</u>**





|Bus|Boundary address|Peripheral|
|---|---|---|
|APB1|0x4000 7800 - 0x4000 7FFF|Reserved|
|APB1|0x4000 7400 - 0x4000 77FF|DAC|
|APB1|0x4000 7000 - 0x4000 73FF|PWR|
|APB1|0x4000 6C00 - 0x4000 6FFF|Reserved|
|APB1|0x4000 6800 - 0x4000 6BFF|CAN2|
|APB1|0x4000 6400 - 0x4000 67FF|CAN1|
|APB1|0x4000 6000 - 0x4000 63FF|Reserved|
|APB1|0x4000 5C00 - 0x4000 5FFF|I2C3|
|APB1|0x4000 5800 - 0x4000 5BFF|I2C2|
|APB1|0x4000 5400 - 0x4000 57FF|I2C1|
|APB1|0x4000 5000 - 0x4000 53FF|UART5|
|APB1|0x4000 4C00 - 0x4000 4FFF|UART4|
|APB1|0x4000 4800 - 0x4000 4BFF|USART3|
|APB1|0x4000 4400 - 0x4000 47FF|USART2|
|APB1|0x4000 4000 - 0x4000 43FF|I2S3ext|
|APB1|0x4000 3C00 - 0x4000 3FFF|SPI3 / I2S3|
|APB1|0x4000 3800 - 0x4000 3BFF|SPI2 / I2S2|
|APB1|0x4000 3400 - 0x4000 37FF|I2S2ext|
|APB1|0x4000 3000 - 0x4000 33FF|IWDG|
|APB1|0x4000 2C00 - 0x4000 2FFF|WWDG|
|APB1|0x4000 2800 - 0x4000 2BFF|RTC & BKP Registers|
|APB1|0x4000 2400 - 0x4000 27FF|Reserved|
|APB1|0x4000 2000 - 0x4000 23FF|TIM14|
|APB1|0x4000 1C00 - 0x4000 1FFF|TIM13|
|APB1|0x4000 1800 - 0x4000 1BFF|TIM12|
|APB1|0x4000 1400 - 0x4000 17FF|TIM7|
|APB1|0x4000 1000 - 0x4000 13FF|TIM6|
|APB1|0x4000 0C00 - 0x4000 0FFF|TIM5|
|APB1|0x4000 0800 - 0x4000 0BFF|TIM4|
|APB1|0x4000 0400 - 0x4000 07FF|TIM3|
|APB1|0x4000 0000 - 0x4000 03FF|TIM2|


<u>DS8626 Rev 12</u> <u>77/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

# **6 Electrical characteristics**

## **6.1 Parameter conditions**


Unless otherwise specified, all voltages are referenced to VSS.

### **6.1.1 Minimum and maximum values**


Unless otherwise specified the minimum and maximum values are evaluated in the worst
conditions of ambient temperature, supply voltage, and frequencies by tests in production
on 100% of the devices with an ambient temperature at TA = 25 °C and TA = TAmax (given
by the selected temperature range).


Data based on characterization results, design simulation and/or technology characteristics
are indicated in the table footnotes and are not tested in production. Based on
characterization, the minimum and maximum values refer to sample tests and represent the
mean value plus or minus three times the standard deviation (mean±3Σ).

### **6.1.2 Typical values**


Unless otherwise specified, typical data are based on TA = 25 °C, VDD = 3.3 V (for the
1.8 V ≤ VDD ≤ 3.6 V voltage range). They are given only as design guidelines and are not
tested.


Typical ADC accuracy values are determined by characterization of a batch of samples from
a standard diffusion lot over the full temperature range, where 95% of the devices have an
error less than or equal to the value indicated (mean±2Σ).

### **6.1.3 Typical curves**


Unless otherwise specified, all typical curves are given only as design guidelines and are
not tested.

### **6.1.4 Loading capacitor**

#### The loading conditions used for pin parameter measurement are shown in Figure 19 .

### **6.1.5 Pin input voltage**

#### The input voltage measurement on a pin of the device is described in Figure 20 .







<u>78/206</u> <u>DS8626 Rev 12</u>






**STM32F405xx, STM32F407xx** **Electrical characteristics**

### **6.1.6 Power supply scheme**

#### **Figure 21. Power supply scheme**



































1. Each power supply pair must be decoupled with filtering ceramic capacitors as shown above. These capacitors must be
placed as close as possible to, or below, the appropriate pins on the underside of the PCB to ensure the good functionality
of the device.

2. To connect BYPASS_REG and PDR_ON pins, refer to _Section 3.16: Voltage regulator_ and _Table 3.15: Power supply_
_supervisor_ .

3. The two 2.2 µF ceramic capacitors should be replaced by two 100 nF decoupling capacitors when the voltage regulator is
OFF.

4. The 4.7 µF ceramic capacitor must be connected to one of the VDD pin.

5. VDDA=VDD and VSSA=VSS.


<u>DS8626 Rev 12</u> <u>79/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

### **6.1.7 Current consumption measurement**

#### **Figure 22. Current consumption measurement scheme**


## **6.2 Absolute maximum ratings**





Stresses above the absolute maximum ratings listed in _Table 11: Voltage characteristics_,
_Table 12: Current characteristics_, and _Table 13: Thermal characteristics_ may cause
permanent damage to the device. These are stress ratings only and functional operation of
the device at these conditions is not implied. Exposure to maximum rating conditions for
extended periods may affect device reliability. Device mission profile (application conditions)
is compliant with JEDEC JESD47 Qualification Standard, extended mission profiles are
available on demand.




















|Col1|Table 11. Voltage characteristics|Col3|Col4|Col5|
|---|---|---|---|---|
|**Symbol**|**Ratings**|**Min**|**Max**|**Unit**|
|VDD–VSS|External main supply voltage (including VDDA, VDD)(1)|–0.3|4.0|V|
|VIN|Input voltage on five-volt tolerant pin(2)|VSS–0.3|VDD+4|VDD+4|
|VIN|Input voltage on any other pin|VSS–0.3|4.0|4.0|
||ΔVDDx||Variations between different VDD power pins|-|50|mV|
||VSSX− VSS||Variations between all the different ground pins<br>including VREF−|-|50|50|
|VESD(HBM)|Electrostatic discharge voltage (human body model)|see_Section 6.3.14:_<br>_Absolute maximum_<br>_ratings (electrical_<br>_sensitivity)_|see_Section 6.3.14:_<br>_Absolute maximum_<br>_ratings (electrical_<br>_sensitivity)_||



1. All main power (VDD, VDDA) and ground (VSS, VSSA) pins must always be connected to the external power
supply, in the permitted range.

2. VIN maximum value must always be respected. Refer to _Table 12_ for the values of the maximum allowed
injected current.


<u>80/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**
























|Col1|Table 12. Current characteristics|Col3|Col4|
|---|---|---|---|
|**Symbol**|**Ratings**|** Max.**|**Unit**|
|IVDD|Total current into VDDpower lines (source)(1)|240|mA|
|IVSS|Total current out of VSSground lines (sink)(1)|240|240|
|IIO|Output current sunk by any I/O and control pin|25|25|
|IIO|Output current source by any I/Os and control pin|25|25|
|IINJ(PIN)<br> (2)|Injected current on five-volt tolerant I/O(3)|–5/+0|–5/+0|
|IINJ(PIN)<br> (2)|Injected current on any other pin(4)|±5|±5|
|ΣIINJ(PIN)<br>(4)|Total injected current (sum of all I/O and control pins)(5)|±25|±25|



1. All main power (VDD, VDDA) and ground (VSS, VSSA) pins must always be connected to the external power
supply, in the permitted range.


2. Negative injection disturbs the analog performance of the device. See note in _Section 6.3.21: 12-bit ADC_
_characteristics_ .

3. Positive injection is not possible on these I/Os. A negative injection is induced by VIN<VSS. IINJ(PIN) must
never be exceeded. Refer to _Table 11_ for the values of the maximum allowed input voltage.

4. A positive injection is induced by VIN>VDD while a negative injection is induced by VIN<VSS. IINJ(PIN) must
never be exceeded. Refer to _Table 11_ for the values of the maximum allowed input voltage.

5. When several inputs are submitted to a current injection, the maximum ΣIINJ(PIN) is the absolute sum of the
positive and negative injected currents (instantaneous values).

### **Table 13. Thermal characteristics**

|Symbol|Ratings|Value|Unit|
|---|---|---|---|
|TSTG|Storage temperature range|–65 to +150|°C|
|TJ|Maximum junction temperature|125|°C|


## **6.3 Operating conditions**

### **6.3.1 General operating conditions**

#### **Table 14. General operating conditions**























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fHCLK|Internal AHB clock frequency|VOS bit in PWR_CR register = 0(1)|0|-|144|MHz|
|fHCLK|Internal AHB clock frequency|VOS bit in PWR_CR register= 1|0|-|168|168|
|fPCLK1|Internal APB1 clock frequency|-|0|-|42|42|
|fPCLK2|Internal APB2 clock frequency|-|0|-|84|84|
|VDD|Standard operating voltage|-|1.8(2)|-|3.6|V|
|VDDA<br>(3)(4)|Analog operating voltage <br>(ADC limited to 1.2 M samples)|Must be the same potential as<br>VDD<br>(5)|1.8(2)|-|2.4|V|
|VDDA<br>(3)(4)|Analog operating voltage <br>(ADC limited to 1.4 M samples)|Analog operating voltage <br>(ADC limited to 1.4 M samples)|2.4|-|3.6|3.6|
|VBAT|Backup operating voltage|-|1.65|-|3.6|V|


<u>DS8626 Rev 12</u> <u>81/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 14. General operating conditions (continued)</u>**




















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V12|Regulator ON:<br>1.2 V internal voltage on<br>VCAP_1/VCAP_2pins|VOS bit in PWR_CR register = 0(1)<br>Max frequency 144MHz|1.08|1.14|1.20|V|
|V12|Regulator ON:<br>1.2 V internal voltage on<br>VCAP_1/VCAP_2pins|VOS bit in PWR_CR register= 1<br>Max frequency 168MHz|1.20|1.26|1.32|V|
|V12|Regulator OFF:<br>1.2 V external voltage must be<br>supplied from external regulator<br>on VCAP_1/VCAP_2pins|Max frequency 144MHz|1.10|1.14|1.20|V|
|V12|Regulator OFF:<br>1.2 V external voltage must be<br>supplied from external regulator<br>on VCAP_1/VCAP_2pins|Max frequency 168MHz|1.20|1.26|1.30|V|
|VIN|Input voltage on RST and FT<br>pins(6)|2 V ≤ VDD ≤ 3.6 V|–0.3|-|5.5|V|
|VIN|Input voltage on RST and FT<br>pins(6)|VDD ≤ 2 V|–0.3|-|5.2|5.2|
|VIN|Input voltage on TTa pins|-|–0.3|-|VDDA+<br>0.3|VDDA+<br>0.3|
|VIN|Input voltage on B pin|-|-|-|5.5|5.5|
|PD|Power dissipation at TA = 85 °C<br>for suffix 6 or TA = 105 °C for<br>suffix 7(7)|LQFP64|-|-|435|mW|
|PD|Power dissipation at TA = 85 °C<br>for suffix 6 or TA = 105 °C for<br>suffix 7(7)|LQFP100|-|-|465|465|
|PD|Power dissipation at TA = 85 °C<br>for suffix 6 or TA = 105 °C for<br>suffix 7(7)|LQFP144|-|-|500|500|
|PD|Power dissipation at TA = 85 °C<br>for suffix 6 or TA = 105 °C for<br>suffix 7(7)|LQFP176|-|-|526|526|
|PD|Power dissipation at TA = 85 °C<br>for suffix 6 or TA = 105 °C for<br>suffix 7(7)|UFBGA176|-|-|513|513|
|PD|Power dissipation at TA = 85 °C<br>for suffix 6 or TA = 105 °C for<br>suffix 7(7)|WLCSP90|-|-|543|543|
|TA|Ambient temperature for 6 suffix<br>version|Maximum power dissipation|–40|-|85|°C|
|TA|Ambient temperature for 6 suffix<br>version|Low-power dissipation(8)|–40|-|105|105|
|TA|Ambient temperature for 7 suffix<br>version|Maximum power dissipation|–40|-|105|°C|
|TA|Ambient temperature for 7 suffix<br>version|Low-power dissipation(8)|–40|-|125|125|
|TJ|Junction temperature range|6 suffix version|–40|-|105|°C|
|TJ|Junction temperature range|7 suffix version|–40|-|125|125|



1. The average expected gain in power consumption when VOS = 0 compared to VOS = 1 is around 10% for the whole
temperature range, when the system clock frequency is between 30 and 144 MHz.

2. VDD/VDDA minimum value of 1.7 V is obtained when the device operates in reduced temperature range, and with the use of
an external power supply supervisor (refer to _Section 3.15.2: Internal reset OFF_ ).


3. When the ADC is used, refer to _Table 67: ADC characteristics_ .

4. If VREF+ pin is present, it must respect the following condition: VDDA-VREF+ < 1.2 V.

5. It is recommended to power VDD and VDDA from the same source. A maximum difference of 300 mV between VDD and
VDDA can be tolerated during power-up and power-down operation.

6. To sustain a voltage higher than VDD+0.3, the internal pull-up and pull-down resistors must be disabled.

7. If TA is lower, higher PD values are allowed as long as TJ does not exceed TJmax.

8. In low-power dissipation state, TA can be extended to this range as long as TJ does not exceed TJmax.


<u>82/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 15. Limitations depending on the operating power supply range**


































|Operating<br>power<br>supply<br>range|ADC<br>operation|Maximum<br>flash memory<br>access<br>frequency<br>with no wait<br>state<br>(f )<br>Flashmax|Maximum flash<br>memory access<br>frequency<br>with wait<br>states(1) (2)|I/O operation|Clock output<br>Frequency on<br>I/O pins|Possible<br>flash<br>memory<br>operations|
|---|---|---|---|---|---|---|
|VDD =1.8 to<br>2.1 V(3)|Conversion<br>time up to<br>1.2 Msps|20 MHz(4)|160 MHz with 7<br>wait states|– Degraded<br>speed<br>performance<br>– No I/O<br>compensation|up to 30 MHz|8-bit erase<br>and program<br>operations<br>only|
|VDD = 2.1 to<br>2.4 V|Conversion<br>time up to<br>1.2 Msps|22 MHz|168 MHz with 7<br>wait states|– Degraded<br>speed<br>performance<br>– No I/O<br>compensation|up to 30 MHz|16-bit erase<br>and program<br>operations|
|VDD = 2.4 to<br>2.7 V|Conversion<br>time up to<br>2.4 Msps|24 MHz|168 MHz with 6<br>wait states|– Degraded<br>speed<br>performance<br>– I/O<br>compensation<br>works|up to 48 MHz|16-bit erase<br>and program<br>operations|
|VDD = 2.7 to<br>3.6 V(5)|Conversion<br>time up to<br>2.4 Msps|30 MHz|168 MHz with 5<br>wait states|– Full-speed<br>operation<br>– I/O<br>compensation<br>works|– up to<br>60 MHz<br>when VDD =<br>3.0 to 3.6 V<br>– up to<br>48 MHz<br>when VDD =<br>2.7 to 3.0 V|32-bit erase<br>and program<br>operations|



1. It applies only when code executed from flash memory access, when code executed from RAM, no wait state is required.


2. Thanks to the ART accelerator and the 128-bit flash memory, the number of wait states given here does not impact the
execution speed from flash memory since the ART accelerator allows to achieve a performance equivalent to 0 wait state
program execution.

3. VDD/VDDA minimum value of 1.7 V is obtained when the device operates in reduced temperature range, and with the use
of an external power supply supervisor (refer to _Section 3.15.2: Internal reset OFF_ ).


4. Prefetch is not available. Refer to AN3430 application note for details on how to adjust performance and power.


5. The voltage range for OTG USB FS can drop down to 2.7 V. However it is degraded between 2.7 and 3 V.


<u>DS8626 Rev 12</u> <u>83/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

### **6.3.2 VCAP_1/VCAP_2 external capacitor**


Stabilization for the main regulator is achieved by connecting an external capacitor CEXT to
#### the VCAP_1/VCAP_2 pins. CEXT is specified in Table 16 .


1. Legend: ESR is the equivalent series resistance.

#### **Table 16. VCAP_1/VCAP_2 operating conditions (1)**

|Symbol|Parameter|Conditions|
|---|---|---|
|CEXT|Capacitance of external capacitor|2.2 µF|
|ESR|ESR of external capacitor|< 2Ω|



1. When bypassing the voltage regulator, the two 2.2 µF VCAP capacitors are not required and should be
replaced by two 100 nF decoupling capacitors.

### **6.3.3 Operating conditions at power-up / power-down (regulator ON)**


Subject to general operating conditions for TA.

#### **Table 17. Operating conditions at power-up / power-down (regulator ON)**






|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tVDD|VDD rise time rate|20|∞|µs/V|
|tVDD|VDD fall time rate|20|∞|∞|


### **6.3.4 Operating conditions at power-up / power-down (regulator OFF)**

Subject to general operating conditions for TA.

#### **Table 18. Operating conditions at power-up / power-down (regulator OFF) (1)**








|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|tVDD|VDD rise time rate|Power-up|20|∞|µs/V|
|tVDD|VDD fall time rate|Power-down|20|∞|∞|
|tVCAP|VCAP_1 and VCAP_2rise time<br>rate|Power-up|20|∞|∞|
|tVCAP|VCAP_1 and VCAP_2 fall time<br>rate|Power-down|20|∞|∞|



1. To reset the internal logic at power-down, a reset must be applied on pin PA0 when VDD reach below
minimum value of V12.


<u>84/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

### **6.3.5 Embedded reset and power control block characteristics**

#### The parameters given in Table 19 are derived from tests performed under ambient

temperature and VDD supply voltage conditions summarized in _Table 14_ .

#### **Table 19. Embedded reset and power control block characteristics**
























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=000 (rising<br>edge)|2.09|2.14|2.19|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=000 (falling<br>edge)|1.98|2.04|2.08|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=001 (rising<br>edge)|2.23|2.30|2.37|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=001 (falling<br>edge)|2.13|2.19|2.25|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=010 (rising<br>edge)|2.39|2.45|2.51|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=010 (falling<br>edge)|2.29|2.35|2.39|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=011 (rising edge)|2.54|2.60|2.65|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=011 (falling<br>edge)|2.44|2.51|2.56|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=100 (rising<br>edge)|2.70|2.76|2.82|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=100 (falling<br>edge)|2.59|2.66|2.71|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=101 (rising<br>edge)|2.86|2.93|2.99|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=101 (falling<br>edge)|2.75|2.84|2.92|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=110 (rising edge)|2.96|3.03|3.10|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=110 (falling<br>edge)|2.85|2.93|2.99|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=111 (rising edge)|3.07|3.14|3.21|V|
|VPVD|Programmable voltage<br>detector level selection|PLS[2:0]=111 (falling<br>edge)|2.95|3.03|3.09|V|
|VPVDhyst<br>(1)|PVD hysteresis|-|-|100|-|mV|
|VPOR/PDR|Power-on/power-down<br>reset threshold|Falling edge|1.60|1.68|1.76|V|
|VPOR/PDR|Power-on/power-down<br>reset threshold|Rising edge|1.64|1.72|1.80|V|
|VPDRhyst<br>(1)|PDR hysteresis|-|-|40|-|mV|
|VBOR1|Brownout level 1<br>threshold|Falling edge|2.13|2.19|2.24|V|
|VBOR1|Brownout level 1<br>threshold|Rising edge|2.23|2.29|2.33|V|



<u>DS8626 Rev 12</u> <u>85/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 19. Embedded reset and power control block characteristics (continued)</u>**




















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VBOR2|Brownout level 2<br>threshold|Falling edge|2.44|2.50|2.56|V|
|VBOR2|Brownout level 2<br>threshold|Rising edge|2.53|2.59|2.63|V|
|VBOR3|Brownout level 3<br>threshold|Falling edge|2.75|2.83|2.88|V|
|VBOR3|Brownout level 3<br>threshold|Rising edge|2.85|2.92|2.97|V|
|VBORhyst<br>(1)<br>|BOR hysteresis<br>|-|-|100|-|mV|
|TRSTTEMPO<br>(1)(2)|Reset temporization|-|0.5|1.5|3.0|ms|
|IRUSH<br>(1)|InRush current on<br>voltage regulator<br>power-on (POR or<br>wakeup from Standby)|-|-|160|200|mA|
|ERUSH<br>(1)|InRush energy on<br>voltage regulator<br>power-on (POR or<br>wakeup from Standby)|VDD = 1.8 V, TA = 105 °C,<br>IRUSH= 171 mA for 31 µs|-|-|5.4|µC|



1. Specified by design.

2. The reset temporization is measured from the power-on (POR reset or wakeup from VBAT) to the instant
when first instruction is read by the user application code.

### **6.3.6 Supply current characteristics**


The current consumption is a function of several parameters and factors such as the
operating voltage, ambient temperature, I/O pin loading, device software configuration,
operating frequencies, I/O pin switching rate, program location in memory and executed
binary code.
The current consumption is measured as described in _Figure 22: Current consumption_
_measurement scheme_ .


All Run mode current consumption measurements given in this section are performed using
a CoreMark-compliant code.


**Typical and maximum current consumption**


The MCU is placed under the following conditions:

      - At startup, all I/O pins are configured as analog inputs by firmware.

      - All peripherals are disabled except if it is explicitly mentioned.

      - The flash memory access time is adjusted to fHCLK frequency (0 wait state from 0 to
30 MHz, 1 wait state from 30 to 60 MHz, 2 wait states from 60 to 90 MHz, 3 wait states
from 90 to 120 MHz, 4 wait states from 120 to 150 MHz, and 5 wait states from 150 to
168 MHz).

      - When the peripherals are enabled HCLK is the system clock, fPCLK1 = fHCLK/4, and
fPCLK2 = fHCLK/2, except is explicitly mentioned.

      - The maximum values are obtained for VDD = 3.6 V and maximum ambient temperature
(TA), and the typical values for TA= 25 °C and VDD = 3.3 V unless otherwise specified.


<u>86/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 20. Typical and maximum current consumption in Run mode, code with data processing**

**<u>running from flash memory (ART accelerator enabled) or RAM</u>** <sup>**(1)**</sup>
















|Symbol|Parameter|Conditions|f<br>HCLK|Typ|Max(2)|Col7|Unit|
|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**fHCLK**|**TA =**<br>**25 °C**|**TA =**<br>**85 °C**|**TA =**<br>**105 °C**|**TA =**<br>**105 °C**|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|168 MHz|87|102|109|mA|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|144 MHz|67|80|86|86|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|120 MHz|56|69|75|75|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|90 MHz|44|56|62|62|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|60 MHz|30|42|49|49|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|30 MHz|16|28|35|35|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|25 MHz|12|24|31|31|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|16 MHz(6)|9|20|28|28|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|8 MHz|5|17|24|24|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|4 MHz|3|15|22|22|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals enabled(4)(5)|2 MHz|2|14|21|21|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|168 MHz|40|54|61|61|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|144 MHz|31|43|50|50|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|120 MHz|26|38|45|45|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|90 MHz|20|32|39|39|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|60 MHz|14|26|33|33|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|30 MHz|8|20|27|27|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|25 MHz|6|18|25|25|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|16 MHz(6)|5|16|24|24|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|8 MHz|3|15|22|22|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|4 MHz|2|14|21|21|
|IDD|Supply current in<br>Run mode|External clock(3), all<br>peripherals disabled(4)(5)|2 MHz|2|14|21|21|



1. Code and data processing running from SRAM1 using boot pins.

2. Evaluated by characterization, tested in production at VDD max and fHCLK max with peripherals enabled.

3. External clock is 4 MHz and PLL is on when fHCLK > 25 MHz.

4. When the ADC is ON (ADON bit set in the ADC_CR2 register), add an additional power consumption of 1.6 mA per ADC for
the analog part.


5. When analog peripheral blocks such as ADCs, DACs, HSE, LSE, HSI, or LSI are ON, an additional power consumption
should be considered.


6. In this case HCLK = system clock/2.


<u>DS8626 Rev 12</u> <u>87/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Table 21. Typical and maximum current consumption in Run mode, code with data processing**

**<u>running from flash memory (ART accelerator disabled)</u>**
















|Symbol|Parameter|Conditions|f<br>HCLK|Typ|Max(1)|Col7|Unit|
|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**fHCLK**|**TA = 25 °C **|**TA = 85 °C **|**TA = 105 °C**|**TA = 105 °C**|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|168 MHz|93|109|117|mA|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|144 MHz|76|89|96|96|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|120 MHz|67|79|86|86|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|90 MHz|53|65|73|73|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|60 MHz|37|49|56|56|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|30 MHz|20|32|39|39|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|25 MHz|16|27|35|35|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|16 MHz|11|23|30|30|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|8 MHz|6|18|25|25|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|4 MHz|4|16|23|23|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>enabled(3)(4)|2 MHz|3|15|22|22|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|168 MHz|46|61|69|69|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|144 MHz|40|52|60|60|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|120 MHz|37|48|56|56|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|90 MHz|30|42|50|50|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|60 MHz|22|33|41|41|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|30 MHz|12|24|31|31|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|25 MHz|10|21|29|29|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|16 MHz|7|19|26|26|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|8 MHz|4|16|23|23|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|4 MHz|3|15|22|22|
|IDD|Supply current<br>in Run mode|External clock(2),  <br>all peripherals<br>disabled(3)(4)|2 MHz|2|14|21|21|



1. Evaluated by characterization, tested in production at VDD max and fHCLK max with peripherals enabled.

2. External clock is 4 MHz and PLL is on when fHCLK > 25 MHz.

3. When analog peripheral blocks such as (ADCs, DACs, HSE, LSE, HSI,LSI) are on, an additional power consumption
should be considered.


4. When the ADC is ON (ADON bit set in the ADC_CR2 register), add an additional power consumption of 1.6 mA per ADC
for the analog part.


<u>88/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 24. Typical current consumption versus temperature, Run mode, code with data**

**<u>processing running from flash (ART accelerator ON) or RAM, and peripherals OFF</u>**








#### **Figure 25. Typical current consumption versus temperature, Run mode, code with data**

**<u>processing running from flash (ART accelerator ON) or RAM, and peripherals ON</u>**









<u>DS8626 Rev 12</u> <u>89/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 26. Typical current consumption versus temperature, Run mode, code with data**

**<u>processing running from flash (ART accelerator OFF) or RAM, and peripherals OFF</u>**








#### **Figure 27. Typical current consumption versus temperature, Run mode, code with data**

**<u>processing running from flash (ART accelerator OFF) or RAM, and peripherals ON</u>**













<u>90/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 22. Typical and maximum current consumption in Sleep mode**
















|Symbol|Parameter|Conditions|f<br>HCLK|Typ|Max(1)|Col7|Unit|
|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**fHCLK**|**TA =**<br>**25 °C**|**TA =**<br>**85 °C**|**TA =**<br>**105 °C**|**TA =**<br>**105 °C**|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|168 MHz|59|77|84|mA|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|144 MHz|46|61|67|67|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|120 MHz|38|53|60|60|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|90 MHz|30|44|51|51|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|60 MHz|20|34|41|41|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|30 MHz|11|24|31|31|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|25 MHz|8|21|28|28|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|16 MHz|6|18|25|25|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|8 MHz|3|16|23|23|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|4 MHz|2|15|22|22|
|IDD|Supply current in<br>Sleep mode|External clock(2),  <br>all peripherals enabled(3)|2 MHz|2|14|21|21|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|168 MHz|12|27|35|35|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|144 MHz|9|22|29|29|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|120 MHz|8|20|28|28|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|90 MHz|7|19|26|26|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|60 MHz|5|17|24|24|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|30 MHz|3|16|23|23|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|25 MHz|2|15|22|22|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|16 MHz|2|14|21|21|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|8 MHz|1|14|21|21|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|4 MHz|1|13|21|21|
|IDD|Supply current in<br>Sleep mode|External clock(2), all<br>peripherals disabled|2 MHz|1|13|21|21|



1. Evaluated by characterization, tested in production at VDD max and fHCLK max with peripherals enabled.

2. External clock is 4 MHz and PLL is on when fHCLK > 25 MHz.

3. Add an additional power consumption of 1.6 mA per ADC for the analog part. In applications, this consumption occurs only
while the ADC is ON (ADON bit is set in the ADC_CR2 register).


<u>DS8626 Rev 12</u> <u>91/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Table 23. Typical and maximum current consumptions in Stop mode**












|Symbol|Parameter|Conditions|Typ|Max|Col6|Col7|Unit|
|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**TA =**<br>**25 °C**|**TA =**<br>**25 °C**|**TA =**<br>**85 °C**|**TA =**<br>**105 °C**|**TA =**<br>**105 °C**|
|IDD_STOP|Supply<br>current in<br>Stop mode<br>with main<br>regulator in<br>Run mode|Flash in Stop mode, low-speed and high-<br>speed internal RC oscillators and high-speed<br>oscillator OFF (no independent watchdog)|0.45|1.5|11.00|20.00|mA|
|IDD_STOP|Supply<br>current in<br>Stop mode<br>with main<br>regulator in<br>Run mode|Flash in Deep power-down mode, low-speed<br>and high-speed internal RC oscillators and<br>high-speed oscillator OFF (no independent<br>watchdog)|0.40|1.5|11.00|20.00|20.00|
|IDD_STOP|Supply<br>current in<br>Stop mode<br>with main<br>regulator in<br>Low-power<br>mode|Flash in Stop mode, low-speed and high-<br>speed internal RC oscillators and high-speed<br>oscillator OFF (no independent watchdog)|0.31|1.1|8.00|15.00|15.00|
|IDD_STOP|Supply<br>current in<br>Stop mode<br>with main<br>regulator in<br>Low-power<br>mode|Flash in Deep power-down mode, low-speed<br>and high-speed internal RC oscillators and<br>high-speed oscillator OFF (no independent<br>watchdog)|0.28|1.1|8.00|15.00|15.00|


#### **Table 24. Typical and maximum current consumptions in Standby mode**




















|Symbol|Parameter|Conditions|Typ|Col5|Col6|Max(1)|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**TA = 25 °C**|**TA = 25 °C**|**TA = 25 °C**|**TA =**<br>**85 °C**|**TA =**<br>**105 °C**|**TA =**<br>**105 °C**|
|**Symbol**|**Parameter**|**Conditions**|**VDD =**<br>**1.8 V**|**VDD= **<br>**2.4 V**|**VDD =**<br>**3.3 V**|**VDD = 3.6 V**|**VDD = 3.6 V**|**VDD = 3.6 V**|
|IDD_STBY|Supply current<br>in Standby<br>mode|Backup SRAM ON, low-<br>speed oscillator and RTC ON|3.0|3.4|4.0|20|36|µA|
|IDD_STBY|Supply current<br>in Standby<br>mode|Backup SRAM OFF, low-<br>speed oscillator and RTC ON|2.4|2.7|3.3|16|32|32|
|IDD_STBY|Supply current<br>in Standby<br>mode|Backup SRAM ON, RTC<br>OFF|2.4|2.6|3.0|12.5|24.8|24.8|
|IDD_STBY|Supply current<br>in Standby<br>mode|Backup SRAM OFF, RTC<br>OFF|1.7|1.9|2.2|9.8|19.2|19.2|



1. Evaluated by characterization - not tested in production.


<u>92/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


















|Col1|Table 2|25. Typical and maximum cu|urrent consumptions in|Col5|Col6|n VBAT mode|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Typ**|**Typ**|**Typ**|**Max(1)**|**Max(1)**|**Unit**|
|**Symbol**|**Parameter**|**Conditions**|**TA = 25 °C**|**TA = 25 °C**|**TA = 25 °C**|**TA =**<br>**85 °C**|**TA =**<br>**105 °C**|**TA =**<br>**105 °C**|
|**Symbol**|**Parameter**|**Conditions**|**VBAT **<br>**= **<br>**1.8 V**|**VBAT= **<br>**2.4 V**|**VBAT **<br>**= **<br>**3.3 V**|**VBAT = 3.6 V**|**VBAT = 3.6 V**|**VBAT = 3.6 V**|
|IDD_VBA<br>T|Backup<br>domain<br>supply<br>current|Backup SRAM ON, low-speed<br>oscillator and RTC ON|1.29|1.42|1.68|6|11|µA|
|IDD_VBA<br>T|Backup<br>domain<br>supply<br>current|Backup SRAM OFF, low-speed<br>oscillator and RTC ON|0.62|0.73|0.96|3|5|5|
|IDD_VBA<br>T|Backup<br>domain<br>supply<br>current|Backup SRAM ON, RTC OFF|0.79|0.81|0.86|5|10|10|
|IDD_VBA<br>T|Backup<br>domain<br>supply<br>current|Backup SRAM OFF, RTC OFF|0.10|0.10|0.10|2|4|4|



1. Evaluated by characterization - not tested in production.







<u>DS8626 Rev 12</u> <u>93/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**









**Additional current consumption**


The MCU is placed under the following conditions:

      - All I/O pins are configured in analog mode.

      - The flash memory access time is adjusted to fHCLK frequency.

      - The voltage scaling is adjusted to fHCLK frequency as follows:

       - Scale 2 for fHCLK ≤ 144 MHz

       - Scale 1 for 144 MHz < fHCLK ≤ 168 MHz.

      - The system clock is HCLK, fPCLK1 = fHCLK/4, and fPCLK2 = fHCLK/2.

      - The HSE crystal clock frequency is 25 MHz.

      - TA= 25 °C.


<u>94/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 26. Typical current consumption in Run mode, code with data processing**

**running from flash memory, regulator ON (ART accelerator enabled**










|Col1|exce|ept prefetch), VDD|D = 1.8 V(1)|Col5|Col6|
|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**fHCLK (MHz)**|**Typ. at TA =**<br>**25 °C**|**Unit**|
|IDD|Supply current in<br>Run mode|All peripheral<br>disabled|160|36.2|mA|
|IDD|Supply current in<br>Run mode|All peripheral<br>disabled|144|29.3|29.3|
|IDD|Supply current in<br>Run mode|All peripheral<br>disabled|120|24.7|24.7|
|IDD|Supply current in<br>Run mode|All peripheral<br>disabled|90|19.3|19.3|
|IDD|Supply current in<br>Run mode|All peripheral<br>disabled|60|13.4|13.4|
|IDD|Supply current in<br>Run mode|All peripheral<br>disabled|30|7.7|7.7|
|IDD|Supply current in<br>Run mode|All peripheral<br>disabled|25|6.0|6.0|



1. When peripherals are enabled, the power consumption corresponding to the analog part of the peripherals
(such as ADC or DAC) is not included.


**I/O system current consumption**


The current consumption of the I/O system has two components: static and dynamic.


I/O static current consumption


All the I/Os used as input with pull-up or pull-down generate current consumption when the
pin is externally held to the opposite level. The value of this current consumption can be
simply computed by using the pull-up/pull-down resistors values given in _Table 48: I/O static_
_characteristics_ .


For the output pins, any internal or external pull-up or pull-down and external load must also
be considered to estimate the current consumption.


Additional I/O current consumption is due to I/Os configured as inputs if an intermediate
voltage level is externally applied. This current consumption is caused by the input Schmitt
trigger circuits used to discriminate the input value. Unless this specific configuration is
required by the application, this supply current consumption can be avoided by configuring
these I/Os in analog mode. This is notably the case of ADC input pins which should be
configured as analog inputs.


**Caution:** Any floating input pin can also settle to an intermediate voltage level or switch inadvertently,
as a result of external electromagnetic noise. To avoid current consumption related to
floating pins, they must either be configured in analog mode, or forced internally to a definite
digital value. This can be done either by using pull-up/down resistors or by configuring the
pins in output mode.


I/O dynamic current consumption


In addition to the internal peripheral current consumption measured previously (see
_Table 28: Peripheral current consumption_ ), the I/Os used by an application also contribute
to the current consumption. When an I/O pin switches, it uses the current from the MCU
supply voltage to supply the I/O pin circuitry and to charge/discharge the capacitive load
internal and external connected to the pin:


ISW = VDD × fSW × C


<u>DS8626 Rev 12</u> <u>95/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


where

ISW is the current sunk by a switching I/O to charge/discharge the capacitive load

VDD is the MCU supply voltage

fSW is the I/O switching frequency

C is the total capacitance seen by the I/O pin: C = CINT+ CEXT

The test pin is configured in push-pull output mode and is toggled by software at a fixed
frequency.


<u>96/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 27. Switching output I/O current consumption**












|Symbol|Parameter|Conditions(1)|I/O toggling<br>frequency (f )<br>SW|Typ|Unit|
|---|---|---|---|---|---|
|IDDIO|I/O switching<br>current|VDD = 3.3 V(2)<br>C = CINT|2 MHz|0.02|mA|
|IDDIO|I/O switching<br>current|VDD = 3.3 V(2)<br>C = CINT|8 MHz|0.14|0.14|
|IDDIO|I/O switching<br>current|VDD = 3.3 V(2)<br>C = CINT|25 MHz|0.51|0.51|
|IDDIO|I/O switching<br>current|VDD = 3.3 V(2)<br>C = CINT|50 MHz|0.86|0.86|
|IDDIO|I/O switching<br>current|VDD = 3.3 V(2)<br>C = CINT|60 MHz|1.30|1.30|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 0 pF<br>C = CINT + CEXT+ CS|2 MHz|0.10|0.10|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 0 pF<br>C = CINT + CEXT+ CS|8 MHz|0.38|0.38|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 0 pF<br>C = CINT + CEXT+ CS|25 MHz|1.18|1.18|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 0 pF<br>C = CINT + CEXT+ CS|50 MHz|2.47|2.47|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 0 pF<br>C = CINT + CEXT+ CS|60 MHz|2.86|2.86|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 10 pF<br>C = CINT + CEXT+ CS|2 MHz|0.17|0.17|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 10 pF<br>C = CINT + CEXT+ CS|8 MHz|0.66|0.66|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 10 pF<br>C = CINT + CEXT+ CS|25 MHz|1.70|1.70|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 10 pF<br>C = CINT + CEXT+ CS|50 MHz|2.65|2.65|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 10 pF<br>C = CINT + CEXT+ CS|60 MHz|3.48|3.48|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 22 pF<br>C = CINT + CEXT+ CS|2 MHz|0.23|0.23|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 22 pF<br>C = CINT + CEXT+ CS|8 MHz|0.95|0.95|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 22 pF<br>C = CINT + CEXT+ CS|25 MHz|3.20|3.20|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 22 pF<br>C = CINT + CEXT+ CS|50 MHz|4.69|4.69|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 22 pF<br>C = CINT + CEXT+ CS|60 MHz|8.06|8.06|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 33 pF<br>C = CINT + CEXT+ CS|2 MHz|0.30|0.30|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 33 pF<br>C = CINT + CEXT+ CS|8 MHz|1.22|1.22|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 33 pF<br>C = CINT + CEXT+ CS|25 MHz|3.90|3.90|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 33 pF<br>C = CINT + CEXT+ CS|50 MHz|8.82|8.82|
|IDDIO|I/O switching<br>current|VDD = 3.3 V<br>CEXT = 33 pF<br>C = CINT + CEXT+ CS|60 MHz|-(3)|-(3)|



1. CS is the PCB board capacitance including the pad pin. CS = 7 pF (estimated value).

2. This test is performed by cutting the LQFP package pin (pad removal).


3. At 60 MHz, C maximum load is specified 30 pF.


<u>DS8626 Rev 12</u> <u>97/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**On-chip peripheral current consumption**

#### The current consumption of the on-chip peripherals is given in Table 28 . The MCU is placed

under the following conditions:

      - At startup, all I/O pins are configured as analog pins by firmware.

      - All peripherals are disabled unless otherwise mentioned

      - The code is running from flash memory and the flash memory access time is equal to 5
wait states at 168 MHz.

      - The code is running from flash memory and the flash memory access time is equal to 4
wait states at 144 MHz, and the power scale mode is set to 2.

      - The ART accelerator is ON.

      - The given value is calculated by measuring the difference of current consumption

       - with all peripherals clocked off

       - with one peripheral clocked on (with only the clock applied)

      - When the peripherals are enabled: HCLK is the system clock, fPCLK1 = fHCLK/4, and
fPCLK2 = fHCLK/2.

      - The typical values are obtained for VDD = 3.3 V and TA= 25 °C, unless otherwise
specified.

#### **Table 28. Peripheral current consumption**

















|Peripheral|Col2|I (Typ)(1)<br>DD|Col4|Unit|
|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**Scale1**<br>**(up t 168 MHz)**|**Scale2**<br>**(up to 144 MHz)**|**Scale2**<br>**(up to 144 MHz)**|
|AHB1<br>(up to 168 MHz)|GPIOA|2.70|2.40|µA/MHz|
|AHB1<br>(up to 168 MHz)|GPIOB|2.50|2.22|2.22|
|AHB1<br>(up to 168 MHz)|GPIOC|2.54|2.28|2.28|
|AHB1<br>(up to 168 MHz)|GPIOD|2.55|2.28|2.28|
|AHB1<br>(up to 168 MHz)|GPIOE|2.68|2.40|2.40|
|AHB1<br>(up to 168 MHz)|GPIOF|2.53|2.28|2.28|
|AHB1<br>(up to 168 MHz)|GPIOG|2.51|2.22|2.22|
|AHB1<br>(up to 168 MHz)|GPIOH|2.51|2.22|2.22|
|AHB1<br>(up to 168 MHz)|GPIOI|2.50|2.22|2.22|
|AHB1<br>(up to 168 MHz)|OTG_HS+ULPI|28.33|25.38|25.38|
|AHB1<br>(up to 168 MHz)|CRC|0.41|0.40|0.40|
|AHB1<br>(up to 168 MHz)|BKPSRAM|0.63|0.58|0.58|
|AHB1<br>(up to 168 MHz)|DMA1|37.44|33.58|33.58|
|AHB1<br>(up to 168 MHz)|DMA2|37.69|33.93|33.93|
|AHB1<br>(up to 168 MHz)|ETH_MAC<br>ETH_MAC_TX<br>ETH_MAC_RX<br>ETH_MAC_PTP|20.43|18.39|18.39|


<u>98/206</u> <u>DS8626 Rev 12</u>




**STM32F405xx, STM32F407xx** **Electrical characteristics**


**<u>Table 28. Peripheral current consumption (continued)</u>**




















|Peripheral|Col2|I (Typ)(1)<br>DD|Col4|Unit|
|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**Scale1**<br>**(up t 168 MHz)**|**Scale2**<br>**(up to 144 MHz)**|**Scale2**<br>**(up to 144 MHz)**|
|AHB2<br>(up to 168 MHz)|OTG_FS|26.45|26.67|µA/MHz|
|AHB2<br>(up to 168 MHz)|DCMI|5.87|5.35|5.35|
|AHB2<br>(up to 168 MHz)|RNG|1.50|1.67|1.67|
|AHB3<br>(up to 168 MHz)|FSMC|12.46|11.31|µA/MHz|
|Bus matrix(2)|Bus matrix(2)|13.10|11.81|µA/MHz|
|APB1<br>(up to 42 MHz)|TIM2|16.71|16.50|µA/MHz|
|APB1<br>(up to 42 MHz)|TIM3|12.33|11.94|11.94|
|APB1<br>(up to 42 MHz)|TIM4|13.45|12.92|12.92|
|APB1<br>(up to 42 MHz)|TIM5|17.14|16.58|16.58|
|APB1<br>(up to 42 MHz)|TIM6|2.43|3.06|3.06|
|APB1<br>(up to 42 MHz)|TIM7|2.43|2.22|2.22|
|APB1<br>(up to 42 MHz)|TIM12|6.62|6.83|6.83|
|APB1<br>(up to 42 MHz)|TIM13|5.05|5.47|5.47|
|APB1<br>(up to 42 MHz)|TIM14|5.26|5.61|5.61|
|APB1<br>(up to 42 MHz)|PWR|1.00|0.56|0.56|
|APB1<br>(up to 42 MHz)|USART2|2.69|2.78|2.78|
|APB1<br>(up to 42 MHz)|USART3|2.74|2.78|2.78|
|APB1<br>(up to 42 MHz)|UART4|3.24|3.33|3.33|
|APB1<br>(up to 42 MHz)|UART5|2.69|2.78|2.78|
|APB1<br>(up to 42 MHz)|I2C1|2.67|2.50|2.50|
|APB1<br>(up to 42 MHz)|I2C2|2.83|2.78|2.78|
|APB1<br>(up to 42 MHz)|I2C3|2.81|2.78|2.78|
|APB1<br>(up to 42 MHz)|SPI2|2.43|2.22|2.22|
|APB1<br>(up to 42 MHz)|SPI3|2.43|2.22|2.22|
|APB1<br>(up to 42 MHz)|I2S2(3)|2.43|2.22|2.22|
|APB1<br>(up to 42 MHz)|I2S3(3)|2.26|2.22|2.22|
|APB1<br>(up to 42 MHz)|CAN1|5.12|5.56|5.56|
|APB1<br>(up to 42 MHz)|CAN2|4.81|5.28|5.28|
|APB1<br>(up to 42 MHz)|DAC(4)|1.67|1.67|1.67|
|APB1<br>(up to 42 MHz)|WWDG|1.00|0.83|0.83|



<u>DS8626 Rev 12</u> <u>99/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 28. Peripheral current consumption (continued)</u>**














|Peripheral|Col2|I (Typ)(1)<br>DD|Col4|Unit|
|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**Scale1**<br>**(up t 168 MHz)**|**Scale2**<br>**(up to 144 MHz)**|**Scale2**<br>**(up to 144 MHz)**|
|APB2<br>(up to 84 MHz)|SDIO|7.08|7.92|µA/MHz|
|APB2<br>(up to 84 MHz)|TIM1|16.79|15.51|15.51|
|APB2<br>(up to 84 MHz)|TIM8|17.88|16.53|16.53|
|APB2<br>(up to 84 MHz)|TIM9|7.64|7.28|7.28|
|APB2<br>(up to 84 MHz)|TIM10|4.89|4.82|4.82|
|APB2<br>(up to 84 MHz)|TIM11|5.19|4.82|4.82|
|APB2<br>(up to 84 MHz)|ADC1(5)|4.67|4.58|4.58|
|APB2<br>(up to 84 MHz)|ADC2(5)|4.67|4.58|4.58|
|APB2<br>(up to 84 MHz)|ADC3(5)|4.43|4.44|4.44|
|APB2<br>(up to 84 MHz)|SPI1|1.32|1.39|1.39|
|APB2<br>(up to 84 MHz)|USART1|3.51|3.72|3.72|
|APB2<br>(up to 84 MHz)|USART6|3.55|3.75|3.75|
|APB2<br>(up to 84 MHz)|SYSCFG|0.74|0.56|0.56|



1. When the I/O compensation cell is ON, IDD typical value increases by 0.22 mA.

2. The BusMatrix is automatically active when at least one master is ON.


3. To enable an I2S peripheral, first set the I2SMOD bit and then the I2SE bit in the SPI_I2SCFGR register.


4. When the DAC is ON and EN1/2 bits are set in DAC_CR register, add an additional power consumption of
0.8 mA per DAC channel for the analog part.


5. When the ADC is ON (ADON bit set in the ADC_CR2 register), add an additional power consumption of
1.6 mA per ADC for the analog part.

### **6.3.7 Wakeup time from low-power mode**


The wakeup times given in _Table 29_ is measured on a wakeup phase with a 16 MHz HSI
RC oscillator. The clock source used to wake up the device depends from the current
operating mode:

      - Stop or Standby mode: the clock source is the RC oscillator

      - Sleep mode: the clock source is the clock that was set before entering Sleep mode.


All timings are derived from tests performed under ambient temperature and VDD supply
voltage conditions summarized in _Table 14_ .


<u>100/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 29. Low-power mode wakeup timings**












|Symbol|Parameter|Min(1)|Typ(1)|Max(1)|Unit|
|---|---|---|---|---|---|
|tWUSLEEP<br>(2)|Wakeup from Sleep mode|-|5|-|CPU<br>clock<br>cycle|
|tWUSTOP<br>(2)|Wakeup from Stop mode (regulator in Run mode and<br>flash memory in Stop mode)|-|13|-|µs|
|tWUSTOP<br>(2)|Wakeup from Stop mode (regulator in low-power mode<br>and flash memory in Stop mode)|-|17|40|40|
|tWUSTOP<br>(2)|Wakeup from Stop mode (regulator in Run mode and<br>flash memory in Deep power-down mode)|-|105|-|-|
|tWUSTOP<br>(2)|Wakeup from Stop mode (regulator in low-power mode<br>and flash memory in Deep power-down mode)|-|110|-|-|
|tWUSTDBY<br>(2)(3)|Wakeup from Standby mode|260|375|480|µs|



1. Evaluated by characterization - not tested in production.


2. The wakeup times are measured from the wakeup event to the point in which the application code reads the first instruction.

3. tWUSTDBY minimum and maximum values are given at 105 °C and –45 °C, respectively.

### **6.3.8 External clock source characteristics**


**High-speed external user clock generated from an external source**

#### The characteristics given in Table 30 result from tests performed using an high-speed

external clock source, and under ambient temperature and supply voltage conditions
summarized in _Table 14_ .

#### **Table 30. High-speed external user clock characteristics**





















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fHSE_ext|External user clock source<br>frequency(1)|-|1|-|50|MHz|
|VHSEH|OSC_IN input pin high level voltage|OSC_IN input pin high level voltage|0.7VDD|-|VDD|V|
|VHSEL|OSC_IN input pin low level voltage|OSC_IN input pin low level voltage|VSS|-|0.3VDD|0.3VDD|
|tw(HSE)<br>tw(HSE)|OSC_IN high or low time(1)|OSC_IN high or low time(1)|5|-|-|ns|
|tr(HSE)<br>tf(HSE)|OSC_IN rise or fall time(1)|OSC_IN rise or fall time(1)|-|-|10|10|
|Cin(HSE)|OSC_IN input capacitance(1)|-|-|5|-|pF|
|DuCy(HSE)|Duty cycle|-|45|-|55|%|
|IL|OSC_IN Input leakage current|VSS≤ VIN≤ VDD|-|-|±1|µA|


1. Specified by design.


<u>DS8626 Rev 12</u> <u>101/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**Low-speed external user clock generated from an external source**

#### The characteristics given in Table 31 result from tests performed using an low-speed

external clock source, and under ambient temperature and supply voltage conditions
summarized in _Table 14_ .

#### **Table 31. Low-speed external user clock characteristics**























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fLSE_ext|User External clock source<br>frequency(1)|-|-|32.768|1000|kHz|
|VLSEH|OSC32_IN input pin high level<br>voltage|OSC32_IN input pin high level<br>voltage|0.7VDD|-|VDD|V|
|VLSEL|OSC32_IN input pin low level voltage|OSC32_IN input pin low level voltage|VSS|-|0.3VDD|0.3VDD|
|tw(LSE)<br>tf(LSE)|OSC32_IN high or low time(1)|OSC32_IN high or low time(1)|450|-|-|ns|
|tr(LSE)<br>tf(LSE)|OSC32_IN rise or fall time(1)|OSC32_IN rise or fall time(1)|-|-|50|50|
|Cin(LSE)|OSC32_IN input capacitance(1)|-|-|5|-|pF|
|DuCy(LSE)|Duty cycle|-|30|-|70|%|
|IL|OSC32_IN Input leakage current|VSS≤ VIN≤ VDD|-|-|±1|µA|


1. Specified by design.

#### **Figure 30. High-speed external clock source AC timing diagram**




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||















<u>102/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 31. Low-speed external clock source AC timing diagram**








|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||











**High-speed external clock generated from a crystal/ceramic resonator**





The high-speed external (HSE) clock can be supplied with a 4 to 26 MHz crystal/ceramic
resonator oscillator. All the information given in this paragraph are based on
#### characterization results obtained with typical external components specified in Table 32 . In

the application, the resonator and the load capacitors have to be placed as close as
possible to the oscillator pins in order to minimize output distortion and startup stabilization
time. Refer to the crystal resonator manufacturer for more details on the resonator
characteristics (frequency, package, accuracy).

#### **Table 32. HSE 4-26 MHz oscillator characteristics (1)**














|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fOSC_IN|Oscillator frequency|-|4|-|26|MHz|
|RF|Feedback resistor|-|-|200|-|kΩ|
|Gm|Oscillator transconductance|Startup|5|-|-|mA/V|
|Gmcritmax|Maximum critical crystal Gm|Maximum critical crystal Gm|-|-|1|1|
|tSU(HSE)<br>(2)|Startup time|VDD is stabilized|-|2|-|ms|



1. Specified by design.

2. Evaluated by characterization - not tested in production. tSU(HSE) is the startup time measured from the
moment it is enabled (by software) to a stabilized 8 MHz oscillation is reached. This value is measured for
a standard crystal resonator and can vary significantly with the crystal manufacturer


For CL1 and CL2, it is recommended to use high-quality external ceramic capacitors in the
5 pF to 25 pF range (typ.), designed for high-frequency applications, and selected to match
the requirements of the crystal or resonator (see _Figure 32_ ). CL1 and CL2 are usually the
same size. The crystal manufacturer typically specifies a load capacitance which is the
series combination of CL1 and CL2. PCB and MCU pin capacitance must be included (10 pF
can be used as a rough estimate of the combined pin and board capacitance) when sizing
CL1 and CL2.


<u>DS8626 Rev 12</u> <u>103/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


_Note:_ _For information on electing the crystal, refer to the application note AN2867 “Oscillator_
_design guide for ST microcontrollers” available from the ST website www.st.com._

#### **Figure 32. Typical application with an 8 MHz crystal**




|8 MHz<br>resonator|Col2|Col3|
|---|---|---|
|8 MHz<br>resonator|||


|Col1|Col2|Col3|
|---|---|---|
||RF|Bias<br>controlled<br>gain|
||||











1. REXT value depends on the crystal characteristics.


**Low-speed external clock generated from a crystal/ceramic resonator**


The low-speed external (LSE) clock can be supplied with a 32.768 kHz crystal/ceramic
resonator oscillator. All the information given in this paragraph are based on
#### characterization results obtained with typical external components specified in Table 33 . In

the application, the resonator and the load capacitors have to be placed as close as
possible to the oscillator pins in order to minimize output distortion and startup stabilization
time. Refer to the crystal resonator manufacturer for more details on the resonator
characteristics (frequency, package, accuracy).

#### **Table 33. LSE oscillator characteristics (fLSE = 32.768 kHz) (1)**














|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fOSC_IN|Oscillator frequency|-|-|32.768|-|kHz|
|RF|Feedback resistor|-|-|18.4|-|MΩ|
|IDD|LSE current consumption|-|-|-|1|µA|
|Gm|Oscillator transconductance|Startup|2.8|-|-|µA/V|
|Gmcritmax|Maximum critical crystal Gm|Maximum critical crystal Gm|-|-|0.56|0.56|
|tSU(LSE)<br>(2)|Startup time|VDD is stabilized|-|2|-|s|



1. Specified by design.

2. Evaluated by characterization - not tested in production. tSU(LSE) is the startup time measured from the
moment it is enabled (by software) to a stabilized 32.768 kHz oscillation is reached. This value is
measured for a standard crystal resonator and it can vary significantly with the crystal manufacturer


_Note:_ _For information on electing the crystal, refer to the application note AN2867 “Oscillator_
_design guide for ST microcontrollers” available from the ST website www.st.com._


<u>104/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 33. Typical application with a 32.768 kHz crystal**










|Col1|Col2|Col3|
|---|---|---|
|32.768 kHz<br>resonator|||
|32.768 kHz<br>resonator|||


|Col1|Col2|Col3|
|---|---|---|
||RF|Bias<br>controlled<br>gain|
||||




### **6.3.9 Internal clock source characteristics**

#### The parameters given in Table 34 and Table 35 are derived from tests performed under

ambient temperature and VDD supply voltage conditions summarized in _Table 14_ .


**High-speed internal (HSI) RC oscillator**

#### **Table 34. HSI oscillator characteristics (1)**























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fHSI|Frequency|-|-|16|-|MHz|
|ACCHSI|HSI user trimming step(2)|-|-|-|1|%|
|ACCHSI|Accuracy of the HSI oscillator|TA = –40 to 105 °C(3)|–8|-|4.5|%|
|ACCHSI|Accuracy of the HSI oscillator|TA = –10 to 85 °C(3)|–4|-|4|%|
|ACCHSI|Accuracy of the HSI oscillator|TA = 25 °C(4)|–1|-|1|%|
|tsu(HSI)<br>(2)|HSI oscillator startup time|-|-|2.2|4|µs|
|IDD(HSI)<br>(2)|HSI oscillator power<br>consumption|-|-|60|80|µA|


1. VDD = 3.3 V, PLL OFF, TA = –40 to 125 °C unless otherwise specified.

2. Specified by design.


3. Evaluated by characterization - not tested in production.


4. Factory calibrated, parts not soldered.


**Low-speed internal (LSI) RC oscillator**

#### **Table 35. LSI oscillator characteristics (1)**












|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|fLSI<br>(2)|Frequency|17|32|47|kHz|
|tsu(LSI)<br>(3)|LSI oscillator startup time|-|15|40|µs|
|IDD(LSI)<br>(3)|LSI oscillator power consumption|-|0.4|0.6|µA|



1. VDD = 3 V, TA = –40 to 105 °C unless otherwise specified.

2. Evaluated by characterization - not tested in production.


3. Specified by design.


<u>DS8626 Rev 12</u> <u>105/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**








### **6.3.10 PLL characteristics**

#### The parameters given in Table 36 and Table 37 are derived from tests performed under

temperature and VDD supply voltage conditions summarized in _Table 14_ .

#### **Table 36. Main PLL characteristics**












|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fPLL_IN|PLL input clock(1)|-|0.95(2)|1|2.10|MHz|
|fPLL_OUT|PLL multiplier output clock|-|24|-|168|MHz|
|fPLL48_OUT|48 MHz PLL multiplier output<br>clock|-|-|48|75|MHz|
|fVCO_OUT|PLL VCO output|-|100|-|432|MHz|
|tLOCK|PLL lock time|VCO freq = 100 MHz|75|-|200|µs|
|tLOCK|PLL lock time|VCO freq = 432 MHz|100|-|300|300|



<u>106/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**<u>Table 36. Main PLL characteristics (continued)</u>**
































|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|Jitter(3)|Cycle-to-cycle jitter|System clock<br>120 MHz|RMS|-|25|-|ps|
|Jitter(3)|Cycle-to-cycle jitter|System clock<br>120 MHz|peak<br>to<br>peak|-|±150|-|-|
|Jitter(3)|Period Jitter|Period Jitter|RMS|-|15|-|-|
|Jitter(3)|Period Jitter|Period Jitter|peak<br>to<br>peak|-|±200|-|-|
|Jitter(3)|Main clock output (MCO) for<br>RMII Ethernet|Cycle to cycle at 50 MHz<br>on 1000 samples|Cycle to cycle at 50 MHz<br>on 1000 samples|-|32|-|-|
|Jitter(3)|Main clock output (MCO) for MII<br>Ethernet|Cycle to cycle at 25 MHz<br>on 1000 samples|Cycle to cycle at 25 MHz<br>on 1000 samples|-|40|-|-|
|Jitter(3)|Bit Time CAN jitter|Cycle to cycle at 1 MHz<br>on 1000 samples|Cycle to cycle at 1 MHz<br>on 1000 samples|-|330|-|-|
|IDD(PLL)<br>(4)|PLL power consumption on VDD|VCO freq = 100 MHz<br>VCO freq = 432 MHz|VCO freq = 100 MHz<br>VCO freq = 432 MHz|0.15<br>0.45|-|0.40<br>0.75|mA|
|IDDA(PLL)<br>(4)|PLL power consumption on<br>VDDA|VCO freq = 100 MHz<br>VCO freq = 432 MHz|VCO freq = 100 MHz<br>VCO freq = 432 MHz|0.30<br>0.55|-|0.40<br>0.85|mA|



1. Take care of using the appropriate division factor M to obtain the specified PLL input clock values. The M factor is shared
between PLL and PLLI2S.


2. Specified by design.


3. The use of 2 PLLs in parallel could degraded the Jitter up to +30%.


4. Evaluated by characterization - not tested in production.

#### **Table 37. PLLI2S (audio PLL) characteristics**

















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|fPLLI2S_IN|PLLI2S input clock(1)|-|-|0.95(2)|1|2.10|MHz|
|fPLLI2S_OUT|PLLI2S multiplier output clock|-|-|-|-|216|MHz|
|fVCO_OUT|PLLI2S VCO output|-|-|100|-|432|MHz|
|tLOCK|PLLI2S lock time|VCO freq = 100 MHz|VCO freq = 100 MHz|75|-|200|µs|
|tLOCK|PLLI2S lock time|VCO freq = 432 MHz|VCO freq = 432 MHz|100|-|300|300|
|Jitter(3)|Master I2S clock jitter|Cycle to cycle at<br>12.288 MHz on<br>48KHz period,<br>N=432, R=5|RMS|-|90|-||
|Jitter(3)|Master I2S clock jitter|Cycle to cycle at<br>12.288 MHz on<br>48KHz period,<br>N=432, R=5|peak<br>to<br>peak|-|±280|-|ps|
|Jitter(3)|Master I2S clock jitter|Average frequency of<br>12.288 MHz<br>N = 432, R = 5<br>on 1000 samples|Average frequency of<br>12.288 MHz<br>N = 432, R = 5<br>on 1000 samples|-|90|-|ps|
|Jitter(3)|WS I2S clock jitter|Cycle to cycle at 48 KHz<br>on 1000 samples|Cycle to cycle at 48 KHz<br>on 1000 samples|-|400|-|ps|


<u>DS8626 Rev 12</u> <u>107/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 37. PLLI2S (audio PLL) characteristics (continued)</u>**














|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|IDD(PLLI2S)<br>(4)|PLLI2S power consumption on<br>VDD|VCO freq = 100 MHz<br>VCO freq = 432 MHz|0.15<br>0.45|-|0.40<br>0.75|mA|
|IDDA(PLLI2S)<br>(4)|PLLI2S power consumption on<br>VDDA|VCO freq = 100 MHz<br>VCO freq = 432 MHz|0.30<br>0.55|-|0.40<br>0.85|mA|



1. Take care of using the appropriate division factor M to have the specified PLL input clock values.


2. Specified by design.


3. Value given with main PLL running.


4. Evaluated by characterization - not tested in production.

### **6.3.11 PLL spread spectrum clock generation (SSCG) characteristics**


The spread spectrum clock generation (SSCG) feature allows to reduce electromagnetic
interferences (see _Table 44: EMI characteristics for fHSE = 25 MH and fCPU = 168 MHz_ ). It
is available only on the main PLL.

#### **Table 38. SSCG parameters constraint**

|Symbol|Parameter|Min|Typ|Max(1)|Unit|
|---|---|---|---|---|---|
|fMod|Modulation frequency|-|-|10|KHz|
|md|Peak modulation depth|0.25|-|2|%|
|MODEPER * INCSTEP|-|-|-|215−1|-|



1. Specified by design.


Equation 1


The frequency modulation period (MODEPER) is given by the equation below:


MODEPER = round [ fPLL_IN ⁄ ( 4 × fMod )]


fPLL_IN and fMod must be expressed in Hz.

As an example:


If fPLL_IN = 1 MHz, and fMOD = 1 kHz, the modulation depth (MODEPER) is given by
equation 1:

### MODEPER = round [ 10 6 ⁄ ( 4 × 10 3 )] = 250


Equation 2


Equation 2 allows to calculate the increment step (INCSTEP):

INCSTEP = round [(( 2 <sup>15</sup>          - 1 ) × md × PLLN ) ⁄ ( 100 × 5 × MODEPER )]


fVCO_OUT must be expressed in MHz.


<u>108/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


With a modulation depth (md) = ±2 % (4 % peak to peak), and PLLN = 240 (in MHz):


INCSTEP = round [(( 2 <sup>15</sup>       - 1 ) × 2 × 240 ) ⁄ ( 100 × 5 × 250 )] = 126md(quantitazed)%


An amplitude quantization error may be generated because the linear modulation profile is
obtained by taking the quantized values (rounded to the nearest integer) of MODPER and
INCSTEP. As a result, the achieved modulation depth is quantized. The percentage
quantized modulation depth is given by the following formula:

mdquantized% = ( MODEPER × INCSTEP × 100 × 5 ) ⁄ (( 2 <sup>15</sup>            - 1 ) × PLLN )


As a result:

mdquantized% = ( 250 × 126 × 100 × 5 ) ⁄ (( 2 <sup>15</sup>            - 1 ) × 240 ) = 2.002%(peak)

#### Figure 35 and Figure 36 show the main PLL output clock waveforms in center spread and

down spread modes, where:

F0 is fPLL_OUT nominal.

Tmode is the modulation period.

md is the modulation depth.

#### **Figure 35. PLL output clock waveforms in center spread mode**













<u>DS8626 Rev 12</u> <u>109/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 36. PLL output clock waveforms in down spread mode**








### **6.3.12 Memory characteristics**

**Flash memory**


The characteristics are given at TA = –40 to 105 °C unless otherwise specified.

The devices are shipped to customers with the flash memory erased.

#### **Table 39. Flash memory characteristics**





|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|IDD|Supply current|Write / Erase 8-bit mode, VDD = 1.8 V|-|5|-|mA|
|IDD|Supply current|Write / Erase 16-bit mode, VDD = 2.1 V|-|8|-|-|
|IDD|Supply current|Write / Erase 32-bit mode, VDD = 3.3 V|-|12|-|-|

#### **Table 40. Flash memory programming**








|Symbol|Parameter|Conditions|Min(1)|Typ|Max(1)|Unit|
|---|---|---|---|---|---|---|
|tprog|Word programming time|Program/erase parallelism<br>(PSIZE) = x 8/16/32|-|16|100(2)|µs|
|tERASE16KB|Sector (16 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 8|-|400|800|ms|
|tERASE16KB|Sector (16 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 16|-|300|600|600|
|tERASE16KB|Sector (16 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 32|-|250|500|500|
|tERASE64KB|Sector (64 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 8|-|1200|2400|ms|
|tERASE64KB|Sector (64 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 16|-|700|1400|1400|
|tERASE64KB|Sector (64 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 32|-|550|1100|1100|



<u>110/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**<u>Table 40. Flash memory programming (continued)</u>**






|Symbol|Parameter|Conditions|Min(1)|Typ|Max(1)|Unit|
|---|---|---|---|---|---|---|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 8|-|2|4|s|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 16|-|1.3|2.6|2.6|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism<br>(PSIZE) = x 32|-|1|2|2|
|tME|Mass erase time|Program/erase parallelism<br>(PSIZE) = x 8|-|16|32|s|
|tME|Mass erase time|Program/erase parallelism<br>(PSIZE) = x 16|-|11|22|22|
|tME|Mass erase time|Program/erase parallelism<br>(PSIZE) = x 32|-|8|16|16|
|Vprog|Programming voltage|32-bit program operation|2.7|-|3.6|V|
|Vprog|Programming voltage|16-bit program operation|2.1|-|3.6|V|
|Vprog|Programming voltage|8-bit program operation|1.8|-|3.6|V|



1. Evaluated by characterization - not tested in production.


2. The maximum programming time is measured after 100K erase operations.


<u>DS8626 Rev 12</u> <u>111/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**
























|Symbol|Parameter|Conditions|Min(1)|Typ|Max(1)|Unit|
|---|---|---|---|---|---|---|
|tprog|Double word programming|TA =0 to +40 °C<br>VDD = 3.3 V<br>VPP = 8.5 V|-|16|100(2)|µs|
|tERASE16KB|Sector (16 KB) erase time|Sector (16 KB) erase time|-|230|-|ms|
|tERASE64KB|Sector (64 KB) erase time|Sector (64 KB) erase time|-|490|-|-|
|tERASE128KB|Sector (128 KB) erase time|Sector (128 KB) erase time|-|875|-|-|
|tME|Mass erase time|Mass erase time|-|6.9|-|s|
|Vprog|Programming voltage|-|2.7|-|3.6|V|
|VPP|VPP voltage range|-|7|-|9|V|
|IPP|Minimum current sunk on<br>the VPP pin|-|10|-|-|mA|
|tVPP<br>(3)|Cumulative time during<br>which VPPis applied|-|-|-|1|hour|



1. Specified by design.


2. The maximum programming time is measured after 100K erase operations.

3. VPP should only be connected during programming/erasing.

#### **Table 42. Flash memory endurance and data retention**
















|Symbol|Parameter|Conditions|Value|Unit|
|---|---|---|---|---|
|**Symbol**|**Parameter**|** Conditions**|**Min(1)**|**Min(1)**|
|NEND|Endurance|TA = –40 to +85 °C (6 suffix versions)<br>TA = –40 to +105 °C (7 suffix versions)|10|kcycles|
|tRET|Data retention|1 kcycle(2) at TA = 85 °C|30|Years|
|tRET|Data retention|1 kcycle(2) at TA = 105 °C|10|10|
|tRET|Data retention|10 kcycles(2) at TA = 55 °C|20|20|



1. Evaluated by characterization - not tested in production.


2. Cycling performed over the whole temperature range.

### **6.3.13 EMC characteristics**


Susceptibility tests are performed on a sample basis during device characterization.


**Functional EMS (electromagnetic susceptibility)**


While a simple application is executed on the device (toggling 2 LEDs through I/O ports).
the device is stressed by two electromagnetic events until a failure occurs. The failure is
indicated by the LEDs:

      - **Electrostatic discharge (ESD)** (positive and negative) is applied to all device pins until
a functional disturbance occurs. This test is compliant with the IEC 61000-4-2 standard.

      - **FTB** : A burst of fast transient voltage (positive and negative) is applied to VDD and VSS
through a 100 pF capacitor, until a functional disturbance occurs. This test is compliant
with the IEC 61000-4-4 standard.


<u>112/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


A device reset allows normal operations to be resumed.

#### The test results are given in Table 43 . They are based on the EMS levels and classes

defined in application note AN1709.

#### **Table 43. EMS characteristics**










|Symbol|Parameter|Conditions|Level/<br>Class|
|---|---|---|---|
|VFESD|Voltage limits to be applied on any I/O pin to<br>induce a functional disturbance|VDD= 3.3 V, LQFP176, TA = +25 °C,<br>fHCLK = 168 MHz, conforms to<br>IEC 61000-4-2|2B|
|VEFTB|Fast transient voltage burst limits to be<br>applied through 100 pF on VDD and VSS<br>pins to induce a functional disturbance|VDD =3.3 V, LQFP176, TA = +25 °C,<br>fHCLK = 168 MHz, conforms to<br>IEC 61000-4-2|4A|



**Designing hardened software to avoid noise problems**


EMC characterization and optimization are performed at component level with a typical
application environment and simplified MCU software. It should be noted that good EMC
performance is highly dependent on the user application and the software in particular.


Therefore it is recommended that the user applies EMC software optimization and
prequalification tests in relation with the EMC level requested for his application.


Software recommendations


The software flowchart must include the management of runaway conditions such as:

- Corrupted program counter

- Unexpected reset

- Critical Data corruption (control registers...)


Prequalification trials


Most of the common failures (unexpected reset and program counter corruption) can be
reproduced by manually forcing a low state on the NRST pin or the Oscillator pins for 1
second.


To complete these trials, ESD stress can be applied directly on the device, over the range of
specification values. When unexpected behavior is detected, the software can be hardened
to prevent unrecoverable errors occurring (see application note AN1015).


<u>DS8626 Rev 12</u> <u>113/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**Electromagnetic Interference (EMI)**


The electromagnetic field emitted by the device are monitored while a simple application,
executing EEMBC code, is running. This emission test is compliant with SAE IEC61967-2
standard which specifies the test board and the pin loading.


















|Col1|Table 4|44. EMI characteristics for fHSE = 25|5 MH and fCPU = 168|MHz|Col6|
|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Monitored**<br>**frequency band**|**Value**|**Unit**|
|SEMI|Peak(1)|VDD= 3.3 V, TA = 25 °C, LQFP176<br>package, conforming to SAE J1752/3<br>EEMBC, code running from flash<br>memory with ART accelerator enabled|0.1 to 30 MHz|32|dBµV|
|SEMI|Peak(1)|VDD= 3.3 V, TA = 25 °C, LQFP176<br>package, conforming to SAE J1752/3<br>EEMBC, code running from flash<br>memory with ART accelerator enabled|30 to 130 MHz|25|25|
|SEMI|Peak(1)|VDD= 3.3 V, TA = 25 °C, LQFP176<br>package, conforming to SAE J1752/3<br>EEMBC, code running from flash<br>memory with ART accelerator enabled|130 MHz to 1GHz|29|29|
|SEMI|Level(2)|Level(2)|0.1 MHz to 2 GHz|4|-|
|SEMI|Peak(1)|VDD= 3.3 V, TA = 25 °C, LQFP176<br>package, conforming to SAE J1752/3<br>EEMBC, code running from flash<br>memory with ART accelerator and PLL<br>spread spectrum enabled|0.1 to 30 MHz|19|dBµV|
|SEMI|Peak(1)|VDD= 3.3 V, TA = 25 °C, LQFP176<br>package, conforming to SAE J1752/3<br>EEMBC, code running from flash<br>memory with ART accelerator and PLL<br>spread spectrum enabled|30 to 130 MHz|16|16|
|SEMI|Peak(1)|VDD= 3.3 V, TA = 25 °C, LQFP176<br>package, conforming to SAE J1752/3<br>EEMBC, code running from flash<br>memory with ART accelerator and PLL<br>spread spectrum enabled|130 MHz to 1GHz|18|18|
|SEMI|Level(2)|Level(2)|0.1 MHz to 2 GHz|3.5|-|



1. Refer to AN1709 "EMI radiated test" chapter.


2. Refer to AN1709 "EMI level classification" chapter.

### **6.3.14 Absolute maximum ratings (electrical sensitivity)**


Stresses above the absolute maximum ratings listed in _Table 11: Voltage characteristics_,
_Table 12: Current characteristics_, and _Table 13: Thermal characteristics_ may cause
permanent damage to the device. These are stress ratings only and the functional operation
of the device at these conditions is not implied. Exposure to maximum rating conditions for
extended periods may affect device reliability. Device mission profile (application conditions)
is compliant with JEDEC JESD47 Qualification Standard, extended mission profiles are
available on demand.


**Electrostatic discharge (ESD)**


Electrostatic discharges (a positive then a negative pulse separated by 1 second) are
applied to the pins of each sample according to each pin combination. The sample size
depends on the number of supply pins in the device (3 parts × (n+1) supply pins). This test
conforms to the JESD22-A114/C101 standard.










|Col1|Table 45.|ESD absolute maximum ratings|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Symbol**|**Ratings**|**Conditions**|**Class**|**Maximum**<br>**value(1)**|**Unit**|
|VESD(HBM)|Electrostatic discharge<br>voltage (human body<br>model)|TA = +25 °C conforming to JESD22-A114|2|2000(2)|V|
|VESD(CDM)|Electrostatic discharge<br>voltage (charge device<br>model)|TA = +25 °C conforming to<br>ANSI/ESDA/JEDEC JS-002|II|250|250|



1. Evaluated by characterization - not tested in production.


<u>114/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


2. On VBAT pin, VESD(HBM) is limited to 1000 V.


**Static latchup**


Two complementary static tests are required on six parts to assess the latchup
performance:

       - A supply overvoltage is applied to each power supply pin

       - A current injection is applied to each input, output and configurable I/O pin


These tests are compliant with EIA/JESD 78A IC latchup standard.

#### **Table 46. Electrical sensitivities**

|Symbol|Parameter|Conditions|Class|
|---|---|---|---|
|LU|Static latch-up class|TA = +105 °C conforming to JESD78A|II level A|


### **6.3.15 I/O current injection characteristics**


As a general rule, current injection to the I/O pins, due to external voltage below VSS or
above VDD (for standard, 3 V-capable I/O pins) should be avoided during normal product
operation. However, in order to give an indication of the robustness of the microcontroller in
cases when abnormal injection accidentally happens, susceptibility tests are performed on a
sample basis during device characterization.


**Functional susceptibilty to I/O current injection**


While a simple application is executed on the device, the device is stressed by injecting
current into the I/O pins programmed in floating input mode. While current is injected into
the I/O pin, one at a time, the device is checked for functional failures.


The failure is indicated by an out of range parameter: ADC error above a certain limit (>5
LSB TUE), out of conventional limits of induced leakage current on adjacent pins (out of
5 μA/+0 μA range), or other functional failure (for example reset, oscillator frequency
deviation).


Negative induced leakage current is caused by negative injection and positive induced
leakage current by positive injection.


The test results are given in _Table 47_ .


<u>DS8626 Rev 12</u> <u>115/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Table 47. I/O current injection susceptibility**



















|Symbol|Description|Functional susceptibility|Col4|Unit|
|---|---|---|---|---|
|**Symbol**|**Description**|**Negative**<br>**injection**|**Positive**<br>**injection**|**Positive**<br>**injection**|
|IINJ<br>(1)|Injected current on BOOT0 pin|−0|NA|mA|
|IINJ<br>(1)|Injected current on NRST pin|−0|NA|NA|
|IINJ<br>(1)|Injected current on PE2, PE3, PE4, PE5, PE6,<br>PI8, PC13, PC14, PC15, PI9, PI10, PI11, PF0,<br>PF1, PF2, PF3, PF4, PF5, PF10, PH0/OSC_IN,<br>PH1/OSC_OUT, PC0, PC1, PC2, PC3, PB6,<br>PB7, PB8, PB9, PE0, PE1, PI4, PI5, PI6, PI7,<br>PDR_ON, BYPASS_REG|−0|NA|NA|
|IINJ<br>(1)|Injected current on all FT pins|−5|NA|NA|
|IINJ<br>(1)|Injected current on any other pin|−5|+5|+5|


1. It is recommended to add a Schottky diode (pin to ground) to analog pins which may potentially inject negative currents.

### **6.3.16 I/O port characteristics**


**General input/output characteristics**

#### Unless otherwise specified, the parameters given in Table 48 are derived from tests

performed under the conditions summarized in _Table 14_ . All I/Os are CMOS and TTL
compliant.


_Note:_ _For information on GPIO configuration, refer to application note AN4899 “STM32 GPIO_
_configuration for hardware settings and low-power consumption” available from the ST_
_website www.st.com._

#### **Table 48. I/O static characteristics**




















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VIL|FT, TTa and NRST I/O input low<br>level voltage|1.7 V ≤ VDD≤ 3.6 V|-|-|0.3VDD-0.04(1)|V|
|VIL|FT, TTa and NRST I/O input low<br>level voltage|1.7 V ≤ VDD≤ 3.6 V|-|-|0.3VDD<br>(2)|0.3VDD<br>(2)|
|VIL|BOOT0 I/O input low level<br>voltage|1.75 V ≤ VDD≤ 3.6 V<br>-40 °C≤ TA ≤ 105 °C|-|-|0.1VDD-+0.1(1)|0.1VDD-+0.1(1)|
|VIL|BOOT0 I/O input low level<br>voltage|1.7 V ≤ VDD≤ 3.6 V<br>0 °C≤ TA ≤ 105 °C|-|-|-|-|
|VIH|FT, TTa and NRST I/O input low<br>level voltage|1.7 V ≤ VDD≤ 3.6 V|0.45VDD+0.3(1)|-|-|-|
|VIH|FT, TTa and NRST I/O input low<br>level voltage|1.7 V ≤ VDD≤ 3.6 V|0.7VDD<br>(2)|-|-|-|
|VIH|BOOT0 I/O input low level<br>voltage|1.75 V ≤ VDD≤ 3.6 V<br>-40 °C≤ TA ≤ 105 °C|0.17VDD+0.7(1)|-|-|-|
|VIH|BOOT0 I/O input low level<br>voltage|1.7 V ≤ VDD≤ 3.6 V<br>0 °C≤ TA ≤ 105 °C|1.7 V ≤ VDD≤ 3.6 V<br>0 °C≤ TA ≤ 105 °C|-|-|-|



<u>116/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**<u>Table 48. I/O static characteristics (continued)</u>**


























|Symbol|Parameter|Col3|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VHYS|FT, TTa and NRST I/O input<br>hysteresis|FT, TTa and NRST I/O input<br>hysteresis|1.7 V ≤ VDD≤ 3.6 V|10%VDD<br>(3)|-|-|V|
|VHYS|BOOT0 I/O input hysteresis|BOOT0 I/O input hysteresis|1.75 V ≤ VDD≤ 3.6 V<br>-40 °C≤ TA ≤ 105 °C|0.1|-|-|-|
|VHYS|BOOT0 I/O input hysteresis|BOOT0 I/O input hysteresis|1.7 V ≤ VDD≤ 3.6 V<br>0 °C≤ TA ≤ 105 °C|1.7 V ≤ VDD≤ 3.6 V<br>0 °C≤ TA ≤ 105 °C|1.7 V ≤ VDD≤ 3.6 V<br>0 °C≤ TA ≤ 105 °C|1.7 V ≤ VDD≤ 3.6 V<br>0 °C≤ TA ≤ 105 °C|1.7 V ≤ VDD≤ 3.6 V<br>0 °C≤ TA ≤ 105 °C|
|Ilkg|I/O input leakage current(4)|I/O input leakage current(4)|VSS≤ VIN≤ VDD|-|-|±1|µA|
|Ilkg|I/O FT input leakage current(5)|I/O FT input leakage current(5)|VIN= 5 V|-|-|3|3|
|RPU|Weak pull-up<br>equivalent<br>resistor(6)|All pins<br>except for<br>PA10 and<br>PB12<br>(OTG_FS_ID,<br>OTG_HS_ID)|VIN= VSS|30|40|50|kΩ|
|RPU|Weak pull-up<br>equivalent<br>resistor(6)|PA10 and<br>PB12<br>(OTG_FS_ID,<br>OTG_HS_ID)|-|7|10|14|14|
|RPD|Weak pull-down<br>equivalent<br>resistor(7)|All pins<br>except for<br>PA10 and<br>PB12|VIN= VDD|30|40|50|50|
|RPD|Weak pull-down<br>equivalent<br>resistor(7)|PA10 and<br>PB12|-|7|10|14|14|
|CIO<br>(8)|I/O pin<br>capacitance|-|-|-|5|-|pF|



1. Specified by design.


2. Tested in production.


3. With a minimum of 200 mV.


4. Leakage could be higher than the maximum value, if negative current is injected on adjacent pins.Refer to _Table 47: I/O_
_current injection susceptibility_

5. To sustain a voltage higher than VDD + 0.3 V, the internal pull-up/pull-down resistors must be disabled. Leakage could be
higher than the maximum value, if negative current is injected on adjacent pins. Refer to _Table 47: I/O current injection_
_susceptibility_ .


6. Pull-up and pull-down resistors are designed with a true resistance in series with a switchable PMOS. This PMOS
contribution to the series resistance is minimum (~10% order).

7. Pull-up and pull-down resistors are designed with a true resistance in series with a switchable NMOS. This NMOS
contribution to the series resistance is minimum (~10% order).

8. Hysteresis voltage between Schmitt trigger switching levels. Evaluated by characterization - not tested in production.


All I/Os are CMOS and TTL compliant (no software configuration required). Their
characteristics cover more than the strict CMOS-technology or TTL parameters.


<u>DS8626 Rev 12</u> <u>117/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**Output driving current**


The GPIOs (general purpose input/outputs) can sink or source up to ± 8 mA, and sink or
source up to ± 20 mA (with a relaxed VOL/VOH) except PC13, PC14 and PC15 which can
sink or source up to ± 3mA. When using the PC13 to PC15 GPIOs in output mode, the speed
should not exceed 2 MHz with a maximum load of 30 pF.


In the user application, the number of I/O pins which can drive current must be limited to
respect the absolute maximum rating specified in _Section 6.2_ . In particular:

      - The sum of the currents sourced by all the I/Os on VDD, plus the maximum Run
consumption of the MCU sourced on VDD, cannot exceed the absolute maximum rating
IVDD (see _Table 12_ ).

      - The sum of the currents sunk by all the I/Os on VSS plus the maximum Run
consumption of the MCU sunk on VSS cannot exceed the absolute maximum rating
IVSS (see _Table 12_ ).


**Output voltage levels**

#### Unless otherwise specified, the parameters given in Table 49 are derived from tests

performed under ambient temperature and VDD supply voltage conditions summarized in
_Table 14_ . All I/Os are CMOS and TTL compliant.

#### **Table 49. Output voltage characteristics (1)**








































|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|VOL<br>(2)|Output low level voltage|CMOS port<br>IIO= +8 mA<br>2.7 V < VDD < 3.6 V|-|0.4|V|
|VOH<br>(3)|Output high level voltage|Output high level voltage|VDD–0.4|-|-|
|VOL<br>(2)|Output low level voltage|TTL port<br>IIO=+ 8mA<br>2.7 V < VDD < 3.6 V|-|0.4|V|
|VOH<br>(3)|Output high level voltage|Output high level voltage|2.4|-|-|
|VOL<br>(2)(4)<br>|Output low level voltage<br>|IIO= +20 mA<br>2.7 V < VDD < 3.6 V|-|1.3|V|
|VOH<br>(3)(4)|Output high level voltage|Output high level voltage|VDD–1.3|-|-|
|VOL<br>(2)(4)<br>|Output low level voltage<br>|IIO= +6 mA<br>2 V < VDD < 2.7 V|-|0.4|V|
|VOH<br>(3)(4)|Output high level voltage|Output high level voltage|VDD–0.4|-|-|



1. PC13, PC14, PC15 and PI8 are supplied through the power switch. Since the switch only sinks a limited
amount of current (3 mA), the use of GPIOs PC13 to PC15 and PI8 in output mode is limited: the speed
should not exceed 2 MHz with a maximum load of 30 pF and these I/Os must not be used as a current
source (e.g. to drive an LED).

2. The IIO current sunk by the device must always respect the absolute maximum rating specified in _Table 12_
and the sum of IIO (I/O ports and control pins) must not exceed IVSS.

3. The IIO current sourced by the device must always respect the absolute maximum rating specified in
_Table 12_ and the sum of IIO (I/O ports and control pins) must not exceed IVDD.

4. Evaluated by characterization - not tested in production.


<u>118/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**Input/output AC characteristics**


The definition and values of input/output AC characteristics are given in _Figure 37_ and
#### Table 50, respectively. Unless otherwise specified, the parameters given in Table 50 are derived from tests

performed under the ambient temperature and VDD supply voltage conditions summarized
in _Table 14_ .

#### **Table 50. I/O AC characteristics (1)(2)**


























|OSPEEDRy<br>[1:0] bit<br>value(1)|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|00|fmax(IO)out|Maximum frequency(3)|CL = 50 pF, VDD >2.70 V|-|-|4|MHz|
|00|fmax(IO)out|Maximum frequency(3)|CL = 50 pF, VDD >1.8 V|-|-|2|2|
|00|fmax(IO)out|Maximum frequency(3)|CL = 10 pF, VDD >2.70 V|-|-|8|8|
|00|fmax(IO)out|Maximum frequency(3)|CL = 10 pF, VDD >1.8 V|-|-|4|4|
|00|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 50 pF, VDD= 1.8 V to<br>3.6 V|-|-|100|ns|
|01|fmax(IO)out|Maximum frequency(3)|CL = 50 pF, VDD >2.70 V|-|-|25|MHz|
|01|fmax(IO)out|Maximum frequency(3)|CL = 50 pF, VDD >1.8 V|-|-|12.5|12.5|
|01|fmax(IO)out|Maximum frequency(3)|CL = 10 pF, VDD >2.70 V|-|-|50(4)|50(4)|
|01|fmax(IO)out|Maximum frequency(3)|CL = 10 pF, VDD >1.8 V|-|-|20|20|
|01|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 50 pF, VDD>2.7 V|-|-|10|ns|
|01|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 50 pF, VDD> 1.8 V|-|-|20|20|
|01|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 10 pF, VDD >2.70 V|-|-|6|6|
|01|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 10 pF, VDD >1.8 V|-|-|10|10|
|10|fmax(IO)out|Maximum frequency(3)|CL = 40 pF, VDD >2.70 V|-|-|50(4)|MHz|
|10|fmax(IO)out|Maximum frequency(3)|CL = 40 pF, VDD >1.8 V|-|-|25|25|
|10|fmax(IO)out|Maximum frequency(3)|CL = 10 pF, VDD >2.70 V|-|-|100(4)|100(4)|
|10|fmax(IO)out|Maximum frequency(3)|CL = 10 pF, VDD >1.8 V|-|-|50(4)|50(4)|
|10|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 40 pF, VDD >2.70 V|-|-|6|ns|
|10|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 40 pF, VDD >1.8 V|-|-|10|10|
|10|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 10 pF, VDD >2.70 V|-|-|4|4|
|10|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 10 pF, VDD >1.8 V|-|-|6|6|



<u>DS8626 Rev 12</u> <u>119/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 50. I/O AC characteristics</u>** <sup>**(1)(2)**</sup> **<u>(continued)</u>**
















|OSPEEDRy<br>[1:0] bit<br>value(1)|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|11|Fmax(IO)out|Maximum frequency(3)|CL = 30 pF, VDD >2.70 V|-|-|100(4)|MHz|
|11|Fmax(IO)out|Maximum frequency(3)|CL = 30 pF, VDD >1.8 V|-|-|50(4)|50(4)|
|11|Fmax(IO)out|Maximum frequency(3)|CL = 10 pF, VDD >2.70 V|-|-|180(4)|180(4)|
|11|Fmax(IO)out|Maximum frequency(3)|CL = 10 pF, VDD >1.8 V|-|-|100(4)|100(4)|
|11|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 30 pF, VDD >2.70 V|-|-|4|ns|
|11|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 30 pF, VDD >1.8 V|-|-|6|6|
|11|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 10 pF, VDD >2.70 V|-|-|2.5|2.5|
|11|tf(IO)out/<br>tr(IO)out|Output high to low level fall<br>time and output low to high<br>level rise time|CL = 10 pF, VDD >1.8 V|-|-|4|4|
|-|tEXTIpw|Pulse width of external signals<br>detected by the EXTI<br>controller|-|10|-|-|ns|



1. Evaluated by characterization - not tested in production.


2. The I/O speed is configured using the OSPEEDRy[1:0] bits. Refer to the STM32F4xx reference manual for a description of
the GPIOx_SPEEDR GPIO port output speed register.

#### 3. The maximum frequency is defined in Figure 37 .


4. For maximum frequencies above 50 MHz, the compensation cell should be used.

#### **Figure 37. I/O AC characteristics definition**



















<u>120/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

### **6.3.17 NRST pin characteristics**


The NRST pin input driver uses CMOS technology. It is connected to a permanent pull-up
resistor, RPU (see _Table 48_ ).
#### Unless otherwise specified, the parameters given in Table 51 are derived from tests

performed under the ambient temperature and VDD supply voltage conditions summarized
in _Table 14_ .

#### **Table 51. NRST pin characteristics**
































|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VIL(NRST)<br>(1)|NRST Input low level voltage|TTL ports<br>2.7 V ≤ VDD ≤ 3.6 V|-|-|0.8|V|
|VIH(NRST)<br>(1)|NRST Input high level voltage|NRST Input high level voltage|2|-|-|-|
|VIL(NRST)<br>(1)|NRST Input low level voltage|CMOS ports<br>1.8 V ≤ VDD ≤ 3.6 V|-|-|0.3VDD|0.3VDD|
|VIH(NRST)<br>(1)|NRST Input high level voltage|NRST Input high level voltage|0.7VDD|-|-|-|
|Vhys(NRST)|NRST Schmitt trigger voltage<br>hysteresis|-|-|200|-|mV|
|RPU|Weak pull-up equivalent resistor(2)|VIN =VSS|30|40|50|kΩ|
|VF(NRST)<br>(1)<br>|NRST Input filtered pulse<br>|-|-|-|100|ns|
|VNF(NRST)<br>(1)|NRST Input not filtered pulse|VDD > 2.7 V|300|-|-|ns|
|TNRST_OUT|Generated reset pulse duration|Internal reset<br>source|20|-|-|µs|



1. Specified by design.


2. The pull-up is designed with a true resistance in series with a switchable PMOS. This PMOS contribution to
the series resistance must be minimum (~10% order).

#### **Figure 38. Recommended NRST pin protection**













1. The reset network protects the device against parasitic resets.

2. The user must ensure that the level on the NRST pin can go below the VIL(NRST) max level specified in
#### Table 51 . Otherwise the reset is not taken into account by the device.

### **6.3.18 TIM timer characteristics**


The parameters given in _Table 52_ and _Table 53_ are specified by design.


Refer to _Section 6.3.16: I/O port characteristics_ for details on the input/output alternate
function characteristics (output compare, input capture, external clock, PWM output).


<u>DS8626 Rev 12</u> <u>121/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Table 52. Characteristics of TIMx connected to the APB1 domain (1)**
























|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|tres(TIM)|Timer resolution time|AHB/APB1<br>prescaler distinct<br>from 1, fTIMxCLK =<br>84 MHz|1|-|tTIMxCLK|
|tres(TIM)|Timer resolution time|AHB/APB1<br>prescaler distinct<br>from 1, fTIMxCLK =<br>84 MHz|11.9|-|ns|
|tres(TIM)|Timer resolution time|AHB/APB1<br>prescaler = 1,<br>fTIMxCLK = 42 MHz|1|-|tTIMxCLK|
|tres(TIM)|Timer resolution time|AHB/APB1<br>prescaler = 1,<br>fTIMxCLK = 42 MHz|23.8|-|ns|
|fEXT|Timer external clock<br>frequency on CH1 to CH4|fTIMxCLK = 84 MHz<br>APB1= 42 MHz|0|fTIMxCLK/2|MHz|
|fEXT|Timer external clock<br>frequency on CH1 to CH4|fTIMxCLK = 84 MHz<br>APB1= 42 MHz|0|42|MHz|
|ResTIM|Timer resolution|Timer resolution|-|16/32|bit|
|tCOUNTER|16-bit counter clock<br>period when internal clock<br>is selected|16-bit counter clock<br>period when internal clock<br>is selected|1|65536|tTIMxCLK|
|tCOUNTER|16-bit counter clock<br>period when internal clock<br>is selected|16-bit counter clock<br>period when internal clock<br>is selected|0.0119|780|µs|
|tCOUNTER|32-bit counter clock<br>period when internal clock<br>is selected|32-bit counter clock<br>period when internal clock<br>is selected|1|-|tTIMxCLK|
|tCOUNTER|32-bit counter clock<br>period when internal clock<br>is selected|32-bit counter clock<br>period when internal clock<br>is selected|0.0119|51130563|µs|
|tMAX_COUNT|Maximum possible count|Maximum possible count|-|65536 × 65536|tTIMxCLK|
|tMAX_COUNT|Maximum possible count|Maximum possible count|-|51.1|s|



1. TIMx is used as a general term to refer to the TIM2, TIM3, TIM4, TIM5, TIM6, TIM7, and TIM12 timers.


<u>122/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 53. Characteristics of TIMx connected to the APB2 domain (1)**























|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|tres(TIM)|Timer resolution time|AHB/APB2<br>prescaler distinct<br>from 1, fTIMxCLK =<br>168 MHz|1|-|tTIMxCLK|
|tres(TIM)|Timer resolution time|AHB/APB2<br>prescaler distinct<br>from 1, fTIMxCLK =<br>168 MHz|5.95|-|ns|
|tres(TIM)|Timer resolution time|AHB/APB2<br>prescaler = 1,<br>fTIMxCLK = 84 MHz|1|-|tTIMxCLK|
|tres(TIM)|Timer resolution time|AHB/APB2<br>prescaler = 1,<br>fTIMxCLK = 84 MHz|11.9|-|ns|
|fEXT|Timer external clock<br>frequency on CH1 to<br>CH4|fTIMxCLK =<br>168 MHz<br>APB2 = 84 MHz|0|fTIMxCLK/2|MHz|
|fEXT|Timer external clock<br>frequency on CH1 to<br>CH4|fTIMxCLK =<br>168 MHz<br>APB2 = 84 MHz|0|84|MHz|
|ResTIM|Timer resolution|Timer resolution|-|16|bit|
|tCOUNTER|16-bit counter clock<br>period when internal<br>clock is selected|16-bit counter clock<br>period when internal<br>clock is selected|1|65536|tTIMxCLK|
|tMAX_COUNT|Maximum possible count|Maximum possible count|-|32768|tTIMxCLK|


1. TIMx is used as a general term to refer to the TIM1, TIM8, TIM9, TIM10, and TIM11 timers.

### **6.3.19 Communications interfaces**

**I** <sup>**2**</sup> **C interface characteristics**

The I <sup>2</sup> C interface meets the timings requirements of the I <sup>2</sup> C-bus specification and user
manual rev. 03 for:

      - Standard-mode (Sm): with a bit rate up to 100 kbit/s

      - Fast-mode (Fm): with a bit rate up to 400 kbit/s.

The I <sup>2</sup> C timings requirements are specified by design when the I2C peripheral is properly
configured (refer to RM0090 reference manual).


The SDA and SCL I/O requirements are met with the following restrictions: the SDA and
SCL I/O pins are not “true” open-drain. When configured as open-drain, the PMOS
connected between the I/O pin and VDD is disabled, but is still present. Refer to
_Section 6.3.16: I/O port characteristics_ for more details on the I <sup>2</sup> C I/O characteristics.

All I <sup>2</sup> C SDA and SCL I/Os embed an analog filter. Refer to the table below for the analog
filter characteristics:

#### **Table 54. I2C analog filter characteristics (1)**












|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tAF|Maximum pulse width of spikes<br>that are suppressed by the analog<br>filter|50(2)|260(3)|ns|



1. Specified by design.

2. Spikes with widths below tAF(min) are filtered.

3. Spikes with widths above tAF(max) are not filtered


<u>DS8626 Rev 12</u> <u>123/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**SPI interface characteristics**

#### Unless otherwise specified, the parameters given in Table 55 for SPI are derived from tests

performed under the ambient temperature, fPCLKx frequency and VDD supply voltage
conditions summarized in _Table 14_ with the following configuration:

      - Output speed is set to OSPEEDRy[1:0] = 10

      - Capacitive load C = 30 pF

      - Measurement points are done at CMOS levels: 0.5 VDD

Refer to _Section 6.3.16: I/O port characteristics_ for more details on the input/output alternate
function characteristics (NSS, SCK, MOSI, MISO).

#### **Table 55. SPI dynamic characteristics (1)**





















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fSCK|SPI clock frequency|Master mode, SPI1, <br>2.7V < VDD < 3.6V|-|-|42|MHz|
|fSCK|SPI clock frequency|Slave mode, SPI1, <br>2.7V < VDD < 3.6V|Slave mode, SPI1, <br>2.7V < VDD < 3.6V|Slave mode, SPI1, <br>2.7V < VDD < 3.6V|42|42|
|1/tc(SCK)|1/tc(SCK)|Master mode, SPI1/2/3, <br>1.7V < VDD < 3.6V|-|-|21|21|
|1/tc(SCK)|1/tc(SCK)|Slave mode, SPI1/2/3, <br>1.7V < VDD < 3.6V|Slave mode, SPI1/2/3, <br>1.7V < VDD < 3.6V|Slave mode, SPI1/2/3, <br>1.7V < VDD < 3.6V|21|21|
|Duty(SCK)|Duty cycle of SPI clock<br>frequency|Slave mode|30|50|70|%|


<u>124/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**<u>Table 55. SPI dynamic characteristics</u>** <sup>**(1)**</sup> **<u>(continued)</u>**





































|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tw(SCKH)|SCK high and low time|Master mode, SPI presc = 2, <br>2.7V < VDD < 3.6V|TPCLK-0.5|TPCLK|TPCLK+0.5|ns|
|tw(SCKL)|tw(SCKL)|Master mode, SPI presc = 2, <br>1.7V < VDD < 3.6V|TPCLK-2|TPCLK|TPCLK+2|TPCLK+2|
|tsu(NSS)|NSS setup time|Slave mode, SPI presc = 2|4 x TPCLK|-|-|-|
|th(NSS)|NSS hold time|Slave mode, SPI presc = 2|2 x TPCLK|2 x TPCLK|2 x TPCLK|2 x TPCLK|
|tsu(MI)|Data input setup time|Master mode|6.5|-|-|-|
|tsu(SI)|tsu(SI)|Slave mode|2.5|-|-|-|
|th(MI)|Data input hold time|Master mode|2.5|-|-|-|
|th(SI)|th(SI)|Slave mode|4|-|-|-|
|ta(SO)<br>(2)|Data output access time|Slave mode, SPI presc = 2|0|-|4 x TPCLK|4 x TPCLK|
|tdis(SO)<br>(3)|Data output disable time|Slave mode, SPI1, <br>2.7V < VDD < 3.6V|0|-|7.5|7.5|
|tdis(SO)<br>(3)|Data output disable time|Slave mode, SPI1/2/3 <br>1.7V < VDD < 3.6V|0|-|16.5|16.5|
|tv(SO)<br>th(SO)|Data output valid/hold time|Slave mode (after enable edge), <br>SPI1, 2.7V < VDD < 3.6V|-|11|13|13|
|tv(SO)<br>th(SO)|Data output valid/hold time|Slave mode (after enable edge), <br>SPI2/3, 2.7V < VDD < 3.6V|-|12|16.5|16.5|
|tv(SO)<br>th(SO)|Data output valid/hold time|Slave mode (after enable edge), <br>SPI1, 1.7V < VDD < 3.6V|-|15.5|19|19|
|tv(SO)<br>th(SO)|Data output valid/hold time|Slave mode (after enable edge), <br>SPI2/3, 1.7V < VDD < 3.6V|-|18|20.5|20.5|
|tv(MO)|Data output valid time|Master mode (after enable edge), <br>SPI1, 2.7V < VDD < 3.6V|-|-|2.5|2.5|
|tv(MO)|Data output valid time|Master mode (after enable edge), <br>SPI1/2/3, 1.7V < VDD < 3.6V|-|-|4.5|4.5|
|th(MO)|Data output hold time|Master mode (after enable edge)|0|-|-|-|


1. Evaluated by characterization - not tested in production.


2. Min time is for the minimum time to drive the output and the max time is for the maximum time to validate the data.


3. Min time is for the minimum time to invalidate the output and the max time is for the maximum time to put the data in Hi-Z.


<u>DS8626 Rev 12</u> <u>125/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 39. SPI timing diagram - slave mode and CPHA = 0**






















#### **Figure 40. SPI timing diagram - slave mode and CPHA = 1**





















<u>126/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 41. SPI timing diagram - master mode**















<u>DS8626 Rev 12</u> <u>127/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**I** <sup>**2**</sup> **S interface characteristics**
#### Unless otherwise specified, the parameters given in Table 56 for the i 2 S interface are

derived from tests performed under the ambient temperature, fPCLKx frequency and VDD
supply voltage conditions summarized in _Table 14_, with the following configuration:

      - Output speed is set to OSPEEDRy[1:0] = 10

      - Capacitive load C = 30 pF

      - Measurement points are done at CMOS levels: 0.5 VDD

Refer to _Section 6.3.16: I/O port characteristics_ for more details on the input/output alternate


function characteristics (CK, SD, WS).

#### **Table 56. I 2 S dynamic characteristics (1)**



























|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|fMCK|I2S main clock output|-|256 x<br>8K|256 x FS<br>(2)|MHz|
|fCK|I2S clock frequency|Master data: 32 bits|-|64 x FS|MHz|
|fCK|I2S clock frequency|Slave data: 32 bits|-|64 x FS|64 x FS|
|DCK|I2S clock frequency duty cycle|Slave receiver|30|70|%|
|tv(WS)|WS valid time|Master mode|0|6|ns|
|th(WS)|WS hold time|Master mode|0|-|-|
|tsu(WS)|WS setup time|Slave mode|1|-|-|
|th(WS)|WS hold time|Slave mode|0|-|-|
|tsu(SD_MR)|Data input setup time|Master receiver|7.5|-|-|
|tsu(SD_SR)|tsu(SD_SR)|Slave receiver|2|-|-|
|th(SD_MR)|Data input hold time|Master receiver|0|-|-|
|th(SD_SR)|th(SD_SR)|Slave receiver|0|-|-|
|tv(SD_ST) <br>th(SD_ST)|Data output valid time|Slave transmitter (after enable edge)|-|27|27|
|tv(SD_MT)|tv(SD_MT)|Master transmitter (after enable edge)|-|20|20|
|th(SD_MT)|Data output hold time|Master transmitter (after enable edge)|2.5|-|-|


1. Evaluated by characterization - not tested in production.

2. The maximum value of 256 x FS is 42 MHz (APB1 maximum frequency).


_Note:_ _Refer to the I_ <sup>_2_</sup> _S section of RM0090 reference manual for more details on the sampling_
_frequency (FS). fMCK, fCK, and DCK values reflect only the digital peripheral behavior. The_
_value of these parameters might be slightly impacted by the source clock accuracy. DCK_
_depends mainly on the value of ODD bit. The digital contribution leads to a minimum value_
_of I2SDIV / (2 x I2SDIV + ODD) and a maximum value of (I2SDIV + ODD) / (2 x I2SDIV +_
_ODD). FS maximum value is supported for each mode/condition._


<u>128/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 42. I 2 S slave timing diagram (Philips protocol)**


1. LSB transmit/receive of the previously transmitted byte. No LSB transmit/receive is sent before the first
byte.

#### **Figure 43. I 2 S master timing diagram (Philips protocol) (1)**


1. Evaluated by characterization - not tested in production.

2. LSB transmit/receive of the previously transmitted byte. No LSB transmit/receive is sent before the first
byte.


<u>DS8626 Rev 12</u> <u>129/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**USB OTG FS characteristics**


This interface is present in both the USB OTG HS and USB OTG FS controllers.

#### **Table 57. USB OTG FS startup time**



|Symbol|Parameter|Max|Unit|
|---|---|---|---|
|tSTARTUP<br>(1)|USB OTG FS transceiver startup time|1|µs|


1. Specified by design.




#### **Table 58. USB OTG FS DC electrical characteristics**












































|Symbol|Col2|Parameter|Conditions|Min.(1)|Typ.|Max.(1)|Unit|
|---|---|---|---|---|---|---|---|
|Input<br>levels|VDD|USB OTG FS operating<br>voltage|-|3.0(2)|-|3.6|V|
|Input<br>levels|VDI<br>(3)|Differential input sensitivity|I(USB_FS_DP/DM,<br>USB_HS_DP/DM)|0.2|-|-|V|
|Input<br>levels|VCM<br>(3)|Differential common mode<br>range|Includes VDIrange|0.8|-|2.5|2.5|
|Input<br>levels|VSE<br>(3)|Single ended receiver<br>threshold|-|1.3|-|2.0|2.0|
|Output<br>levels|VOL|Static output level low|RL of 1.5 kΩ to 3.6 V(4)|-|-|0.3|V|
|Output<br>levels|VOH|Static output level high|RL of 15 kΩ to VSS<br>(4)|2.8|-|3.6|3.6|
|RPD|RPD|PA11, PA12, PB14, PB15<br>(USB_FS_DP/DM,<br>USB_HS_DP/DM)|VIN = VDD|17|21|24|kΩ|
|RPD|RPD|PA9, PB13<br>(OTG_FS_VBUS,<br>OTG_HS_VBUS)|PA9, PB13<br>(OTG_FS_VBUS,<br>OTG_HS_VBUS)|0.65|1.1|2.0|2.0|
|RPU|RPU|PA12, PB15 (USB_FS_DP,<br>USB_HS_DP)|VIN = VSS|1.5|1.8|2.1|2.1|
|RPU|RPU|PA9, PB13<br>(OTG_FS_VBUS,<br>OTG_HS_VBUS)|VIN = VSS|0.25|0.37|0.55|0.55|



1. All the voltages are measured from the local ground potential.


2. The STM32F405xx and STM32F407xx USB OTG FS functionality is ensured down to 2.7 V but not the full
USB OTG FS electrical characteristics which are degraded in the 2.7-to-3.0 V VDD voltage range.

3. Specified by design.

4. RL is the load connected on the USB OTG FS drivers


<u>130/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 44. USB OTG FS timings: definition of data signal rise and fall time**


|Col1|Col2|Col3|
|---|---|---|
||||







|Table 59. USB OTG FS electrical characteristics(1)|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Driver characteristics**|**Driver characteristics**|**Driver characteristics**|**Driver characteristics**|**Driver characteristics**|**Driver characteristics**|
|**Symbol**|**Parameter**|**Conditions**|**Min**|**Max**|**Unit**|
|tr|Rise time(2)|CL = 50 pF|4|20|ns|
|tf|Fall time(2)|CL = 50 pF|4|20|ns|
|trfm|Rise/ fall time matching|tr/tf|90|110|%|
|VCRS|Output signal crossover voltage|-|1.3|2.0|V|


1. Specified by design.

2. Measured from 10% to 90% of the data signal. For more detailed informations, please refer to USB
Specification - Chapter 7 (version 2.0).


**USB HS characteristics**


Unless otherwise specified, the parameters given in _Table 62_ for ULPI are derived from
#### tests performed under the ambient temperature, fHCLK frequency summarized in Table 61 and VDD supply voltage conditions summarized in Table 60, with the following configuration:

- Output speed is set to OSPEEDRy[1:0] = 10

- Capacitive load C = 30 pF

- Measurement points are done at CMOS levels: 0.5VDD.

Refer to Section _Section 6.3.16: I/O port characteristics_ for more details on the input/output
characteristics.

#### **Table 60. USB HS DC electrical characteristics**







|Symbol|Col2|Parameter|Min.(1)|Max.(1)|Unit|
|---|---|---|---|---|---|
|Input level|VDD|USB OTG HS operating voltage|2.7|3.6|V|


1. All the voltages are measured from the local ground potential.

#### **Table 61. USB HS clock timing parameters (1)**

|Parameter|Col2|Symbol|Min|Nominal|Max|Unit|
|---|---|---|---|---|---|---|
|fHCLK value to guarantee proper operation of<br>USB HS interface|fHCLK value to guarantee proper operation of<br>USB HS interface|-|30|-|-|MHz|
|Frequency (first transition)|8-bit ±10%|FSTART_8BIT|54|60|66|MHz|



<u>DS8626 Rev 12</u> <u>131/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 61. USB HS clock timing parameters</u>** <sup>**(1)**</sup>







|Parameter|Col2|Symbol|Min|Nominal|Max|Unit|
|---|---|---|---|---|---|---|
|Frequency (steady state) ±500 ppm|Frequency (steady state) ±500 ppm|FSTEADY|59.97|60|60.03|MHz|
|Duty cycle (first transition)|8-bit ±10%|DSTART_8BIT|40|50|60|%|
|Duty cycle (steady state) ±500 ppm|Duty cycle (steady state) ±500 ppm|DSTEADY|49.975|50|50.025|%|
|Time to reach the steady state frequency and<br>duty cycle after the first transition|Time to reach the steady state frequency and<br>duty cycle after the first transition|TSTEADY|-|-|1.4|ms|
|Clock startup time after the<br>de-assertion of SuspendM|Peripheral|TSTART_DEV|-|-|5.6|ms|
|Clock startup time after the<br>de-assertion of SuspendM|Host|TSTART_HOST|-|-|-|-|
|PHY preparation time after the first transition<br>of the input clock|PHY preparation time after the first transition<br>of the input clock|TPREP|-|-|-|µs|


1. Specified by design.

#### **Table 62. ULPI timing**













|Parameter|Symbol|Value(1)|Col4|Unit|
|---|---|---|---|---|
|**Parameter**|**Symbol**|**Min.**|**Max.**|**Max.**|
|Control in (ULPI_DIR) setup time|tSC|-|2.0|ns|
|Control in (ULPI_NXT) setup time|Control in (ULPI_NXT) setup time|-|1.5|1.5|
|Control in (ULPI_DIR, ULPI_NXT) hold time|tHC|0|-|-|
|Data in setup time|tSD|-|2.0|2.0|
|Data in hold time|tHD|0|-|-|
|Control out (ULPI_STP) setup time and hold time|tDC|-|9.2|9.2|
|Data out available from clock rising edge|tDD|-|10.7|10.7|


1. VDD = 2.7 V to 3.6 V and TA = –40 to 85 °C.

#### **Figure 45. ULPI timing diagram**















<u>132/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**Ethernet characteristics**

#### Unless otherwise specified, the parameters given in Table 64, Table 65 and Table 66 for

SMI, RMII and MII are derived from tests performed under the ambient temperature, fHCLK
frequency summarized in _Table 14_ and VDD supply voltage conditions summarized in
#### Table 63, with the following configuration:

      - Output speed is set to OSPEEDRy[1:0] = 10

      - Capacitive load C = 30 pF

      - Measurement points are done at CMOS levels: 0.5VDD.

Refer to _Section 6.3.16: I/O port characteristics_ for more details on the input/output
characteristics.

#### **Table 63. Ethernet DC electrical characteristics**







|Symbol|Col2|Parameter|Min.(1)|Max.(1)|Unit|
|---|---|---|---|---|---|
|Input level|VDD|Ethernet operating voltage|2.7|3.6|V|


1. All the voltages are measured from the local ground potential.

#### Table 64 gives the list of Ethernet MAC signals for the SMI (station management interface) and Figure 46 shows the corresponding timing diagram. **Figure 46. Ethernet SMI timing diagram** **Table 64. Dynamic characteristics: Ethernet MAC signals for SMI (1)**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tMDC|MDC cycle time(2.38 MHz)|411|420|425|ns|
|Td(MDIO)|Write data valid time|6|10|13|13|
|tsu(MDIO)|Read data setup time|12|-|-|-|
|th(MDIO)|Read data hold time|0|-|-|-|



1. Evaluated by characterization - not tested in production.


_Table 65_ gives the list of Ethernet MAC signals for the RMII and _Figure 47_ shows the
corresponding timing diagram.


<u>DS8626 Rev 12</u> <u>133/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 47. Ethernet RMII timing diagram**






#### **Table 65. Dynamic characteristics: Ethernet MAC signals for RMII**





|Symbol|Rating|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tsu(RXD)|Receive data setup time|2|-|-|ns|
|tih(RXD)|Receive data hold time|1|-|-|ns|
|tsu(CRS)|Carrier sense set-up time|0.5|-|-|ns|
|tih(CRS)|Carrier sense hold time|2|-|-|ns|
|td(TXEN)|Transmit enable valid delay time|8|9.5|11|ns|
|td(TXD)|Transmit data valid delay time|8.5|10|11.5|ns|

#### Table 66 gives the list of Ethernet MAC signals for MII and Figure 47 shows the

corresponding timing diagram.

#### **Figure 48. Ethernet MII timing diagram**


<u>134/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 66. Dynamic characteristics: Ethernet MAC signals for MII (1)**



|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tsu(RXD)|Receive data setup time|9|-|-|ns|
|tih(RXD)|Receive data hold time|10|-|-|-|
|tsu(DV)|Data valid setup time|9|-|-|-|
|tih(DV)|Data valid hold time|8|-|-|-|
|tsu(ER)|Error setup time|6|-|-|-|
|tih(ER)|Error hold time|8|-|-|-|
|td(TXEN)|Transmit enable valid delay time|0|10|14|14|
|td(TXD)|Transmit data valid delay time|0|10|15|15|


1. Evaluated by characterization - not tested in production.

### **6.3.20 CAN (controller area network) interface**





Refer to _Section 6.3.16: I/O port characteristics_ for more details on the input/output alternate
function characteristics (CANTX and CANRX).

### **6.3.21 12-bit ADC characteristics**

#### Unless otherwise specified, the parameters given in Table 67 are derived from tests

performed under the ambient temperature, fPCLK2 frequency and VDDA supply voltage
conditions summarized in _Table 14_ .

#### **Table 67. ADC characteristics**















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDDA|Power supply|-|1.8(1)|-|3.6|V|
|VREF+|Positive reference voltage|-|1.8(1)(2)(3)|-|VDDA|VDDA|
|VREF−|Negative reference voltage|-|-|0|-|-|
|fADC|ADC clock frequency|VDDA = 1.8(1)(3) to<br>2.4 V|0.6|15|18|MHz|
|fADC|ADC clock frequency|VDDA = 2.4 to 3.6 V(3)|0.6|30|36|MHz|
|fTRIG<br>(4)|External trigger frequency|fADC = 30 MHz,<br>12-bit resolution|-|-|1764|kHz|
|fTRIG<br>(4)|External trigger frequency|-|-|-|17|1/fADC|
|VAIN|Conversion voltage range(5)|-|0 (VSSAor VREF- <br>tied to ground)|-|VREF+|V|
|RAIN<br>(4)<br>|External input impedance<br>|See_Equation 1_ for<br>details|-|-|50|κΩ|
|RADC<br>(4)(6)|Sampling switch resistance|-|-|-|6|κΩ|
|CADC<br>(4)|Internal sample and hold<br>capacitor|-|-|4|-|pF|


<u>DS8626 Rev 12</u> <u>135/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 67. ADC characteristics (continued)</u>**






























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tlat<br>(4)|Injection trigger conversion<br>latency|fADC = 30 MHz|-|-|0.100|µs|
|tlat<br>(4)|Injection trigger conversion<br>latency||-|-|3(7)|1/fADC|
|tlatr<br>(4)|Regular trigger conversion<br>latency|fADC = 30 MHz|-|-|0.067|µs|
|tlatr<br>(4)|Regular trigger conversion<br>latency||-|-|2(7)|1/fADC|
|tS<br>(4)|Sampling time|fADC = 30 MHz|0.100|-|16|µs|
|tS<br>(4)|Sampling time|-|3|-|480|1/fADC|
|tSTAB<br>(4)|Power-up time|-|-|2|3|µs|
|tCONV<br>(4)|Total conversion time (including<br>sampling time)|fADC = 30 MHz<br>12-bit resolution|0.50|-|16.40|µs|
|tCONV<br>(4)|Total conversion time (including<br>sampling time)|fADC = 30 MHz<br>10-bit resolution|0.43|-|16.34|µs|
|tCONV<br>(4)|Total conversion time (including<br>sampling time)|fADC = 30 MHz<br>8-bit resolution|0.37|-|16.27|µs|
|tCONV<br>(4)|Total conversion time (including<br>sampling time)|fADC = 30 MHz<br>6-bit resolution|0.30|-|16.20|µs|
|tCONV<br>(4)|Total conversion time (including<br>sampling time)|9 to 492 (tS for sampling +n-bit resolution for successive<br>approximation)|9 to 492 (tS for sampling +n-bit resolution for successive<br>approximation)|9 to 492 (tS for sampling +n-bit resolution for successive<br>approximation)|9 to 492 (tS for sampling +n-bit resolution for successive<br>approximation)|1/fADC|
|fS<br>(4)|Sampling rate<br>(fADC = 30 MHz, and <br>tS = 3 ADC cycles)|12-bit resolution<br>Single ADC|-|-|2|Msps|
|fS<br>(4)|Sampling rate<br>(fADC = 30 MHz, and <br>tS = 3 ADC cycles)|12-bit resolution<br>Interleave Dual ADC<br>mode|-|-|3.75|Msps|
|fS<br>(4)|Sampling rate<br>(fADC = 30 MHz, and <br>tS = 3 ADC cycles)|12-bit resolution<br>Interleave Triple ADC<br>mode|-|-|6|Msps|
|IVREF+<br>(4)|ADC VREF DC current<br>consumption in conversion<br>mode|-|-|300|500|µA|
|IVDDA<br>(4)|ADC VDDA DC current<br>consumption in conversion<br>mode|-|-|1.6|1.8|mA|



1. VDD/VDDA minimum value of 1.7 V is obtained when the device operates in reduced temperature range, and with the use of
an external power supply supervisor (refer to _Section 3.15.2: Internal reset OFF_ ).

2. It is recommended to maintain the voltage difference between VREF+ and VDDA below 1.8 V.

3. VDDA -VREF+ < 1.2 V.

4. Evaluated by characterization - not tested in production.

5. VREF+ is internally connected to VDDA and VREF- is internally connected to VSSA.

6. RADC maximum value is given for VDD=1.8 V, and minimum value for VDD=3.3 V.

7. For external triggers, a delay of 1/fPCLK2 must be added to the latency specified in _Table 67_ .


<u>136/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**Equation 1: RAIN max formula**

( k                               - 0.5 )
RAIN = ----------------------------------------------------------------                  - RADC

N + 2
fADC × CADC × ln ( 2 )


The formula above ( _Equation 1_ ) is used to determine the maximum external impedance
allowed for an error below 1/4 of LSB. N = 12 (from 12-bit resolution) and k is the number of
sampling periods defined in the ADC_SMPR1 register.



a


#### **Table 68. ADC accuracy at fADC = 30 MHz**

















|Symbol|Parameter|Test conditions|Typ|Max(1)|Unit|
|---|---|---|---|---|---|
|ET|Total unadjusted error|fPCLK2 = 60 MHz, <br>fADC = 30 MHz, RAIN < 10 kΩ, <br>VDDA = 1.8(2) to 3.6 V|±2|±5|LSB|
|EO|Offset error|Offset error|±1.5|±2.5|±2.5|
|EG|Gain error|Gain error|±1.5|±3|±3|
|ED|Differential linearity error|Differential linearity error|±1|±2|±2|
|EL|Integral linearity error|Integral linearity error|±1.5|±3|±3|


1. Evaluated by characterization - not tested in production.

2. VDD/VDDA minimum value of 1.7 V is obtained when the device operates in reduced temperature range,
and with the use of an external power supply supervisor (refer to _Section 3.15.2: Internal reset OFF_ ).


_Note:_ _ADC accuracy vs. negative injection current: injecting a negative current on any analog_
_input pins should be avoided as this significantly reduces the accuracy of the conversion_
_being performed on another analog input. It is recommended to add a Schottky diode (pin to_
_ground) to analog pins which may potentially inject negative currents._
_Any positive injection current within the limits specified for IINJ(PIN) and SIINJ(PIN) in_
_Section 6.3.16 does not affect the ADC accuracy._

#### **Figure 49. ADC accuracy characteristics**





























<u>DS8626 Rev 12</u> <u>137/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**





























1. Refer to _Table 67: ADC characteristics_ for the values of RAIN, RADC and CADC.

2. Cparasitic represents the capacitance of the PCB (dependent on soldering and PCB layout quality) plus the
pad capacitance (refer to _Table 48: I/O static characteristics_ ) A high Cparasitic value downgrades conversion
accuracy. To remedy this, fADC should be reduced.

3. Refer to _Table 48: I/O static characteristics_ .

4. Refer to _Figure 21: Power supply scheme_ .


<u>138/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**General PCB design guidelines**

#### Power supply decoupling should be performed as shown in Figure 51 or Figure 52,

depending on whether VREF+ is connected to VDDA or not. The 10 nF capacitors should be
ceramic (good quality). They should be placed them as close as possible to the chip.







1. VREF+ and VREF– inputs are both available on UFBGA176. VREF+ is also available on LQFP100, LQFP144,
and LQFP176. When VREF+ and VREF– are not available, they are internally connected to VDDA and VSSA.


<u>DS8626 Rev 12</u> <u>139/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**











1. VREF+ and VREF– inputs are both available on UFBGA176. VREF+ is also available on LQFP100, LQFP144,
and LQFP176. When VREF+ and VREF– are not available, they are internally connected to VDDA and VSSA.

### **6.3.22 Temperature sensor characteristics**

#### **Table 69. Temperature sensor characteristics**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|TL<br>(1)|VSENSE linearity with temperature|-|±1|±2|°C|
|Avg_Slope(1)|Average slope|-|2.5|-|mV/°C|
|V25<br>(1)|Voltage at 25 °C|-|0.76|-|V|
|tSTART<br>(2)|Startup time|-|6|10|µs|
|TS_temp<br>(2)|ADC sampling time when reading the temperature (1 °C accuracy)|10|-|-|µs|



1. Evaluated by characterization - not tested in production.


2. Specified by design.

#### **Table 70. Temperature sensor calibration values**

|Symbol|Parameter|Memory address|
|---|---|---|
|TS_CAL1|TS ADC raw data acquired at temperature of 30 °C, VDDA=3.3 V|0x1FFF 7A2C - 0x1FFF 7A2D|
|TS_CAL2|TS ADC raw data acquired at temperature of 110 °C, VDDA=3.3 V|0x1FFF 7A2E - 0x1FFF 7A2F|



<u>140/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

### **6.3.23 VBAT monitoring characteristics**

#### **Table 71. VBAT monitoring characteristics**




|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|R|Resistor bridge for VBAT|-|50|-|KΩ|
|Q|Ratio on VBAT measurement|-|2|-|-|
|Er(1)|Error on Q|–1|-|+1|%|
|TS_vbat<br>(2)(2)|ADC sampling time when reading the VBAT <br>1 mV accuracy|5|-|-|µs|



1. Specified by design.


2. Shortest sampling time can be determined in the application by multiple iterations.

### **6.3.24 Embedded reference voltage**

#### The parameters given in Table 72 are derived from tests performed under ambient

temperature and VDD supply voltage conditions summarized in _Table 14_ .

#### **Table 72. Embedded internal reference voltage**











|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VREFINT|Internal reference voltage|–40 °C < TA < +105 °C|1.18|1.21|1.24|V|
|TS_vrefint<br>(1)|ADC sampling time when reading the<br>internal reference voltage|-|10|-|-|µs|
|VRERINT_s<br>(2)|Internal reference voltage spread over the<br>temperature range|VDD = 3 V|-|3|5|mV|
|TCoeff<br>(2)|Temperature coefficient|-|-|30|50|ppm/°C|
|tSTART<br>(2)|Startup time|-|-|6|10|µs|


1. Shortest sampling time can be determined in the application by multiple iterations.


2. Specified by design.

#### **Table 73. Internal reference voltage calibration values**

|Symbol|Parameter|Memory address|
|---|---|---|
|VREFIN_CAL|Raw data acquired at temperature of 30 °C, VDDA=3.3 V|0x1FFF 7A2A - 0x1FFF 7A2B|


### **6.3.25 DAC electrical characteristics**

#### **Table 74. DAC characteristics**

|Symbol|Parameter|Min|Typ|Max|Unit|Comments|
|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage|1.8(1)|-|3.6|V|-|
|VREF+|Reference supply voltage|1.8(1)|-|3.6|V|VREF+ ≤ VDDA|
|VSSA|Ground|0|-|0|V|-|



<u>DS8626 Rev 12</u> <u>141/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 74. DAC characteristics (continued)</u>**


















































|Symbol|Parameter|Min|Typ|Max|Unit|Comments|
|---|---|---|---|---|---|---|
|RLOAD<br>(2)|Resistive load with buffer<br>ON|5|-|-|kΩ|-|
|RO<br>(2)|Impedance output with<br>buffer OFF|-|-|15|kΩ|When the buffer is OFF, the<br>Minimum resistive load between<br>DAC_OUT and VSS to have a 1%<br>accuracy is 1.5 MΩ|
|CLOAD<br>(2)|Capacitive load|-|-|50|pF|Maximum capacitive load at<br>DAC_OUT pin (when the buffer is<br>ON).|
|DAC_OUT<br>min(2)|Lower DAC_OUT voltage<br>with buffer ON|0.2|-|-|V|It gives the maximum output<br>excursion of the DAC.<br>It corresponds to 12-bit input code<br>(0x0E0) to (0xF1C) at VREF+ =<br>3.6 V and (0x1C7) to (0xE38) at<br>VREF+ = 1.8 V|
|DAC_OUT<br>max(2)|Higher DAC_OUT voltage<br>with buffer ON|-|-|VDDA – 0.2|V|V|
|DAC_OUT<br>min(2)|Lower DAC_OUT voltage<br>with buffer OFF|-|0.5|-|mV|It gives the maximum output<br>excursion of the DAC.|
|DAC_OUT<br>max(2)|Higher DAC_OUT voltage<br>with buffer OFF|-|-|VREF+ – 1LSB|V|V|
|IVREF+<br>(4)|DAC DC VREF current<br>consumption in quiescent<br>mode (Standby mode)|-|170|240|µA|With no load, worst code (0x800)<br>at VREF+ = 3.6 V in terms of DC<br>consumption on the inputs|
|IVREF+<br>(4)|DAC DC VREF current<br>consumption in quiescent<br>mode (Standby mode)|-|50|75|75|With no load, worst code (0xF1C)<br>at VREF+ = 3.6 V in terms of DC<br>consumption on the inputs|
|IDDA<br>(4)|DAC DC VDDA current<br>consumption in quiescent<br>mode(3)|-|280|380|µA|With no load, middle code (0x800)<br>on the inputs|
|IDDA<br>(4)|DAC DC VDDA current<br>consumption in quiescent<br>mode(3)|-|475|625|µA|With no load, worst code (0xF1C)<br>at VREF+ = 3.6 V in terms of DC<br>consumption on the inputs|
|DNL(4)|Differential non linearity<br>Difference between two<br>consecutive code-1LSB)|-|-|±0.5|LSB|Given for the DAC in 10-bit<br>configuration.|
|DNL(4)|Differential non linearity<br>Difference between two<br>consecutive code-1LSB)|-|-|±2|LSB|Given for the DAC in 12-bit<br>configuration.|
|INL(4)|Integral non linearity<br>(difference between<br>measured value at Code i<br>and the value at Code i on a<br>line drawn between Code 0<br>and last Code 1023)|-|-|±1|LSB|Given for the DAC in 10-bit<br>configuration.|
|INL(4)|Integral non linearity<br>(difference between<br>measured value at Code i<br>and the value at Code i on a<br>line drawn between Code 0<br>and last Code 1023)|-|-|±4|LSB|Given for the DAC in 12-bit<br>configuration.|



<u>142/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**<u>Table 74. DAC characteristics (continued)</u>**
































|Symbol|Parameter|Min|Typ|Max|Unit|Comments|
|---|---|---|---|---|---|---|
|Offset(4)|Offset error<br>(difference between<br>measured value at Code<br>(0x800) and the ideal value<br>= VREF+/2)|-|-|±10|mV|Given for the DAC in 12-bit<br>configuration|
|Offset(4)|Offset error<br>(difference between<br>measured value at Code<br>(0x800) and the ideal value<br>= VREF+/2)|-|-|±3|LSB|Given for the DAC in 10-bit at<br>VREF+ = 3.6 V|
|Offset(4)|Offset error<br>(difference between<br>measured value at Code<br>(0x800) and the ideal value<br>= VREF+/2)|-|-|±12|LSB|Given for the DAC in 12-bit at<br>VREF+ = 3.6 V|
|Gain<br>error(4)|Gain error|-|-|±0.5|%|Given for the DAC in 12-bit<br>configuration|
|tSETTLING<br>(4)|Settling time (full scale: for a<br>10-bit input code transition<br>between the lowest and the<br>highest input codes when<br>DAC_OUT reaches final<br>value ±4LSB|-|3|6|µs|CLOAD ≤  50 pF, <br>RLOAD ≥ 5 kΩ|
|THD(4)|Total Harmonic Distortion<br>Buffer ON|-|-|-|dB|CLOAD ≤  50 pF, <br>RLOAD ≥ 5 kΩ|
|Update<br>rate(2)|Max frequency for a correct<br>DAC_OUT change when<br>small variation in the input<br>code (from code i to i+1LSB)|-|-|1|MS/s|CLOAD ≤  50 pF, <br>RLOAD ≥ 5 kΩ|
|tWAKEUP<br>(4)|Wakeup time from off state<br>(Setting the ENx bit in the<br>DAC Control register)|-|6.5|10|µs|CLOAD ≤  50 pF, RLOAD ≥ 5 kΩ<br>input code between lowest and<br>highest possible ones.|
|PSRR+(2)|Power supply rejection ratio<br>(to VDDA) (static DC<br>measurement)|-|–67|–40|dB|No RLOAD, CLOAD = 50 pF|



1. VDD/VDDA minimum value of 1.7 V is obtained when the device operates in reduced temperature range, and with the use of
an external power supply supervisor (refer to _Section 3.15.2: Internal reset OFF_ ).


2. Specified by design.


3. The quiescent mode corresponds to a state where the DAC maintains a stable output level to ensure that no dynamic
consumption occurs.


4. Evaluated by characterization - not tested in production.


<u>DS8626 Rev 12</u> <u>143/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 53. 12-bit buffered /non-buffered DAC**











1. The DAC integrates an output buffer that can be used to reduce the output impedance and to drive external
loads directly without the use of an external operational amplifier. The buffer can be bypassed by
configuring the BOFFx bit in the DAC_CR register.

### **6.3.26 FSMC characteristics**


Unless otherwise specified, the parameters given in _Table 75_ to _Table 86_ for the FSMC
interface are derived from tests performed under the ambient temperature, fHCLK frequency
and VDD supply voltage conditions summarized in _Table 14_, with the following configuration:

      - Output speed is set to OSPEEDRy[1:0] = 10

      - Capacitive load C = 30 pF

      - Measurement points are done at CMOS levels: 0.5VDD

Refer to Section _Section 6.3.16: I/O port characteristics_ for more details on the input/output
characteristics.


**Asynchronous waveforms and timings**


_Figure 54_ through _Figure 57_ represent asynchronous waveforms and _Table 75_ through
_Table 78_ provide the corresponding timings. The results shown in these tables are obtained
with the following FSMC configuration:

      - AddressSetupTime = 1

      - AddressHoldTime = 0x1

      - DataSetupTime = 0x1

      - BusTurnAroundDuration = 0x0


In all timing tables, the THCLK is the HCLK clock period.


<u>144/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 54. Asynchronous non-multiplexed SRAM/PSRAM/NOR read waveforms**



|tw(NOE)|Col2|Col3|Col4|
|---|---|---|---|
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||


1. Mode 2/B, C and D only. In Mode 1, FSMC_NADV is not used.








#### **Table 75. Asynchronous non-multiplexed SRAM/PSRAM/NOR read timings (1)(2)**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FSMC_NE low time|2THCLK–0.5|2 THCLK+1|ns|
|tv(NOE_NE)|FSMC_NEx low to FSMC_NOE low|0.5|3|ns|
|tw(NOE)|FSMC_NOE low time|2THCLK–2|2THCLK+ 2|ns|
|th(NE_NOE)|FSMC_NOE high to FSMC_NE high hold time|0|-|ns|
|tv(A_NE)|FSMC_NEx low to FSMC_A valid|-|4.5|ns|
|th(A_NOE)|Address hold time after FSMC_NOE high|4|-|ns|
|tv(BL_NE)|FSMC_NEx low to FSMC_BL valid|-|1.5|ns|
|th(BL_NOE)|FSMC_BL hold time after FSMC_NOE high|0|-|ns|
|tsu(Data_NE)|Data to FSMC_NEx high setup time|THCLK+4|-|ns|
|tsu(Data_NOE)|Data to FSMC_NOEx high setup time|THCLK+4|-|ns|
|th(Data_NOE)|Data hold time after FSMC_NOE high|0|-|ns|
|th(Data_NE)|Data hold time after FSMC_NEx high|0|-|ns|
|tv(NADV_NE)|FSMC_NEx low to FSMC_NADV low|-|2|ns|
|tw(NADV)|FSMC_NADV low time|-|THCLK|ns|



1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.


<u>DS8626 Rev 12</u> <u>145/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 55. Asynchronous non-multiplexed SRAM/PSRAM/NOR write waveforms**












|Col1|Col2|
|---|---|
|Address||
|Address||
|Address||
|Address||
|Address||





1. Mode 2/B, C and D only. In Mode 1, FSMC_NADV is not used.

#### **Table 76. Asynchronous non-multiplexed SRAM/PSRAM/NOR write timings (1)(2)**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FSMC_NE low time|3THCLK|3THCLK+ 4|ns|
|tv(NWE_NE)|FSMC_NEx low to FSMC_NWE low|THCLK–0.5|THCLK+0.5|ns|
|tw(NWE)|FSMC_NWE low time|THCLK–1|THCLK+2|ns|
|th(NE_NWE)|FSMC_NWE high to FSMC_NE high hold time|THCLK–1|-|ns|
|tv(A_NE)|FSMC_NEx low to FSMC_A valid|-|0|ns|
|th(A_NWE)|Address hold time after FSMC_NWE high|THCLK– 2|-|ns|
|tv(BL_NE)|FSMC_NEx low to FSMC_BL valid|-|1.5|ns|
|th(BL_NWE)|FSMC_BL hold time after FSMC_NWE high|THCLK– 1|-|ns|
|tv(Data_NE)|Data to FSMC_NEx low to Data valid|-|THCLK+3|ns|
|th(Data_NWE)|Data hold time after FSMC_NWE high|THCLK–1|-|ns|
|tv(NADV_NE)|FSMC_NEx low to FSMC_NADV low|-|2|ns|
|tw(NADV)|FSMC_NADV low time|-|THCLK+0.5|ns|



1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.


<u>146/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 56. Asynchronous multiplexed PSRAM/NOR read waveforms**












|tv(NOE_NE) t h(NE_NOE)<br>t w(NOE)|Col2|Col3|Col4|
|---|---|---|---|
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|||
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|||
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|||
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|Address|||
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|Address|||
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|Address|||
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|Address|||
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|Address|||
|t w(NOE)<br>tv(NOE_NE)<br>t h(NE_NOE)|Address|||














#### **Table 77. Asynchronous multiplexed PSRAM/NOR read timings (1)(2)**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FSMC_NE low time|3THCLK–1|3THCLK+1|ns|
|tv(NOE_NE)|FSMC_NEx low to FSMC_NOE low|2THCLK–0.5|2THCLK+0.5|ns|
|tw(NOE)|FSMC_NOE low time|THCLK–1|THCLK+1|ns|
|th(NE_NOE)|FSMC_NOE high to FSMC_NE high hold time|0|-|ns|
|tv(A_NE)|FSMC_NEx low to FSMC_A valid|-|3|ns|
|tv(NADV_NE)|FSMC_NEx low to FSMC_NADV low|1|2|ns|
|tw(NADV)|FSMC_NADV low time|THCLK– 2|THCLK+1|ns|
|th(AD_NADV)|FSMC_AD(adress) valid hold time after FSMC_NADV high)|THCLK|-|ns|
|th(A_NOE)|Address hold time after FSMC_NOE high|THCLK–1|-|ns|
|th(BL_NOE)|FSMC_BL time after FSMC_NOE high|0|-|ns|
|tv(BL_NE)|FSMC_NEx low to FSMC_BL valid|-|2|ns|
|tsu(Data_NE)|Data to FSMC_NEx high setup time|THCLK+4|-|ns|
|tsu(Data_NOE)|Data to FSMC_NOE high setup time|THCLK+4|-|ns|
|th(Data_NE)|Data hold time after FSMC_NEx high|0|-|ns|
|th(Data_NOE)|Data hold time after FSMC_NOE high|0|-|ns|



1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.


<u>DS8626 Rev 12</u> <u>147/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 57. Asynchronous multiplexed PSRAM/NOR write waveforms**


























#### **Table 78. Asynchronous multiplexed PSRAM/NOR write timings (1)(2)**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FSMC_NE low time|4THCLK–0.5|4THCLK+3|ns|
|tv(NWE_NE)|FSMC_NEx low to FSMC_NWE low|THCLK–0.5|THCLK -0.5|ns|
|tw(NWE)|FSMC_NWE low tim e|2THCLK–0.5|2THCLK+3|ns|
|th(NE_NWE)|FSMC_NWE high to FSMC_NE high hold time|THCLK|-|ns|
|tv(A_NE)|FSMC_NEx low to FSMC_A valid|-|0|ns|
|tv(NADV_NE)|FSMC_NEx low to FSMC_NADV low|1|2|ns|
|tw(NADV)|FSMC_NADV low time|THCLK– 2|THCLK+ 1|ns|
|th(AD_NADV)|FSMC_AD(address) valid hold time after<br>FSMC_NADV high)|THCLK–2|-|ns|
|th(A_NWE)|Address hold time after FSMC_NWE high|THCLK|-|ns|
|th(BL_NWE)|FSMC_BL hold time after FSMC_NWE high|THCLK–2|-|ns|
|tv(BL_NE)|FSMC_NEx low to FSMC_BL valid|-|1.5|ns|
|tv(Data_NADV)|FSMC_NADV high to Data valid|-|THCLK–0.5|ns|
|th(Data_NWE)|Data hold time after FSMC_NWE high|THCLK|-|ns|


1. CL = 30 pF.


<u>148/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


2. Evaluated by characterization - not tested in production.


**Synchronous waveforms and timings**

#### Figure 58 through Figure 61 represent synchronous waveforms and Table 80 through

_Table 82_ provide the corresponding timings. The results shown in these tables are obtained
with the following FSMC configuration:

      - BurstAccessMode = FSMC_BurstAccessMode_Enable;

      - MemoryType = FSMC_MemoryType_CRAM;

      - WriteBurst = FSMC_WriteBurst_Enable;

      - CLKDivision = 1; (0 is not supported, see the STM32F40xxx/41xxx reference manual)

      - DataLatency = 1 for NOR flash; DataLatency = 0 for PSRAM


In all timing tables, the THCLK is the HCLK clock period (with maximum
FSMC_CLK = 60 MHz).

#### **Figure 58. Synchronous multiplexed NOR/PSRAM read timings**

























|td(CL<br>td(CL|Da<br>KL-NExL)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|td(CL<br>td(CL|Da<br>KL-NExL)|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|
|td(CL<br>td(CL|KL-AV)<br>td(CL|KL-NADVH)|||||
|td(CL<br>td(CL|KL-AV)<br>td(CL||||td(CLKL-A|IV)|
|td(CL<br>td(CL|||||||
|td(CL<br>td(CL|||EL)|td(|CLKL-NOE|H)<br>KH-AD|
|AD<br>td(CLKL|-ADIV)<br>tsu(A|-ADIV)<br>tsu(A|-ADIV)<br>tsu(A|-ADIV)<br>tsu(A|-ADIV)<br>tsu(A|-ADIV)<br>tsu(A|
|AD<br>td(CLKL|-ADIV)<br>tsu(A|-ADIV)<br>tsu(A|-ADIV)<br>tsu(A|-ADIV)<br>tsu(A|2<br>th(CL<br>ITV)|2<br>th(CL<br>ITV)|
|AD<br>td(CLKL|-ADIV)<br>tsu(A|D|D|D|D|D|
|AD<br>td(CLKL|[15:0]||||||
|AD<br>td(CLKL|tsu(NWAI|tsu(NWAI|tsu(NWAI|tsu(NWAI|tsu(NWAI||
||||||||
|L + 0b)|||||||
||||||||


|Col1|KH)|
|---|---|
|V-CL|V-CL|
|||


<u>DS8626 Rev 12</u> <u>149/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Table 79. Synchronous multiplexed NOR/PSRAM read timings (1)(2)**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FSMC_CLK period|2THCLK|-|ns|
|td(CLKL-NExL)|FSMC_CLK low to FSMC_NEx low (x=0..2)|-|0|ns|
|td(CLKL-NExH)|FSMC_CLK low to FSMC_NEx high (x= 0…2)|2|-|ns|
|td(CLKL-NADVL)|FSMC_CLK low to FSMC_NADV low|-|2|ns|
|td(CLKL-NADVH)|FSMC_CLK low to FSMC_NADV high|2|-|ns|
|td(CLKL-AV)|FSMC_CLK low to FSMC_Ax valid (x=16…25)|-|0|ns|
|td(CLKL-AIV)|FSMC_CLK low to FSMC_Ax invalid (x=16…25)|0|-|ns|
|td(CLKL-NOEL)|FSMC_CLK low to FSMC_NOE low|-|0|ns|
|td(CLKL-NOEH)|FSMC_CLK low to FSMC_NOE high|2|-|ns|
|td(CLKL-ADV)|FSMC_CLK low to FSMC_AD[15:0] valid|-|4.5|ns|
|td(CLKL-ADIV)|FSMC_CLK low to FSMC_AD[15:0] invalid|0|-|ns|
|tsu(ADV-CLKH)|FSMC_A/D[15:0] valid data before FSMC_CLK high|6|-|ns|
|th(CLKH-ADV)|FSMC_A/D[15:0] valid data after FSMC_CLK high|0|-|ns|
|tsu(NWAIT-CLKH)|FSMC_NWAIT valid before FSMC_CLK high|4|-|ns|
|th(CLKH-NWAIT)|FSMC_NWAIT valid after FSMC_CLK high|0|-|ns|



1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.


<u>150/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 59. Synchronous multiplexed PSRAM write timings**
























|td(CL<br>td(CL<br>td(CL<br>td(CLKL<br>AD|Da<br>KL-NExL)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|Da<br>KL-NExL)|ta latency =|0|0|0|0|0|0|0|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|Da<br>KL-NExL)|ta latency =|0|0|0|0|0|0||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|KL-AV)<br>td(CL|KL-NADVH|)|)||||||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|KL-AV)<br>td(CL||||||td(CLKL-AI|V)|V)|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL||||||||||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|KL-NWEL)|||||td|(CLKL-NWE|H)|H)|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|KL-NWEL)|||||td|(CLKL-NWE|H)||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|KL-NWEL)||||d(CLKL-Data)|td(<br>NWA|D2<br>CLKL-NBL<br>ITV)|||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|KL-NWEL)||||D1|D1|D1|||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLKL|KL-NWEL)||||th(CLKH-|th(CLKH-|th(CLKH-|H)|H)|
|||||||||||
|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|
|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)|OL + 0b)||


#### **Table 80. Synchronous multiplexed PSRAM write timings (1)(2)**











|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FSMC_CLK period|2THCLK|-|ns|
|td(CLKL-NExL)|FSMC_CLK low to FSMC_NEx low (x=0..2)|-|1|ns|
|td(CLKL-NExH)|FSMC_CLK low to FSMC_NEx high (x= 0…2)|1|-|ns|
|td(CLKL-NADVL)|FSMC_CLK low to FSMC_NADV low|-|0|ns|
|td(CLKL-<br>NADVH)|FSMC_CLK low to FSMC_NADV high|0|-|ns|
|td(CLKL-AV)|FSMC_CLK low to FSMC_Ax valid (x=16…25)|-|0|ns|
|td(CLKL-AIV)|FSMC_CLK low to FSMC_Ax invalid (x=16…25)|8|-|ns|
|td(CLKL-NWEL)|FSMC_CLK low to FSMC_NWE low|-|0.5|ns|
|td(CLKL-NWEH)|FSMC_CLK low to FSMC_NWE high|0|-|ns|
|td(CLKL-ADIV)|FSMC_CLK low to FSMC_AD[15:0] invalid|0|-|ns|
|td(CLKL-DATA)|FSMC_A/D[15:0] valid data after FSMC_CLK<br>low|-|3|ns|


<u>DS8626 Rev 12</u> <u>151/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**


**<u>Table 80. Synchronous multiplexed PSRAM write timings</u>** <sup>**(1)(2)**</sup> **<u>(continued)</u>**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|td(CLKL-NBLH)|FSMC_CLK low to FSMC_NBL high|0|-|ns|
|tsu(NWAIT-<br>CLKH)|FSMC_NWAIT valid before FSMC_CLK high|4|-|ns|
|th(CLKH-NWAIT)|FSMC_NWAIT valid after FSMC_CLK high|0|-|ns|


1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.

#### **Figure 60. Synchronous non-multiplexed NOR/PSRAM read timings**












|td(CL|Da|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|td(CL|Da|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|
|td(CL|KL-AV)<br>td(CL|KL-NADVH)||||||
|td(CL|KL-AV)<br>td(CL|||t|d(CLKL-AIV|)|)|
|td(CL|KL-AV)<br>td(CL|||t|d(CLKL-AIV|)||
|td(CL||||||||
|td(CL|||EL)|td(|CLKL-NOE|H)|H)|
|td(CL|||EL)|td(|CLKL-NOE|H)||
||tsu(|tsu(|tsu(|tsu(|tsu(|tsu(|tsu(|
||tsu(|tsu(|tsu(|tsu(|2<br>th(CL<br>ITV)|KH-D|KH-D|
||tsu(|tsu(|tsu(|tsu(|2<br>th(CL<br>ITV)|||
||tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|
||tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|||
|||||||||
|L + 0b)||||||||
|||||||||


|Col1|LKH)|
|---|---|
|TV-C|TV-C|
|||





<u>152/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Table 81. Synchronous non-multiplexed NOR/PSRAM read timings (1)(2)**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FSMC_CLK period|2THCLK –0.5|-|ns|
|td(CLKL-NExL)|FSMC_CLK low to FSMC_NEx low (x=0..2)|-|0.5|ns|
|td(CLKL-NExH)|FSMC_CLK low to FSMC_NEx high (x= 0…2)|0|-|ns|
|td(CLKL-NADVL)|FSMC_CLK low to FSMC_NADV low|-|2|ns|
|td(CLKL-NADVH)|FSMC_CLK low to FSMC_NADV high|3|-|ns|
|td(CLKL-AV)|FSMC_CLK low to FSMC_Ax valid (x=16…25)|-|0|ns|
|td(CLKL-AIV)|FSMC_CLK low to FSMC_Ax invalid (x=16…25)|2|-|ns|
|td(CLKL-NOEL)|FSMC_CLK low to FSMC_NOE low|-|0.5|ns|
|td(CLKL-NOEH)|FSMC_CLK low to FSMC_NOE high|1.5|-|ns|
|tsu(DV-CLKH)|FSMC_D[15:0] valid data before FSMC_CLK high|6|-|ns|
|th(CLKH-DV)|FSMC_D[15:0] valid data after FSMC_CLK high|3|-|ns|
|tsu(NWAIT-CLKH)|FSMC_NWAIT valid before FSMC_CLK high|4|-|ns|
|th(CLKH-NWAIT)|FSMC_NWAIT valid after FSMC_CLK high|0|-|ns|



1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.


<u>DS8626 Rev 12</u> <u>153/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 61. Synchronous non-multiplexed PSRAM write timings**




















|td(CL<br>td(CL|Da|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|td(CL<br>td(CL|Da|ta latency =|0|0|0|0|0|
|td(CL<br>td(CL|KL-AV)<br>td(CL|KL-NADVH)||||||
|td(CL<br>td(CL|KL-AV)<br>td(CL||||td(CLK|L-AI|V)|
|td(CL<br>td(CL||||||||
|td(CL<br>td(CL|KL-NWEL)||||td(CLKL|-NWE|H)|
|td(CL<br>td(CL|td(CL|KL-Data)|KL-Data)||D2<br>td(CLK<br>NWAITV)<br>td(CLKL|L-Da<br>-NBL|ta)|
|td(CL<br>td(CL|td(CL|KL-Data)|KL-Data)|D1|D1|D1||
|||||||||
|||||||||
||||||||H)|
||tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|


#### **Table 82. Synchronous non-multiplexed PSRAM write timings (1)(2)**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FSMC_CLK period|2THCLK|-|ns|
|td(CLKL-NExL)|FSMC_CLK low to FSMC_NEx low (x=0..2)|-|1|ns|
|td(CLKL-NExH)|FSMC_CLK low to FSMC_NEx high (x= 0…2)|1|-|ns|
|td(CLKL-NADVL)|FSMC_CLK low to FSMC_NADV low|-|7|ns|
|td(CLKL-NADVH)|FSMC_CLK low to FSMC_NADV high|6|-|ns|
|td(CLKL-AV)|FSMC_CLK low to FSMC_Ax valid (x=16…25)|-|0|ns|
|td(CLKL-AIV)|FSMC_CLK low to FSMC_Ax invalid (x=16…25)|6|-|ns|
|td(CLKL-NWEL)|FSMC_CLK low to FSMC_NWE low|-|1|ns|
|td(CLKL-NWEH)|FSMC_CLK low to FSMC_NWE high|2|-|ns|
|td(CLKL-Data)|FSMC_D[15:0] valid data after FSMC_CLK low|-|3|ns|
|td(CLKL-NBLH)|FSMC_CLK low to FSMC_NBL high|3|-|ns|
|tsu(NWAIT-CLKH)|FSMC_NWAIT valid before FSMC_CLK high|4|-|ns|
|th(CLKH-NWAIT)|FSMC_NWAIT valid after FSMC_CLK high|0|-|ns|



1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.


<u>154/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**PC Card/CompactFlash controller waveforms and timings**

#### Figure 62 through Figure 67 represent synchronous waveforms, and Table 83 and Table 84

provide the corresponding timings. The results shown in this table are obtained with the
following FSMC configuration:

      - COM.FSMC_SetupTime = 0x04;

      - COM.FSMC_WaitSetupTime = 0x07;

      - COM.FSMC_HoldSetupTime = 0x04;

      - COM.FSMC_HiZSetupTime = 0x00;

      - ATT.FSMC_SetupTime = 0x04;

      - ATT.FSMC_WaitSetupTime = 0x07;

      - ATT.FSMC_HoldSetupTime = 0x04;

      - ATT.FSMC_HiZSetupTime = 0x00;

      - IO.FSMC_SetupTime = 0x04;

      - IO.FSMC_WaitSetupTime = 0x07;

      - IO.FSMC_HoldSetupTime = 0x04;

      - IO.FSMC_HiZSetupTime = 0x00;

      - TCLRSetupTime = 0;

      - TARSetupTime = 0.


In all timing tables, the THCLK is the HCLK clock period.

#### **Figure 62. PC Card/CompactFlash controller waveforms for common memory read**

**<u>access</u>**











1. FSMC_NCE4_2 remains high (inactive during 8-bit access.





<u>DS8626 Rev 12</u> <u>155/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 63. PC Card/CompactFlash controller waveforms for common memory write**

**<u>access</u>**








|Col1|Col2|Col3|
|---|---|---|
||tv(NCE4_1-A)<br>td(NREG-NCE4_1)<br>td(NIORD-NCE4_1)<br>th(NCE4_1-AI~~)~~<br>th(NCE4_1-NREG)<br>th(NCE4_1-NIORD~~)~~<br>th(NCE4_1-NIOWR)|tv(NCE4_1-A)<br>td(NREG-NCE4_1)<br>td(NIORD-NCE4_1)<br>th(NCE4_1-AI~~)~~<br>th(NCE4_1-NREG)<br>th(NCE4_1-NIORD~~)~~<br>th(NCE4_1-NIOWR)|
||||
||tw(NWE)<br>td(NWE-NCE4_1)|tw(NWE)<br>td(NWE-NCE4_1)|
||||
||||









<u>156/206</u> <u>DS8626 Rev 12</u>




**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 64. PC Card/CompactFlash controller waveforms for attribute memory read**

**<u>access</u>**








|Col1|tv(NCE4_1-A) th(NCE4_1-AI)|Col3|
|---|---|---|
||tv(NCE4_1-A)<br>th(NCE4_1-AI)||
||||
||td(NREG-NCE4_1)<br>th(NCE4_1-NREG~~)~~|td(NREG-NCE4_1)<br>th(NCE4_1-NREG~~)~~|
||||



1. Only data bits 0...7 are read (bits 8...15 are disregarded).





<u>DS8626 Rev 12</u> <u>157/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 65. PC Card/CompactFlash controller waveforms for attribute memory write**

**<u>access</u>**








|Col1|Col2|
|---|---|
|||


|Col1|Col2|Col3|
|---|---|---|
||tv(NCE4_1-A)<br>th(NCE4_1-AI~~)~~|tv(NCE4_1-A)<br>th(NCE4_1-AI~~)~~|
||td(NREG-NCE4_1)<br>th(NCE4_1-NREG)|td(NREG-NCE4_1)<br>th(NCE4_1-NREG)|
||||







1. Only data bits 0...7 are driven (bits 8...15 remains Hi-Z).

#### **Figure 66. PC Card/CompactFlash controller waveforms for I/O space read access**


<u>158/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 67. PC Card/CompactFlash controller waveforms for I/O space write access**






#### **Table 83. Switching characteristics for PC Card/CF read and write cycles**

|Col1|in attribute/common space(1)|)(2)|Col4|Col5|
|---|---|---|---|---|
|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|tv(NCEx-A)|FSMC_Ncex low to FSMC_Ay valid|-|0|ns|
|th(NCEx_AI)|FSMC_NCEx high to FSMC_Ax invalid|4|-|ns|
|td(NREG-NCEx)|FSMC_NCEx low to FSMC_NREG valid|-|3.5|ns|
|th(NCEx-NREG)|FSMC_NCEx high to FSMC_NREG invalid|THCLK+4|-|ns|
|td(NCEx-NWE)|FSMC_NCEx low to FSMC_NWE low|-|5THCLK+0.5|ns|
|td(NCEx-NOE)|FSMC_NCEx low to FSMC_NOE low|-|5THCLK +0.5|ns|
|tw(NOE)|FSMC_NOE low width|8THCLK–1|8THCLK+1|ns|
|td(NOE_NCEx)|FSMC_NOE high to FSMC_NCEx high|5THCLK+2.5|-|ns|
|tsu (D-NOE)|FSMC_D[15:0] valid data before FSMC_NOE high|4.5|-|ns|
|th(N0E-D)|FSMC_N0E high to FSMC_D[15:0] invalid|3|-|ns|
|tw(NWE)|FSMC_NWE low width|8THCLK–0.5|8THCLK+ 3|ns|
|td(NWE_NCEx)|FSMC_NWE high to FSMC_NCEx high|5THCLK–1|-|ns|
|td(NCEx-NWE)|FSMC_NCEx low to FSMC_NWE low|-|5THCLK+ 1|ns|
|tv(NWE-D)|FSMC_NWE low to FSMC_D[15:0] valid|-|0|ns|
|th (NWE-D)|FSMC_NWE high to FSMC_D[15:0] invalid|8THCLK –1|-|ns|
|td (D-NWE)|FSMC_D[15:0] valid before FSMC_NWE high|13THCLK –1|-|ns|



1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.


<u>DS8626 Rev 12</u> <u>159/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

|Tab|ble 84. Switching characteristics for PC Card/CF in I/O space(1)(2)|F read and wr|rite cycles|Col5|
|---|---|---|---|---|
|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|tw(NIOWR)|FSMC_NIOWR low width|8THCLK –1|-|ns|
|tv(NIOWR-D)|FSMC_NIOWR low to FSMC_D[15:0] valid|-|5THCLK– 1|ns|
|th(NIOWR-D)|FSMC_NIOWR high to FSMC_D[15:0] invalid|8THCLK– 2|-|ns|
|td(NCE4_1-NIOWR)|FSMC_NCE4_1 low to FSMC_NIOWR valid|-|5THCLK+ 2.5|ns|
|th(NCEx-NIOWR)|FSMC_NCEx high to FSMC_NIOWR invalid|5THCLK–1.5|-|ns|
|td(NIORD-NCEx)|FSMC_NCEx low to FSMC_NIORD valid|-|5THCLK+ 2|ns|
|th(NCEx-NIORD)|FSMC_NCEx high to FSMC_NIORD) valid|5THCLK– 1.5|-|ns|
|tw(NIORD)|FSMC_NIORD low width|8THCLK–0.5|-|ns|
|tsu(D-NIORD)|FSMC_D[15:0] valid before FSMC_NIORD high|9|-|ns|
|td(NIORD-D)|FSMC_D[15:0] valid after FSMC_NIORD high|0|-|ns|



1. CL = 30 pF.

2. Evaluated by characterization - not tested in production.


**NAND controller waveforms and timings**


_Figure 68_ and _Figure 69_ represent synchronous waveforms, and _Table 85_ and _Table 86_
provide the corresponding timings. The results shown in this table are obtained with the
following FSMC configuration:

      - COM.FSMC_SetupTime = 0x01;

      - COM.FSMC_WaitSetupTime = 0x03;

      - COM.FSMC_HoldSetupTime = 0x02;

      - COM.FSMC_HiZSetupTime = 0x01;

      - ATT.FSMC_SetupTime = 0x01;

      - ATT.FSMC_WaitSetupTime = 0x03;

      - ATT.FSMC_HoldSetupTime = 0x02;

      - ATT.FSMC_HiZSetupTime = 0x01;

      - Bank = FSMC_Bank_NAND;

      - MemoryDataWidth = FSMC_MemoryDataWidth_16b;

      - ECC = FSMC_ECC_Enable;

      - ECCPageSize = FSMC_ECCPageSize_512Bytes;

      - TCLRSetupTime = 0;

      - TARSetupTime = 0.


In all timing tables, the THCLK is the HCLK clock period.


<u>160/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**

#### **Figure 68. NAND controller waveforms for read access**







1. y = 7 or 15 depending on the NAND flash memory interface.







1. y = 7 or 15 depending on the NAND flash memory interface.

#### **Table 85. Switching characteristics for NAND flash read cycles (1)**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(N0E)|FSMC_NOE low width|4THCLK– <br>0.5|4THCLK+ 3|ns|
|tsu(D-NOE)|FSMC_D[15-0] valid data before FSMC_NOE high|10|-|ns|
|th(NOE-D)|FSMC_D[15-0] valid data after FSMC_NOE high|0|-|ns|
|td(ALE-NOE)|FSMC_ALE valid before FSMC_NOE low|-|3THCLK|ns|
|th(NOE-ALE)|FSMC_NWE high to FSMC_ALE invalid|3THCLK– 2|-|ns|



1. CL = 30 pF.


<u>DS8626 Rev 12</u> <u>161/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Table 86. Switching characteristics for NAND flash write cycles (1)**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NWE)|FSMC_NWE low width|4THCLK–1|4THCLK+ 3|ns|
|tv(NWE-D)|FSMC_NWE low to FSMC_D[15-0] valid|-|0|ns|
|th(NWE-D)|FSMC_NWE high to FSMC_D[15-0] invalid|3THCLK –2|-|ns|
|td(D-NWE)|FSMC_D[15-0] valid before FSMC_NWE high|5THCLK–3|-|ns|
|td(ALE-NWE)|FSMC_ALE valid before FSMC_NWE low|-|3THCLK|ns|
|th(NWE-ALE)|FSMC_NWE high to FSMC_ALE invalid|3THCLK–2|-|ns|



1. CL = 30 pF.

### **6.3.27 Camera interface (DCMI) timing specifications**

#### Unless otherwise specified, the parameters given in Table 87 for DCMI are derived from

tests performed under the ambient temperature, fHCLK frequency and VDD supply voltage
summarized in _Table 13_, with the following configuration:

      - PCK polarity: falling

      - VSYNC and HSYNC polarity: high

      - Data format: 14 bits

#### **Figure 70. DCMI timing diagram**








|Col1|Col2|
|---|---|
||tsu(VSY|
|||



|Col1|Table 87. DCMI characteristics(1|1)|Col4|Col5|
|---|---|---|---|---|
|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|-|Frequency ratio DCMI_PIXCLK/fHCLK|-|0.4|-|
|DCMI_PIXCLK|Pixel clock input|-|54|MHz|
|Dpixel|Pixel clock input duty cycle|30|70|%|


<u>162/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Electrical characteristics**


**<u>Table 87. DCMI characteristics</u>** <sup>**(1)**</sup> **<u>(continued)</u>**








|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tsu(DATA)|Data input setup time|2.5|-|ns|
|th(DATA)|Data hold time|1|-|-|
|tsu(HSYNC), <br>tsu(VSYNC)|HSYNC/VSYNC input setup time|2|-|-|
|th(HSYNC), <br>th(VSYNC)|HSYNC/VSYNC input hold time|0.5|-|-|



1. Evaluated by characterization - not tested in production.

### **6.3.28 SD/SDIO MMC card host interface (SDIO) characteristics**


Unless otherwise specified, the parameters given in _Table 88_ are derived from tests
performed under ambient temperature, fPCLKx frequency and VDD supply voltage conditions
summarized in _Table 14_ with the following configuration:

      - Output speed is set to OSPEEDRy[1:0] = 10

      - Capacitive load C = 30 pF

      - Measurement points are done at CMOS levels: 0.5VDD

Refer to _Section 6.3.16: I/O port characteristics_ for more details on the input/output
characteristics.

#### **Figure 71. SDIO high-speed mode**


<u>DS8626 Rev 12</u> <u>163/206</u>



191


**Electrical characteristics** **STM32F405xx, STM32F407xx**

#### **Figure 72. SD default mode** **Table 88. Dynamic characteristics: SD/MMC characteristics (1)**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fPP|Clock frequency in data transfer mode|-|0|-|48|MHz|
||SDIO_CK/fPCLK2 frequency ratio|-|-|-|8/3|-|
|tW(CKL)|Clock low time|fPP = 48 MHz|8.5|9|-|ns|
|tW(CKH)|Clock high time|fPP = 48 MHz|8.3|10|-|-|
|CMD, D inputs (referenced to CK) in MMC and SD HS mode|CMD, D inputs (referenced to CK) in MMC and SD HS mode|CMD, D inputs (referenced to CK) in MMC and SD HS mode|CMD, D inputs (referenced to CK) in MMC and SD HS mode|CMD, D inputs (referenced to CK) in MMC and SD HS mode|CMD, D inputs (referenced to CK) in MMC and SD HS mode|CMD, D inputs (referenced to CK) in MMC and SD HS mode|
|tISU|Input setup time HS|fPP = 48 MHz|3|-|-|ns|
|tIH|Input hold time HS|fPP = 48 MHz|0|-|-|-|
|CMD, D outputs (referenced to CK) in MMC and SD HS mode|CMD, D outputs (referenced to CK) in MMC and SD HS mode|CMD, D outputs (referenced to CK) in MMC and SD HS mode|CMD, D outputs (referenced to CK) in MMC and SD HS mode|CMD, D outputs (referenced to CK) in MMC and SD HS mode|CMD, D outputs (referenced to CK) in MMC and SD HS mode|CMD, D outputs (referenced to CK) in MMC and SD HS mode|
|tOV|Output valid time HS|fPP = 48 MHz|-|4.5|6|ns|
|tOH|Output hold time HS|fPP = 48 MHz|1|-|-|-|
|CMD, D inputs (referenced to CK) in SD default mode|CMD, D inputs (referenced to CK) in SD default mode|CMD, D inputs (referenced to CK) in SD default mode|CMD, D inputs (referenced to CK) in SD default mode|CMD, D inputs (referenced to CK) in SD default mode|CMD, D inputs (referenced to CK) in SD default mode|CMD, D inputs (referenced to CK) in SD default mode|
|tISUD|Input setup time SD|fPP = 24 MHz|1.5|-|-|ns|
|tIHD|Input hold time SD|fPP = 24 MHz|0.5|-|-|-|
|CMD, D outputs (referenced to CK) in SD default mode|CMD, D outputs (referenced to CK) in SD default mode|CMD, D outputs (referenced to CK) in SD default mode|CMD, D outputs (referenced to CK) in SD default mode|CMD, D outputs (referenced to CK) in SD default mode|CMD, D outputs (referenced to CK) in SD default mode|CMD, D outputs (referenced to CK) in SD default mode|
|tOVD|Output valid default time SD|fPP = 24 MHz|-|4.5|7|ns|
|tOHD|Output hold default time SD|fPP = 24 MHz|0.5|-|-|-|



1. Evaluated by characterization - not tested in production.

### **6.3.29 RTC characteristics**

#### **Table 89. RTC characteristics**

|Symbol|Parameter|Conditions|Min|Max|
|---|---|---|---|---|
|-|fPCLK1/RTCCLK frequency ratio|Any read/write operation<br>from/to an RTC register|4|-|



<u>164/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Package information**

# **7 Package information**


In order to meet environmental requirements, ST offers these devices in different grades of
ECOPACK packages, depending on their level of environmental compliance. ECOPACK
specifications, grade definitions and product status are available at: _www.st.com_ .
ECOPACK is an ST trademark.

## **7.1 Device marking**


Refer to technical note “Reference device marking schematics for STM32 microcontrollers
and microprocessors” (TN1433), available on _www.st.com_, for the location of pin 1 / ball A1
as well as the location and orientation of the marking areas versus pin 1 / ball A1.


Parts marked as “ES”, “E”, or accompanied by an engineering sample notification letter, are
not yet qualified and therefore not approved for use in production. ST is not responsible for
any consequences resulting from such use. In no event will ST be liable for the customer
using any of these engineering samples in production. ST’s Quality department must be
contacted prior to any decision to use these engineering samples to run a qualification
activity.


A WLCSP simplified marking example (if any) is provided in the corresponding package
information subsection.


<u>DS8626 Rev 12</u> <u>165/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**

## **7.2 WLCSP90 package information**

### **Figure 73. WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch wafer level chip scale**

**<u>package outline</u>**














|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||



















1. Drawing is not to scale.


<u>166/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Package information**

### **Table 90. WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch wafer level chip scale**

**<u>package mechanical data</u>**







|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
|** Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A|0.540|0.570|0.600|0.0213|0.0224|0.0236|
|A1|-|0.190|-|-|0.0075|-|
|A2|-|0.380|-|-|0.0150|-|
|A3(2)|-|0.025|-|-|0.0010|-|
|b(3)|0.240|0.270|0.300|0.0094|0.0106|0.0118|
|D|4.188|4.223|4.258|0.1649|0.1663|0.1676|
|E|3.934|3.969|4.004|0.1549|0.1563|0.1576|
|e|-|0.400|-|-|0.0157|-|
|e1|-|3.600|-|-|0.1417|-|
|e2|-|3.200|-|-|0.1260|-|
|F|-|0.3115|-|-|0.0123|-|
|G|-|0.3845|-|-|0.0151|-|
|aaa|-|0.100|-|-|0.0039|-|
|bbb|-|0.100|-|-|0.0039|-|
|ccc|-|0.100|-|-|0.0039|-|
|ddd|-|0.050|-|-|0.0020|-|
|eee|-|0.050|-|-|0.0020|-|


1. Values in inches are converted from mm and rounded to 4 decimal digits.


2. Back side coating.


3. Dimension is measured at the maximum bump diameter parallel to primary datum Z.

### **Figure 74. WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch wafer level chip scale**

**<u>package recommended footprint</u>**


<u>DS8626 Rev 12</u> <u>167/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**

|Table 91. WLCSP90|recommended PCB design rules|
|---|---|
|** Dimension**|**Recommended values**|
|Pitch|0.4 mm|
|Dpad|260 µm max. (circular)<br>220 µm recommended|
|Dsm|300 µm min. (for 260 µm diameter pad)|
|PCB pad design|Non-solder mask defined via underbump allowed|



**Device marking for WLCSP90**


The following figure gives an example of topside marking and ball A1 position identifier
location.


The printed markings may differ depending on the supply chain.
Other optional marking or inset/upset marks, which depend on supply chain operations, are
not indicated below.

### **Figure 75. WLCSP90 marking example (package top view)**







1. Parts marked as “ES”, “E” or accompanied by an Engineering Sample notification letter, are not yet
qualified and therefore not yet ready to be used in production and any consequences deriving from such
usage will not be at ST charge. In no event, ST will be liable for any customer usage of these engineering
samples in production. ST Quality has to be contacted prior to any decision to use these Engineering
Samples to run qualification activity.


<u>168/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Package information**

## **7.3 LQFP64 package information (5W)**


This LQFP is 64-pin, 10 x 10 mm low-profile quad flat package.

### **Figure 76. LQFP64 - Outline (15)**

































































<u>DS8626 Rev 12</u> <u>169/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**

### **Table 92. LQFP64 - Mechanical data**







|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A<br>|-|-|1.60|-|-|0.0630|
|A1(12)|0.05|-|0.15|0.0020|-|0.0059|
|A2<br>|1.35|1.40|1.45|0.0531|0.0551|0.0570|
|b(9)(11)<br>|0.17|0.22|0.27|0.0067|0.0087|0.0106|
|b1(11)<br>|0.17|0.20|0.23|0.0067|0.0079|0.0091|
|c(11)<br>|0.09|-|0.20|0.0035|-|0.0079|
|c1(11)<br>|0.09|-|0.16|0.0035|-|0.0063|
|D(4)<br>|12.00 BSC|12.00 BSC|12.00 BSC|0.4724 BSC|0.4724 BSC|0.4724 BSC|
|D1(2)(5)<br>|10.00 BSC|10.00 BSC|10.00 BSC|0.3937 BSC|0.3937 BSC|0.3937 BSC|
|E(4)<br>|12.00 BSC|12.00 BSC|12.00 BSC|0.4724 BSC|0.4724 BSC|0.4724 BSC|
|E1(2)(5)|10.00 BSC|10.00 BSC|10.00 BSC|0.3937 BSC|0.3937 BSC|0.3937 BSC|
|e|0.50 BSC|0.50 BSC|0.50 BSC|0.1970 BSC|0.1970 BSC|0.1970 BSC|
|L|0.45|0.60|0.75|0.0177|0.0236|0.0295|
|L1<br>|1.00 REF|1.00 REF|1.00 REF|0.0394 REF|0.0394 REF|0.0394 REF|
|N(13)|64|64|64|64|64|64|
|θ|0°|3.5°|7°|0°|3.5°|7°|
|θ1|0°|-|-|0°|-|-|
|θ2|10°|12°|14°|10°|12°|14°|
|θ3|10°|12°|14°|10°|12°|14°|
|R1|0.08|-|-|0.0031|-|-|
|R2|0.08|-|0.20|0.0031|-|0.0079|
|S<br>|0.20|-|-|0.0079|-|-|
|aaa(1)<br>|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|bbb(1)<br>|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|ccc(1)<br>|0.08|0.08|0.08|0.0031|0.0031|0.0031|
|ddd(1)|0.08|0.08|0.08|0.0031|0.0031|0.0031|


<u>170/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Package information**


**Notes:**


1. Dimensioning and tolerancing schemes conform to ASME Y14.5M-1994.

2. The Top package body size may be smaller than the bottom package size by as much
as 0.15 mm.

3. Datums A-B and D to be determined at datum plane H.

4. To be determined at seating datum plane C.

5. Dimensions D1 and E1 do not include mold flash or protrusions. Allowable mold flash
or protrusions is “0.25 mm” per side. D1 and E1 are Maximum plastic body size
dimensions including mold mismatch.

6. Details of pin 1 identifier are optional but must be located within the zone indicated.

7. All Dimensions are in millimeters.

8. No intrusion allowed inwards the leads.

9. Dimension “b” does not include dambar protrusion. Allowable dambar protrusion shall
not cause the lead width to exceed the maximum “b” dimension by more than 0.08 mm.
Dambar cannot be located on the lower radius or the foot. Minimum space between
protrusion and an adjacent lead is 0.07 mm for 0.4 mm and 0.5 mm pitch packages.

10. Exact shape of each corner is optional.

11. These dimensions apply to the flat section of the lead between 0.10 mm and 0.25 mm
from the lead tip.

12. A1 is defined as the distance from the seating plane to the lowest point on the package
body.

13. “N” is the number of terminal positions for the specified body size.

14. Values in inches are converted from mm and rounded to 4 decimal digits.

15. Drawing is not to scale.


<u>DS8626 Rev 12</u> <u>171/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**

## **7.4 LQFP100 package information (1L)**


This LQFP is a 100-pin, 14 x 14 mm low-profile quad flat package.


_Note:_ _See list of notes in the notes section._

### **Figure 77. LQFP100 - Outline (15)**










































































|Col1|D (3)|
|---|---|
|||
|D1/4<br>E1/4<br>(6)||
|||



<u>172/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Package information**

### **Table 93. LQFP100 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A|-|1.50|1.60|-|0.0590|0.0630|
|A1(12)|0.05|-|0.15|0.0019|-|0.0059|
|A2|1.35|1.40|1.45|0.0531|0.0551|0.0570|
|b(9)(11)|0.17|0.22|0.27|0.0067|0.0087|0.0106|
|b1(11)|0.17|0.20|0.23|0.0067|0.0079|0.0090|
|c(11)|0.09|-|0.20|0.0035|-|0.0079|
|c1(11)|0.09|-|0.16|0.0035|-|0.0063|
|D(4)|16.00 BSC|16.00 BSC|16.00 BSC|0.6299 BSC|0.6299 BSC|0.6299 BSC|
|D1(2)(5)|14.00 BSC|14.00 BSC|14.00 BSC|0.5512 BSC|0.5512 BSC|0.5512 BSC|
|E(4)|16.00 BSC|16.00 BSC|16.00 BSC|0.6299 BSC|0.6299 BSC|0.6299 BSC|
|E1(2)(5)|14.00 BSC|14.00 BSC|14.00 BSC|0.5512 BSC|0.5512 BSC|0.5512 BSC|
|e|0.50 BSC|0.50 BSC|0.50 BSC|0.0197 BSC|0.0197 BSC|0.0197 BSC|
|L|0.45|0.60|0.75|0.177|0.0236|0.0295|
|L1(1)(11)|1.00|1.00|1.00|-|0.0394|-|
|N(13)|100|100|100|100|100|100|
|θ|0°|3.5°|7°|0°|3.5°|7°|
|θ1|0°|-|-|0°|-|-|
|θ2|10°|12°|14°|10°|12°|14°|
|θ3|10°|12°|14°|10°|12°|14°|
|R1|0.08|-|-|0.0031|-|-|
|R2|0.08|-|0.20|0.0031|-|0.0079|
|S|0.20|-|-|0.0079|-|-|
|aaa(1)|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|bbb(1)|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|ccc(1)|0.08|0.08|0.08|0.0031|0.0031|0.0031|
|ddd(1)|0.08|0.08|0.08|0.0031|0.0031|0.0031|



<u>DS8626 Rev 12</u> <u>173/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**


**Notes:**


1. Dimensioning and tolerancing schemes conform to ASME Y14.5M-1994.

2. The top package body size may be smaller than the bottom package size by as much
as 0.15 mm.

3. Datums A-B and D to be determined at datum plane H.

4. To be determined at the seating datum plane C.

5. Dimensions D1 and E1 do not include mold flash or protrusions. Allowable mold flash
or protrusions is 0.25 mm per side. D1 and E1 are maximum plastic body size
dimensions including mold mismatch.

6. Details of pin 1 identifier are optional but must be located within the zone indicated.

7. All dimensions are in millimeters.

8. No intrusion is allowed inwards the leads.

9. Dimension b does not include a dambar protrusion. Allowable dambar protrusion shall
not cause the lead width to exceed the maximum b dimension by more than 0.08 mm.
The dambar cannot be located on the lower radius or the foot. The minimum space
between the protrusion and an adjacent lead is 0.07 mm for 0.4 mm and 0.5 mm pitch
packages.

10. The exact shape of each corner is optional.

11. These dimensions apply to the flat section of the lead that is between 0.10 mm and
0.25 mm from the lead tip.

12. A1 is defined as the distance from the seating plane to the lowest point on the package
body.

13. N is the number of terminal positions for the specified body size.

14. Values in inches are converted from mm and rounded to four decimal digits.

15. Drawing is not to scale.

### **Figure 78. LQFP100 - Footprint example**











1. Dimensions are expressed in millimeters.


<u>174/206</u> <u>DS8626 Rev 12</u>








**STM32F405xx, STM32F407xx** **Package information**

## **7.5 LQFP144 package information (1A)**


This LQFP is a 144-pin, 20 x 20 mm low-profile quad flat package.


_Note:_ _See list of notes in the notes section._

### **Figure 79. LQFP144 - Outline (15)**




























|Col1|aaa|C|A-B|D|
|---|---|---|---|---|
||||||


|Col1|bb|bH A-B D|
|---|---|---|
||||


|A|Col2|Col3|Col4|
|---|---|---|---|
|A||||


















































|Col1|Col2|
|---|---|
|||
|||
|A<br>(Section A-A)|A<br>(Section A-A)|





<u>DS8626 Rev 12</u> <u>175/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**

### **Table 94. LQFP144 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A|-|-|1.60|-|-|0.0630|
|A1(12)|0.05|-|0.15|0.0020|-|0.0059|
|A2|1.35|1.40|1.45|0.0531|0.0551|0.0571|
|b(9)(11)|0.17|0.22|0.27|0.0067|0.0087|0.0106|
|b1(11)|0.17|0.20|0.23|0.0067|0.0079|0.0090|
|c(11)|0.09|-|0.20|0.0035|-|0.0079|
|c1(11)|0.09|-|0.16|0.0035|-|0.0063|
|D(4)|22.00 BSC|22.00 BSC|22.00 BSC|0.8661 BSC|0.8661 BSC|0.8661 BSC|
|D1(2)(5)|20.00 BSC|20.00 BSC|20.00 BSC|0.7874 BSC|0.7874 BSC|0.7874 BSC|
|E(4)|22.00 BSC|22.00 BSC|22.00 BSC|0.8661 BSC|0.8661 BSC|0.8661 BSC|
|E1(2)(5)|20.00 BSC|20.00 BSC|20.00 BSC|0.7874 BSC|0.7874 BSC|0.7874 BSC|
|e|0.50 BSC|0.50 BSC|0.50 BSC|0.0197 BSC|0.0197 BSC|0.0197 BSC|
|L|0.45|0.60|0.75|0.0177|0.0236|0.0295|
|L1|1.00 REF|1.00 REF|1.00 REF|0.0394 REF|0.0394 REF|0.0394 REF|
|N(13)|144|144|144|144|144|144|
|θ|0°|3.5°|7°|0°|3.5°|7°|
|θ1|0°|-|-|0°|-|-|
|θ2|10°|12°|14°|10°|12°|14°|
|θ3|10°|12°|14°|10°|12°|14°|
|R1|0.08|-|-|0.0031|-|-|
|R2|0.08|-|0.20|0.0031|-|0.0079|
|S|0.20|-|-|0.0079|-|-|
|aaa|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|bbb|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|ccc|0.08|0.08|0.08|0.0031|0.0031|0.0031|
|ddd|0.08|0.08|0.08|0.0031|0.0031|0.0031|



<u>176/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Package information**


**Notes:**


1. Dimensioning and tolerancing schemes conform to ASME Y14.5M-1994.

2. The top package body size may be smaller than the bottom package size by as much
as 0.15 mm.

3. Datums A-B and D to be determined at datum plane H.

4. To be determined at the seating datum plane C.

5. Dimensions D1 and E1 do not include mold flash or protrusions. Allowable mold flash
or protrusions is 0.25 mm per side. D1 and E1 are maximum plastic body size
dimensions including mold mismatch.

6. Details of pin 1 identifier are optional but must be located within the zone indicated.

7. All dimensions are in millimeters.

8. No intrusion is allowed inwards the leads.

9. Dimension b does not include a dambar protrusion. Allowable dambar protrusion shall
not cause the lead width to exceed the maximum b dimension by more than 0.08 mm.
The dambar cannot be located on the lower radius or the foot. The minimum space
between the protrusion and an adjacent lead is 0.07 mm for 0.4 mm and 0.5 mm pitch
packages.

10. The exact shape of each corner is optional.

11. These dimensions apply to the flat section of the lead that is between 0.10 mm and
0.25 mm from the lead tip.

12. A1 is defined as the distance from the seating plane to the lowest point on the package
body.

13. N is the number of terminal positions for the specified body size.

14. Values in inches are converted from mm and rounded to four decimal digits.

15. Drawing is not to scale.


<u>DS8626 Rev 12</u> <u>177/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**

### **Figure 80. LQFP144 - Footprint example**












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||||||||





1. Dimensions are expressed in millimeters.


<u>178/206</u> <u>DS8626 Rev 12</u>




**STM32F405xx, STM32F407xx** **Package information**

## **7.6 UFBGA(176+25) package information (A0E7)**


This UFBGA is a 176+25-ball, 10 x 10 mm, 0.65 mm pitch, ultra fine pitch ball grid array
package.

### **Figure 81. UFBGA(176+25) - Outline**




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|ddd|C|
|---|---|---|---|---|---|---|---|---|
||||||||||
















|Col1|Col2|Col3|
|---|---|---|
||||





1. Drawing is not to scale.










|Col1|ØeeeM|C|A|B|
|---|---|---|---|---|
||fff<br>Ø<br>M|C|C|C|






### **Table 95. UFBGA(176+25) - Mechanical data**



|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min.**|**Typ.**|**Max.**|**Min.**|**Typ.**|**Max.**|
|A|-|-|0.600|-|-|0.0236|
|A1|0.050|0.080|0.110|0.0020|0.0031|0.0043|
|A2|-|0.450|-|-|0.0177|-|
|A3|-|0.130|-|-|0.0051|-|
|A4|-|0.320|-|-|0.0126|-|
|b|0.240|0.290|0.340|0.0094|0.0114|0.0134|
|D|9.850|10.000|10.150|0.3878|0.3937|0.3996|
|D1|-|9.100|-|-|0.3583|-|
|E|9.850|10.000|10.150|0.3878|0.3937|0.3996|
|E1|-|9.100|-|-|0.3583|-|
|e|-|0.650|-|-|0.0256|-|
|F|-|0.450|-|-|0.0177|-|
|ddd|-|-|0.080|-|-|0.0031|


<u>DS8626 Rev 12</u> <u>179/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**


**<u>Table 95. UFBGA(176+25) - Mechanical data (continued)</u>**

|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min.**|**Typ.**|**Max.**|**Min.**|**Typ.**|**Max.**|
|eee|-|-|0.150|-|-|0.0059|
|fff|-|-|0.050|-|-|0.0020|



1. Values in inches are converted from mm and rounded to 4 decimal digits.

### **Figure 82. UFBGA(176+25) - Footprint example** **Table 96. UFBGA(176+25) - Example of PCB design rules (0.65 mm pitch BGA)**

|Dimension|Values|
|---|---|
|Pitch|0.65 mm|
|Dpad|0.300 mm|
|Dsm|0.400 mm typ. (depends on the soldermask<br>registration tolerance)|
|Stencil opening|0.300 mm|
|Stencil thickness|Between 0.100 mm and 0.125 mm|
|Pad trace width|0.100 mm|



<u>180/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Package information**

## **7.7 LQFP176 package information (1T)**


This LQFP is a 176-pin, 24 x 24 mm, 0.5 mm pitch, low profile quad flat package.


_Note:_ _See list of notes in the notes section._

### **Figure 83. LQFP176 - Outline (15)**













































































<u>DS8626 Rev 12</u> <u>181/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**

### **Table 97. LQFP176 - Mechanical data**







|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A<br>|-|-|1.600|-|-|0.0630|
|A1(12)|0.050|-|0.150|0.0020|-|0.0059|
|A2<br>|1.350|1.400|1.450|0.0531|0.0551|0.0571|
|b(9)(11)<br>|0.170|0.220|0.270|0.0067|0.0087|0.0106|
|b1(11)<br>|0.170|0.200|0.230|0.0067|0.0079|0.0091|
|c(11)<br>|0.090|-|0.200|0.0035|-|0.0079|
|c1(11)<br>|0.090|-|0.160|0.0035|-|0.063|
|D(4)<br>|26.000|26.000|26.000|1.0236|1.0236|1.0236|
|D1(2)(5)<br>|24.000|24.000|24.000|0.9449|0.9449|0.9449|
|E(4)<br>|26.000|26.000|26.000|0.0197|0.0197|0.0197|
|E1(2)(5)|24.000|24.000|24.000|0.9449|0.9449|0.9449|
|e|0.500|0.500|0.500|0.1970|0.1970|0.1970|
|L<br>|0.450|0.600|0.750|0.0177|0.0236|0.0295|
|L1(1)(11)<br>|1|1|1|0.0394 REF|0.0394 REF|0.0394 REF|
|N(13)|176|176|176|176|176|176|
|θ|0°|3.5°|7°|0°|3.5°|7°|
|θ1|0°|-|-|0°|-|-|
|θ2|10°|12°|14°|10°|12°|14°|
|θ3|10°|12°|14°|10°|12°|14°|
|R1|0.080|-|-|0.0031|-|-|
|R2|0.080|-|0.200|0.0031|-|0.0079|
|S<br>|0.200|-|-|0.0079|-|-|
|aaa(1)<br>|0.200|0.200|0.200|0.0079|0.0079|0.0079|
|bbb(1)<br>|0.200|0.200|0.200|0.0079|0.0079|0.0079|
|ccc(1)<br>|0.080|0.080|0.080|0.0031|0.0031|0.0031|
|ddd(1)|0.080|0.080|0.080|0.0031|0.0031|0.0031|


<u>182/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Package information**


**Notes:**


1. Dimensioning and tolerancing schemes conform to ASME Y14.5M-1994.

2. The top package body size may be smaller than the bottom package size by as much
as 0.15 mm.

3. Datums A-B and D to be determined at datum plane H.

4. To be determined at the seating datum plane C.

5. Dimensions D1 and E1 do not include mold flash or protrusions. Allowable mold flash
or protrusions is 0.25 mm per side. D1 and E1 are maximum plastic body size
dimensions including mold mismatch.

6. Details of pin 1 identifier are optional but must be located within the zone indicated.

7. All dimensions are in millimeters.

8. No intrusion is allowed inwards the leads.

9. Dimension b does not include a dambar protrusion. Allowable dambar protrusion shall
not cause the lead width to exceed the maximum b dimension by more than 0.08 mm.
The dambar cannot be located on the lower radius or the foot. The minimum space
between the protrusion and an adjacent lead is 0.07 mm for 0.4 mm and 0.5 mm pitch
packages.

10. The exact shape of each corner is optional.

11. These dimensions apply to the flat section of the lead that is between 0.10 mm and
0.25 mm from the lead tip.

12. A1 is defined as the distance from the seating plane to the lowest point on the package
body.

13. N is the number of terminal positions for the specified body size.

14. Values in inches are converted from mm and rounded to four decimal digits.

15. Drawing is not to scale.


<u>DS8626 Rev 12</u> <u>183/206</u>



191


**Package information** **STM32F405xx, STM32F407xx**

### **Figure 84. LQFP176 - Footprint example**



|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|Col39|Col40|Col41|Col42|Col43|Col44|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
||44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||


1. Dimensions are expressed in millimeters.


<u>184/206</u> <u>DS8626 Rev 12</u>








**STM32F405xx, STM32F407xx** **Package information**

## **7.8 Thermal characteristics**


The maximum chip-junction temperature, TJ max, in degrees Celsius, may be calculated
using the following equation:


TJ max = TA max + (PD max x Θ JA)

Where:

      - TA max is the maximum ambient temperature in ° C,

      - Θ JA is the package junction-to-ambient thermal resistance, in ° C/W,

      - PD max is the sum of PINT max and PI/O max (PD max = PINT max + PI/Omax),

      - PINT max is the product of IDD and VDD, expressed in Watts. This is the maximum chip
internal power.


PI/O max represents the maximum power dissipation on output pins where:

PI/O max = Σ (VOL × IOL) + Σ ((VDD – VOH) × IOH),

taking into account the actual VOL / IOL and VOH / IOH of the I/Os at low and high level in the
application.

### **Table 98. Package thermal characteristics**








|Symbol|Parameter|Value|Unit|
|---|---|---|---|
|ΘJA|**Thermal resistance junction-ambient** <br>LQFP64 - 10 × 10 mm / 0.5 mm pitch|46|°C/W|
|ΘJA|**Thermal resistance junction-ambient** <br>LQFP100 - 14 × 14 mm / 0.5 mm pitch|43|43|
|ΘJA|**Thermal resistance junction-ambient** <br>LQFP144 - 20 × 20 mm / 0.5 mm pitch|40|40|
|ΘJA|**Thermal resistance junction-ambient** <br>LQFP176 - 24 × 24 mm / 0.5 mm pitch|38|38|
|ΘJA|**Thermal resistance junction-ambient** <br>UFBGA176 - 10× 10 mm / 0.65 mm pitch|39|39|
|ΘJA|**Thermal resistance junction-ambient** <br>WLCSP90 - 0.400 mm pitch|38.1|38.1|



**Reference document**


JESD51-2 Integrated Circuits Thermal Test Method Environment Conditions - Natural
Convection (Still Air). Available from www.jedec.org.


<u>DS8626 Rev 12</u> <u>185/206</u>



191


**Ordering information** **STM32F405xx, STM32F407xx**

# **8 Ordering information**


Example: STM32 F 405 R E T 6 xxx


TR = tape and reel


For a list of available options (speed, package, etc.) or for further information on any aspect
of this device, please contact your nearest ST sales office.


<u>186/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Application block diagrams**

# **Appendix A Application block diagrams**

## **A.1 USB OTG full speed (FS) interface solutions**

### **Figure 85. USB controller configured as peripheral-only and used**

**<u>in Full speed mode</u>**















1. External voltage regulator only needed when building a VBUS powered device.

2. The same application can be developed using the OTG HS in FS mode to achieve enhanced performance
thanks to the large Rx/Tx FIFO and to a dedicated DMA controller.

### **Figure 86. USB controller configured as host-only and used in full speed mode**















1. The current limiter is required only if the application has to support a VBUS powered device. A basic power
switch can be used if 5 V are available on the application board.

2. The same application can be developed using the OTG HS in FS mode to achieve enhanced performance
thanks to the large Rx/Tx FIFO and to a dedicated DMA controller.


<u>DS8626 Rev 12</u> <u>187/206</u>



191


**Application block diagrams** **STM32F405xx, STM32F407xx**

### **Figure 87. USB controller configured in dual mode and used in full speed mode**



















1. External voltage regulator only needed when building a VBUS powered device.

2. The current limiter is required only if the application has to support a VBUS powered device. A basic power
switch can be used if 5 V are available on the application board.

3. The ID pin is required in dual role only.

4. The same application can be developed using the OTG HS in FS mode to achieve enhanced performance
thanks to the large Rx/Tx FIFO and to a dedicated DMA controller.


<u>188/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Application block diagrams**

## **A.2 USB OTG high speed (HS) interface solutions**

### **Figure 88. USB controller configured as peripheral, host, or dual-mode**

**<u>and used in high speed mode</u>**
























|Col1|Col2|Col3|ULPI_CLK|
|---|---|---|---|
||||ULPI_D[7:0]|
||||ULPI_DIR|
||||ULPI_STP|
||||ULPI_NXT|
||||MCO1 or MCO2<br>24 or 26 MHz XT(1) <br>XT1|
|||||
|||||
|||||
|||||
|||||
|||||


|Col1|DP|
|---|---|
|High speed<br>OTG PHY<br>XI|DM|
|High speed<br>OTG PHY<br>XI|ID(2)|
|High speed<br>OTG PHY<br>XI|VBUS|
|High speed<br>OTG PHY<br>XI|VSS|



1. It is possible to use MCO1 or MCO2 to save a crystal. It is however not mandatory to clock the
STM32F40xxx with a 24 or 26 MHz crystal when using USB HS. The above figure only shows an example
of a possible connection.

2. The ID pin is required in dual role only.


<u>DS8626 Rev 12</u> <u>189/206</u>



191


**Application block diagrams** **STM32F405xx, STM32F407xx**

## **A.3 Ethernet interface solutions**

### **Figure 89. MII mode using a 25 MHz crystal**


























|Col1|MII_TX_CLK|
|---|---|
||MII_TX_EN|
||MII_TXD[3:0]|
||MII_CRS|
||MII_COL|
||MII_RX_CLK|
||MII_RXD[3:0]|
||MII_RX_DV|
||MII_RX_ER|
||MDIO|
||MDC|
||PHY_CLK 25 MHz<br><br>PPS_OUT(2)|



1. fHCLK must be greater than 25 MHz.

2. Pulse per second when using IEEE1588 PTP optional signal.

### **Figure 90. RMII with a 50 MHz oscillator**
























|Col1|Col2|RMII_TX_EN|Col4|
|---|---|---|---|
|||RMII_TXD[1:0]|RMII_TXD[1:0]|
|||RMII_RXD[1:0]|RMII_RXD[1:0]|
|||RMII_CRX_DV|RMII_CRX_DV|
|||RMII_REF_CLK<br>MDIO|RMII_REF_CLK<br>MDIO|
|||MDIO|MDIO|
|||MDC||
|||MDC|50 MHz|





1. fHCLK must be greater than 25 MHz.


<u>190/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Application block diagrams**

### **Figure 91. RMII with a 25 MHz crystal and PHY with PLL**




























|Col1|Col2|RMII_TX_EN|Col4|
|---|---|---|---|
|||RMII_TXD[1:0]|RMII_TXD[1:0]|
|||RMII_RXD[1:0]|RMII_RXD[1:0]|
|||RMII_CRX_DV|RMII_CRX_DV|
|||RMII_REF_CLK|RMII_REF_CLK|
|||MDIO|XT1<br>P|
|||MDC|MDC|
|||PHY_CLK   25 MHz<br>|PHY_CLK   25 MHz<br>|



1. fHCLK must be greater than 25 MHz.

2. The 25 MHz (PHY_CLK) must be derived directly from the HSE oscillator, before the PLL block.


<u>DS8626 Rev 12</u> <u>191/206</u>



191


**Important security notice** **STM32F405xx, STM32F407xx**

# **9 Important security notice**


The STMicroelectronics group of companies (ST) places a high value on product security,
which is why the ST product(s) identified in this documentation may be certified by various
security certification bodies and/or may implement our own security measures as set forth
herein. However, no level of security certification and/or built-in security measures can
guarantee that ST products are resistant to all forms of attacks. As such, it is the
responsibility of each of ST's customers to determine if the level of security provided in an
ST product meets the customer needs both in relation to the ST product alone, as well as
when combined with other components and/or software for the customer end product or
application. In particular, take note that:

      - ST products may have been certified by one or more security certification bodies, such
as Platform Security Architecture (www.psacertified.org) and/or Security Evaluation
standard for IoT Platforms (www.trustcb.com). For details concerning whether the ST
product(s) referenced herein have received security certification along with the level
and current status of such certification, either visit the relevant certification standards
website or go to the relevant product page on www.st.com for the most up to date
information. As the status and/or level of security certification for an ST product can
change from time to time, customers should re-check security certification status/level
as needed. If an ST product is not shown to be certified under a particular security
standard, customers should not assume it is certified.

      - Certification bodies have the right to evaluate, grant and revoke security certification in
relation to ST products. These certification bodies are therefore independently
responsible for granting or revoking security certification for an ST product, and ST
does not take any responsibility for mistakes, evaluations, assessments, testing, or
other activity carried out by the certification body with respect to any ST product.

      - Industry-based cryptographic algorithms (such as AES, DES, or MD5) and other open
standard technologies which may be used in conjunction with an ST product are based
on standards which were not developed by ST. ST does not take responsibility for any
flaws in such cryptographic algorithms or open technologies or for any methods which
have been or may be developed to bypass, decrypt or crack such algorithms or
technologies.

      - While robust security testing may be done, no level of certification can absolutely
guarantee protections against all attacks, including, for example, against advanced
attacks which have not been tested for, against new or unidentified forms of attack, or
against any form of attack when using an ST product outside of its specification or
intended use, or in conjunction with other components or software which are used by
customer to create their end product or application. ST is not responsible for resistance
against such attacks. As such, regardless of the incorporated security features and/or
any information or support that may be provided by ST, each customer is solely
responsible for determining if the level of attacks tested for meets their needs, both in
relation to the ST product alone and when incorporated into a customer end product or
application.

      - All security features of ST products (inclusive of any hardware, software,
documentation, and the like), including but not limited to any enhanced security
features added by ST, are provided on an "AS IS" BASIS. AS SUCH, TO THE EXTENT
PERMITTED BY APPLICABLE LAW, ST DISCLAIMS ALL WARRANTIES, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, unless the
applicable written and signed contract terms specifically provide otherwise.


<u>192/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Revision history**

# **10 Revision history**

## **Table 99. Document revision history**





|Date|Revision|Changes|
|---|---|---|
|15-Sep-2011|1|Initial release.|
|24-Jan-2012|2|Added WLCSP90 package on cover page.<br>Renamed USART4 and USART5 into UART4 and UART5,<br>respectively.<br>Updated number of USB OTG HS and FS in Table 3: STM32F405xx<br>and STM32F407xx: features and peripheral counts.<br>Updated Figure 3: Compatible board design between<br>STM32F10xx/STM32F2/STM32F40xxx for LQFP144 package and<br>Figure 4: Compatible board design between STM32F2 and<br>STM32F40xxx for LQFP176 and BGA176 packages, and removed<br>note 1 and 2.<br>Updated Section 3.0.9: Flexible static memory controller (FSMC).<br>Modified I/Os used to reprogram the flash memory for CAN2 and USB<br>OTG FS in Section 3.0.13: Boot modes.<br>Updated note in Section 3.0.14: Power supply schemes.<br>PDR_ON no more available on LQFP100 package. Updated Section<br>3.0.16: Voltage regulator. Updated condition to obtain a minimum<br>supply voltage of 1.7 V in the whole document.<br>Renamed USART4/5 to UART4/5 and added LIN and IrDA feature for<br>UART4 and UART5 in Table 6: USART feature comparison.<br>Removed support of I2C for OTG PHY in Section 3.0.30: Universal<br>serial bus on-the-go full-speed (OTG_FS).<br>Added Table 7: Legend/abbreviations used in the pinout table.<br>Table 8: STM32F40xxx pin and ball definitions: replaced VSS_3,<br>VSS_4, and VSS_8 by VSS; reformatted Table 8: STM32F40xxx pin<br>and ball definitions to better highlight I/O structure, and alternate<br>functions versus additional functions; signal corresponding to<br>LQFP100 pin 99 changed from PDR_ON to VSS; EVENTOUT added<br>in the list of alternate functions for all I/Os; ADC3_IN8 added as<br>alternate function for PF10; FSMC_CLE and FSMC_ALE added as<br>alternate functions for PD11 and PD12, respectively; PH10 alternate<br>function TIM15_CH1_ETR renamed TIM5_CH1; updated PA4 and PA5<br>I/O structure to TTa.<br>Removed OTG_HS_SCL, OTG_HS_SDA, OTG_FS_INTN in Table 8:<br>STM32F40xxx pin and ball definitions and Table 10: Alternate function<br>mapping.<br>Changed TCM data RAM to CCM data RAM in Figure 18:<br>STM32F40xxx memory map.<br>Added IVDD and IVSS maximum values in Table 14: Current<br>characteristics.<br>Added Note 1 related to fHCLK, updated Note 2 in Table 16: General<br>operating conditions, and added maximum power dissipation values.<br>Updated Table 17: Limitations depending on the operating power<br>supply range.|


<u>DS8626 Rev 12</u> <u>193/206</u>



205


**Revision history** **STM32F405xx, STM32F407xx**


**<u>Table 99. Document revision history (continued)</u>**






|Date|Revision|Changes|
|---|---|---|
|24-Jan-2012|2<br>(continued)|Added V12 in Table 21: Embedded reset and power control block<br>characteristics.<br>Updated Table 23: Typical and maximum current consumption in Run<br>mode, code with data processing   running from flash memory (ART<br>accelerator disabled) and Table 22: Typical and maximum current<br>consumption in Run mode, code with data processing   running from<br>flash memory (ART accelerator enabled) or RAM. Added Figure ,<br>Figure 25, Figure 26, and Figure 27.<br>Updated Table 24: Typical and maximum current consumption in Sleep<br>mode and removed Note 1.<br>Updated Table 25: Typical and maximum current consumptions in Stop<br>mode and Table 26: Typical and maximum current consumptions in<br>Standby mode, Table 27: Typical and maximum current consumptions<br>in VBAT mode, and Table 29: Switching output I/O current<br>consumption.<br>Section : On-chip peripheral current consumption: modified conditions,<br>and updated Table 30: Peripheral current consumption and Note 2.<br>Changed fHSE_ext to 50 MHz and tr(HSE)/tf(HSE) maximum value in<br>Table 32: High-speed external user clock characteristics.<br>Added Cin(LSE) in Table 33: Low-speed external user clock<br>characteristics.<br>Updated maximum PLL input clock frequency, removed related note,<br>and deleted jitter for MCO for RMII Ethernet typical value in Table 38:<br>Main PLL characteristics. Updated maximum PLLI2S input clock<br>frequency and removed related note in Table 39: PLLI2S (audio PLL)<br>characteristics.<br>Updated Section : Flash memory to specify that the devices are<br>shipped to customers with the flash memory erased. Updated Table 41:<br>Flash memory characteristics, and added tME in Table 42: Flash<br>memory programming.<br>Updated Table 45: EMS characteristics, and Table 46: EMI<br>characteristics.<br>Updated Table 58: I2S dynamic characteristics<br>Updated Figure 45: ULPI timing diagram and Table 64: ULPI timing.<br>Added tCOUNTER and tMAX_COUNT in Table 54: Characteristics of<br>TIMx connected to the APB1 domain and Table 55: Characteristics of<br>TIMx connected to the APB2 domain. Updated Table 67: Dynamic<br>characteristics: Ethernet MAC signals for RMII.<br>Removed USB-IF certification in Section : USB OTG FS<br>characteristics.|



<u>194/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Revision history**


**<u>Table 99. Document revision history (continued)</u>**





|Date|Revision|Changes|
|---|---|---|
|24-Jan-2012|2<br>(continued)|Updated Table 63: USB HS clock timing parameters<br>Updated Table 69: ADC characteristics.<br>Updated Table 70: ADC accuracy at fADC = 30 MHz.<br>Updated Note 1 in Table 76: DAC characteristics.<br>Section 6.3.26: FSMC characteristics: updated Table 77 toTable 88,<br>changed CL value to 30 pF, and modified FSMC configuration for<br>asynchronous timings and waveforms. Updated Figure 59:<br>Synchronous multiplexed PSRAM write timings.<br>Updated Table 100: Package thermal characteristics.<br>Appendix A.1: USB OTG full speed (FS) interface solutions: modified<br>Figure 93: USB controller configured as peripheral-only and used in<br>Full speed mode added Note 2, updated Figure 94: USB controller<br>configured as host-only and used in full speed mode and added Note<br>2, changed Figure 95: USB controller configured in dual mode and<br>used in full speed mode and added Note 3.<br>Appendix A.2: USB OTG high speed (HS) interface solutions: removed<br>figures USB OTG HS device-only connection in FS mode and USB<br>OTG HS host-only connection in FS mode, and updated Figure 96:<br>USB controller configured as peripheral, host, or dual-mode and used<br>in high speed mode and added Note 2.<br>Added Appendix A.3: Ethernet interface solutions.|


<u>DS8626 Rev 12</u> <u>195/206</u>



205


**Revision history** **STM32F405xx, STM32F407xx**


**<u>Table 99. Document revision history (continued)</u>**






|Date|Revision|Changes|
|---|---|---|
|31-May-2012|3|Updated Figure 5: STM32F40xxx block diagram and Figure 7: Power<br>supply supervisor interconnection with internal reset OFF<br>Added SDIO, added notes related to FSMC and SPI/I2S in Table 3:<br>STM32F405xx and STM32F407xx: features and peripheral counts.<br>Starting from Silicon revision Z, USB OTG full-speed interface is now<br>available for all STM32F405xx devices.<br>Added full information on WLCSP90 package together with<br>corresponding part numbers.<br>Changed number of AHB buses to 3.<br>Modified available flash memory sizes in Section 3.0.4: Embedded<br>flash memory.<br>Modified number of maskable interrupt channels in Section 3.0.10:<br>Nested vectored interrupt controller (NVIC).<br>Updated case of Regulator ON/internal reset ON, Regulator<br>ON/internal reset OFF, and Regulator OFF/internal reset ON in Section<br>3.0.16: Voltage regulator.<br>Updated standby mode description in Section 3.0.19: Low-power<br>modes.<br>Added Note 1 below Figure 16: STM32F40xxx UFBGA176 ballout.<br>Added Note 1 below Figure 17: STM32F40xxx WLCSP90 ballout.<br>Updated Table 8: STM32F40xxx pin and ball definitions.<br>Added Table 9: FSMC pin definition.<br>Removed OTG_HS_INTN alternate function in Table 8: STM32F40xxx<br>pin and ball definitions and Table 10: Alternate function mapping.<br>Removed I2S2_WS on PB6/AF5 in Table 10: Alternate function<br>mapping.<br>Replaced JTRST by NJTRST, removed ETH_RMII _TX_CLK, and<br>modified I2S3ext_SD on PC11 in Table 10: Alternate function<br>mapping.<br>Added Table 12: register boundary addresses.<br>Updated Figure 18: STM32F40xxx memory map.<br>Updated VDDA and VREF+ decoupling capacitor in Figure 21: Power<br>supply scheme.<br>Added power dissipation maximum value for WLCSP90 in Table 16:<br>General operating conditions.<br>Updated VPOR/PDR in Table 21: Embedded reset and power control<br>block characteristics.<br>Updated notes in Table 23: Typical and maximum current consumption<br>in Run mode, code with data processing   running from flash memory<br>(ART accelerator disabled), Table 22: Typical and maximum current<br>consumption in Run mode, code with data processing   running from<br>flash memory (ART accelerator enabled) or RAM, and Table 24:<br>Typical and maximum current consumption in Sleep mode.<br>Updated maximum current consumption at TA = 25 °n Table 25:<br>Typical and maximum current consumptions in Stop mode.|



<u>196/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Revision history**


**<u>Table 99. Document revision history (continued)</u>**





|Date|Revision|Changes|
|---|---|---|
|31-May-2012|3 <br>(continued)|Removed fHSE_ext typical value in Table 32: High-speed external user<br>clock characteristics. Updated Table 34: HSE 4-26 MHz oscillator<br>characteristics and Table 35: LSE oscillator characteristics (fLSE =<br>32.768 kHz).<br>Added fPLL48_OUT maximum value in Table 38: Main PLL<br>characteristics.<br>Modified equation 1 and 2 in Section 6.3.11: PLL spread spectrum<br>clock generation (SSCG) characteristics.<br>Updated Table 41: Flash memory characteristics, Table 42: Flash<br>memory programming, and Table 43: Flash memory programming with<br>VPP.<br>Updated Section : Output driving current.<br>Table 56: I2C characteristics: Note 4 updated and applied to th(SDA) in<br>Fast mode, and removed note 4 related to th(SDA) minimum value.<br>Updated Table 69: ADC characteristics. Updated note concerning ADC<br>accuracy vs. negative injection current below Table 70: ADC accuracy<br>at fADC = 30 MHz.<br>Added WLCSP90 thermal resistance in Table 100: Package thermal<br>characteristics.<br>Updated Table 92: WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch<br>wafer level chip scale package mechanical data.<br>Updated Figure 87: UFBGA176+25 ball, 10 x 10 mm, 0.65 mm pitch,<br>ultra fine pitch ball grid array package outline and Table 97:<br>UFBGA176+25 ball, 10 × 10 × 0.65 mm pitch, ultra thin fine pitch ball<br>grid array mechanical data.<br>Added Figure 91: LQFP176 - 176-pin, 24 x 24 mm low profile quad flat<br>recommended footprint.<br>Removed 256 and 768 Kbyte flash memory density from Table : .|


<u>DS8626 Rev 12</u> <u>197/206</u>



205


**Revision history** **STM32F405xx, STM32F407xx**


**<u>Table 99. Document revision history (continued)</u>**






|Date|Revision|Changes|
|---|---|---|
|04-Jun-2013|4|Modified Note 1 below Table 3: STM32F405xx and STM32F407xx:<br>features and peripheral counts.<br>Updated Figure 4 title.<br>Updated Note 3 below Figure 21: Power supply scheme.<br>Changed simplex mode into half-duplex mode in Section 3.0.25: Inter-<br>integrated sound (I2S).<br>Replaced DAC1_OUT and DAC2_OUT by DAC_OUT1 and<br>DAC_OUT2, respectively.<br>Updated pin 36 signal in Figure 15: STM32F40xxx LQFP176 pinout.<br>Changed pin number from F8 to D4 for PA13 pin in Table 8:<br>STM32F40xxx pin and ball definitions.<br>Replaced TIM2_CH1/TIM2_ETR by TIM2_CH1_ETR for PA0 and PA5<br>pins in Table 10: Alternate function mapping.<br>Changed system memory into System memory + OTP in Figure 18:<br>STM32F40xxx memory map.<br>Added Note 1 below Table 18: VCAP_1/VCAP_2 operating conditions.<br>Updated IDDA description in Table 76: DAC characteristics.<br>Removed PA9/PB13 connection to VBUS in Figure 93: USB controller<br>configured as peripheral-only and used in Full speed mode and Figure<br>94: USB controller configured as host-only and used in full speed<br>mode.<br>Updated SPI throughput on front page and Section 3.0.24: Serial<br>peripheral interface (SPI)<br>Updated operating voltages in Table 3: STM32F405xx and<br>STM32F407xx: features and peripheral counts.<br>Updated note in Section 3.0.14: Power supply schemes<br>Updated Section 3.0.15: Power supply supervisor<br>Updated “Regulator ON” paragraph in Section 3.0.16: Voltage<br>regulator<br>Removed note in Section 3.0.19: Low-power modes<br>Corrected wrong reference manual in Section 3.0.28: Ethernet MAC<br>interface with dedicated DMA and IEEE 1588 support<br>Updated Table 17: Limitations depending on the operating power<br>supply range<br>Updated Table 26: Typical and maximum current consumptions in<br>Standby mode<br>Updated Table 27: Typical and maximum current consumptions in<br>VBAT mode<br>Updated Table 39: PLLI2S (audio PLL) characteristics<br>Updated Table 46: EMI characteristics<br>Updated Table 51: Output voltage characteristics<br>Updated Table 53: NRST pin characteristics<br>Updated Table 57: SPI dynamic characteristics<br>Updated Table 58: I2S dynamic characteristics<br>Deleted Table 59<br>Updated Table 64: ULPI timing<br>Updated Figure 46: Ethernet SMI timing diagram|



<u>198/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Revision history**


**<u>Table 99. Document revision history (continued)</u>**





|Date|Revision|Changes|
|---|---|---|
|04-Jun-2013|4<br>(continued)|Updated Figure 87: UFBGA176+25 ball, 10 x 10 mm, 0.65 mm pitch,<br>ultra fine pitch ball grid array package outline<br>Updated Table 97: UFBGA176+25 ball, 10 × 10 × 0.65 mm pitch, ultra<br>thin fine pitch ball grid array mechanical data<br>Updated Figure 5: STM32F40xxx block diagram<br>Updated Section 2: Description<br>Updated footnote (3) in Table 3: STM32F405xx and STM32F407xx:<br>features and peripheral counts.<br>Updated Figure 3: Compatible board design between<br>STM32F10xx/STM32F2/STM32F40xxx for LQFP144 package<br>Updated Figure 4: Compatible board design between STM32F2 and<br>STM32F40xxx for LQFP176 and BGA176 packages<br>Updated Section 3.0.14: Power supply schemes<br>Updated Section 3.0.15: Power supply supervisor<br>Updated Section 3.0.16: Voltage regulator, including figures.<br>Updated Table 16: General operating conditions, including footnote (2).<br>Updated Table 17: Limitations depending on the operating power<br>supply range, including footnote (3).<br>Updated footnote (1) in Table 69: ADC characteristics.<br>Updated footnote (2) in Table 70: ADC accuracy at fADC = 30 MHz.<br>Updated footnote (1) in Table 76: DAC characteristics.<br>Updated Figure 9: Regulator OFF.<br>Updated Figure 7: Power supply supervisor interconnection with<br>internal reset OFF.<br>Added Section 3.0.17: Regulator ON/OFF and internal reset ON/OFF<br>availability.<br>Updated footnote (2) of Figure 21: Power supply scheme.<br>Replaced respectively “I2S3S_WS" by "I2S3_WS”, “I2S3S_CK” by<br>“I2S3_CK” and “FSMC_BLN1” by “FSMC_NBL1” in Table 10: Alternate<br>function mapping.<br>Added “EVENTOUT” as alternate function “AF15” for pin PC13, PC14,<br>PC15, PH0, PH1, PI8 in Table 10: Alternate function mapping<br>Replaced “DCMI_12” by “DCMI_D12” in Table 8: STM32F40xxx pin<br>and ball definitions.<br>Removed the following sentence from Section : I2C interface<br>characteristics: ”Unless otherwise specified, the parameters<br>given in Table 56 are derived from tests performed under the<br>ambient temperature, fPCLK1 frequency and VDD supply<br>voltage conditions summarized in Table 16.”.<br>In_Table 8: STM32F40xxx pin and ball definitions on page 53_:<br>– For pin PC13, replaced “RTC_AF1” by “RTC_OUT, RTC_TAMP1,<br>RTC_TS”<br>– for pin PI8, replaced “RTC_AF2” by “RTC_TAMP1, RTC_TAMP2,<br>RTC_TS”.<br>– for pin PB15, added RTC_REFIN in Alternate functions column.<br>In_Table 10: Alternate function mapping on page 70_, for port<br>PB15, replaced “RTC_50Hz” by “RTC_REFIN”.|


<u>DS8626 Rev 12</u> <u>199/206</u>



205


**Revision history** **STM32F405xx, STM32F407xx**


**<u>Table 99. Document revision history (continued)</u>**






|Date|Revision|Changes|
|---|---|---|
|04-Jun-2013|4<br>(continued)|Updated Figure 6: Multi-AHB matrix.<br>Updated Figure 7: Power supply supervisor interconnection with<br>internal reset OFF<br>Changed 1.2 V to V12 in Section : Regulator OFF<br>Updated LQFP176 pin 48.<br>Updated Section 1: Introduction.<br>Updated Section 2: Description.<br>Updated operating voltage in Table 3: STM32F405xx and<br>STM32F407xx: features and peripheral counts.<br>Updated Note 1.<br>Updated Section 3.0.15: Power supply supervisor.<br>Updated Section 3.0.16: Voltage regulator.<br>Updated Figure 9: Regulator OFF.<br>Updated Table 4: Regulator ON/OFF and internal reset ON/OFF<br>availability.<br>Updated Section 3.0.19: Low-power modes.<br>Updated Section 3.0.20: VBAT operation.<br>Updated Section 3.0.22: Inter-integrated circuit interface (I²C) .<br>Updated pin 48 in Figure 15: STM32F40xxx LQFP176 pinout.<br>Updated Table 7: Legend/abbreviations used in the pinout table.<br>Updated Table 8: STM32F40xxx pin and ball definitions.<br>Updated Table 16: General operating conditions.<br>Updated Table 17: Limitations depending on the operating power<br>supply range.<br>Updated Section 6.3.7: Wakeup time from low-power mode.<br>Updated Table 36: HSI oscillator characteristics.<br>Updated Section 6.3.15: I/O current injection characteristics.<br>Updated Table 50: I/O static characteristics.<br>Updated Table 53: NRST pin characteristics.<br>Updated Table 56: I2C characteristics.<br>Updated Figure 39: I2C bus AC waveforms and measurement circuit.<br>Updated Section 6.3.19: Communications interfaces.<br>Updated Table 69: ADC characteristics.<br>Added Table 72: Temperature sensor calibration values.<br>Added Table 75: Internal reference voltage calibration values.<br>Updated Section 6.3.26: FSMC characteristics.<br>Updated Section 6.3.28: SD/SDIO MMC card host interface (SDIO)<br>characteristics.<br>Updated Table 25: Typical and maximum current consumptions in Stop<br>mode.<br>Updated Section : SPI interface characteristics included Table 57.<br>Updated Section : I2S interface characteristics included Table 58.<br>Updated Table 66: Dynamic characteristics: Ethernet MAC signals for<br>SMI.<br>Updated Table 68: Dynamic characteristics: Ethernet MAC signals for<br>MII.|



<u>200/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Revision history**


**<u>Table 99. Document revision history (continued)</u>**





|Date|Revision|Changes|
|---|---|---|
|04-Jun-2013|4<br>(continued)|Updated Table 66: Dynamic characteristics: Ethernet MAC signals for<br>SMI.<br>Updated Table 68: Dynamic characteristics: Ethernet MAC signals for<br>MII.<br>Updated Table 81: Synchronous multiplexed NOR/PSRAM read<br>timings.<br>Updated Table 82: Synchronous multiplexed PSRAM write timings.<br>Updated Table 83: Synchronous non-multiplexed NOR/PSRAM read<br>timings.<br>Updated Table 84: Synchronous non-multiplexed PSRAM write<br>timings.<br>Updated Section 6.3.27: Camera interface (DCMI) timing specifications<br>including Table 89: DCMI characteristics and addition of Figure 72:<br>DCMI timing diagram.<br>Updated Section 6.3.28: SD/SDIO MMC card host interface (SDIO)<br>characteristics including Table 90.<br>Updated Chapter Figure 9.|


<u>DS8626 Rev 12</u> <u>201/206</u>



205


**Revision history** **STM32F405xx, STM32F407xx**


**<u>Table 99. Document revision history (continued)</u>**






|Date|Revision|Changes|
|---|---|---|
|06-Mar-2015|5|Replace Cortex-M4F by Cortex-M4 with FPU throughout the<br>document.<br>Updated Section : Regulator OFF and Table 4: Regulator ON/OFF and<br>internal reset ON/OFF availability for LQFP176.<br>Updated Figure 15: STM32F40xxx LQFP176 pinout and Table 8:<br>STM32F40xxx pin and ball definitions.<br>Updated Figure 6: Multi-AHB matrix.<br>Added note 1 below Figure 12: STM32F40xxx LQFP64 pinout, Figure<br>13: STM32F40xxx LQFP100 pinout, Figure 14: STM32F40xxx<br>LQFP144 pinout and Figure 15: STM32F40xxx LQFP176 pinout.<br>Updated IVDD and IVSS in Table 14: Current characteristics.<br>Updated PLS[2:0]=101 (falling edge) configuration in Table 21:<br>Embedded reset and power control block characteristics.<br>Added Section : Additional current consumption. Updated Section :<br>On-chip peripheral current consumption.<br>Updated Table 31: Low-power mode wakeup timings.<br>Updated Table 34: HSE 4-26 MHz oscillator characteristics and Table<br>35: LSE oscillator characteristics (fLSE = 32.768 kHz).<br>Changed condition related to VESD(CDM) in Table 47: ESD absolute<br>maximum ratings.<br>Updated Table 49: I/O current injection susceptibility, Table 50: I/O<br>static characteristics, Table 51: Output voltage characteristics<br>conditions, Table 52: I/O AC characteristics and Figure 37: I/O AC<br>characteristics definition.<br>Updated Section : I2C interface characteristics.<br>Remove note 3 in Table 71: Temperature sensor characteristics.<br>Updated Figure 72: DCMI timing diagram.<br>Modified Figure 75: WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch<br>wafer level chip scale package outline and Table 92: WLCSP90 - 4.223<br>x 3.969 mm, 0.400 mm pitch wafer level chip scale package<br>mechanical data. Added Figure 76: WLCSP90 - 4.223 x 3.969 mm,<br>0.400 mm pitch wafer level chip scale recommended footprint and<br>Table 93: WLCSP90 recommended PCB design rules. /<br>Modified Figure 78: LQFP64 – 64-pin, 10 x 10 mm low-profile quad flat<br>package outline and Table 94: LQFP64 – 64-pin 10 x 10 mm low-profile<br>quad flat package  mechanical data.<br>Updated Figure 87: UFBGA176+25 ball, 10 x 10 mm, 0.65 mm pitch,<br>ultra fine pitch ball grid array package outline and Table 97:<br>UFBGA176+25 ball, 10 × 10 × 0.65 mm pitch, ultra thin fine pitch ball<br>grid array mechanical data. Added Figure 88: UFBGA176+25 - 201-<br>ball, 10 x 10 mm, 0.65 mm pitch, ultra fine pitch ball grid array<br>recommended footprint and Table 98: UFBGA176+25 recommended<br>PCB design rules (0.65 mm pitch BGA).<br>Updated Figure 90: LQFP176 - 176-pin, 24 x 24 mm low profile quad<br>flat package outline.<br>Added Section : Device marking for WLCSP90, Section : Device<br>marking for LQFP64, Section : Device marking for LFP100, Section :<br>Device marking for LQFP144, Section : Device marking for<br>UFBGA176+25 and Section : Device marking for LQFP176.|



<u>202/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Revision history**


**<u>Table 99. Document revision history (continued)</u>**





|Date|Revision|Changes|
|---|---|---|
|22-Oct-2015|6|In the whole document, updated notes related to values specified by<br>design or by characterization.<br>Updated Table 36: HSI oscillator characteristics.<br>Changed fVCO_OUT minimum value and VCO freq to 100 MHz in<br>Table 38: Main PLL characteristics and Table 39: PLLI2S (audio PLL)<br>characteristics.<br>Updated Figure 39: SPI timing diagram - slave mode and CPHA = 0.<br>Updated Figure 53: 12-bit buffered /non-buffered DAC.<br>Removed note 1 related to better performance using a restricted VDD<br>range in Table 70: ADC accuracy at fADC = 30 MHz.<br>Upated Figure 84: LQFP144 - 144-pin, 20 x 20 mm low-profile quad flat<br>package outline.<br>Updated Figure 87: UFBGA176+25 ball, 10 x 10 mm, 0.65 mm pitch,<br>ultra fine pitch ball grid array package outline and Table 97:<br>UFBGA176+25 ball, 10 × 10 × 0.65 mm pitch, ultra thin fine pitch ball<br>grid array mechanical data.|
|16-Mar-2016|7|Updated Figure 2: Compatible board design<br>STM32F10xx/STM32F2/STM32F40xxx for LQFP100 package.<br>Updated |VSSX- VSS| in Table 13: Voltage characteristics to add<br>VREF-.<br>Added VREF- in Table 69: ADC characteristics.<br>Updated Table 92: WLCSP90 - 4.223 x 3.969 mm, 0.400 mm pitch<br>wafer level chip scale package mechanical data.|
|09-Sep-2016|8|Removed note 1 below Figure 5: STM32F40xxx block diagram.<br>Updated definition of stresses above maximum ratings in Section 6.2:<br>Absolute maximum ratings.<br>Updated th(NSS) in Figure 39: SPI timing diagram - slave mode and<br>CPHA = 0 and Figure 40: SPI timing diagram - slave mode and CPHA<br>= 1.<br>Added note related to optional marking and inset/upset marks in all<br>package marking sections.<br>Updated Figure 87: UFBGA176+25 ball, 10 x 10 mm, 0.65 mm pitch,<br>ultra fine pitch ball grid array package outline and Table 97:<br>UFBGA176+25 ball, 10 × 10 × 0.65 mm pitch, ultra thin fine pitch ball<br>grid array mechanical data.|


<u>DS8626 Rev 12</u> <u>203/206</u>



205


**Revision history** **STM32F405xx, STM32F407xx**


**<u>Table 99. Document revision history (continued)</u>**






|Date|Revision|Changes|
|---|---|---|
|14-Aug-2020|9|Renamed Section 3 and Section 8 into Functional overview and<br>Ordering information, respectively.<br>Added Arm logo and legal notice in Section 1: Introduction and<br>updated Arm wordmark in the whole document. Removed USB<br>certified logos.<br>Updated camera interfaces for STM32F405OE in Table 3:<br>STM32F405xx and STM32F407xx: features and peripheral counts.<br>Added OTP memory in Features and Section 3.0.4: Embedded flash<br>memory.<br>Changed random number generator to true random number generator<br>in the whole document and updated Section 3.0.34: True random<br>number generator (RNG).<br>Added Note 1 related to UFBGA176 in Table 8: STM32F40xxx pin and<br>ball definitions.<br>Updated Section 6.2: Absolute maximum ratings introduction.<br>Updated VPVD minimum value for PLS[2:0]=101 (falling edge) in Table<br>21: Embedded reset and power control block characteristics.<br>Updated Note 1 in Table 36: HSI oscillator characteristics.<br>Added reference to application note AN4899 in Section 6.3.16: I/O port<br>characteristics.<br>Replaced DCMI_PIXCK by DCMI_PIXCLK in Table 10: Alternate<br>function mapping.<br>Renamed Section 8 into Ordering information.<br>Updated D1 in Figure 87: UFBGA176+25 ball, 10 x 10 mm, 0.65 mm<br>pitch, ultra fine pitch ball grid array package outline.|



<u>204/206</u> <u>DS8626 Rev 12</u>


**STM32F405xx, STM32F407xx** **Revision history**


**<u>Table 99. Document revision history (continued)</u>**







|Date|Revision|Changes|
|---|---|---|
|08-Nov-2024|10|Updated:<br>– Cover page<br>– _Section 1: Introduction_<br>– _Figure 5: STM32F40xxx block diagram_<br>– _Section 3.18: Real-time clock (RTC), backup SRAM and backup_<br>_registers_<br>– _Table 7: STM32F40xxx pin and ball definitions_<br>– _Table 9: Alternate function mapping_<br>– _I/O system current consumption_<br>– _Note 1_ in_Table 34: HSI oscillator characteristics_.<br>– _Table 33: LSE oscillator characteristics (fLSE = 32.768 kHz)_<br>– _Figure 37: I/O AC characteristics definition_<br>– _Figure 39: SPI timing diagram - slave mode and CPHA = 0_, <br>_Figure 40: SPI timing diagram - slave mode and CPHA = 1_, and<br>_Figure 41: SPI timing diagram - master mode_<br>– _Table 44: EMI characteristics for fHSE = 25 MH and fCPU =_<br>_168 MHz_<br>– _Figure 49: ADC accuracy characteristics_ and_Figure 50: Typical_<br>_connection diagram when using the ADC with FT/TT pins featuring_<br>_analog switch function_<br>– _Figure 68: NAND controller waveforms for read access_ and<br>_Figure 69: NAND controller waveforms for write access_<br>– _Table 96: UFBGA(176+25) - Example of PCB design rules (0.65 mm_<br>_pitch BGA)_ title<br>– _Section 7: Package information_<br>Added_Section 9: Important security notice_|
|04-Feb-2026|11|Updated_Figure 7: Power supply supervisor interconnection with_<br>_internal reset OFF_.<br>Updated_Figure 8: PDR_ON and NRST control with internal reset OFF_.<br>Updated_Figure 9: Regulator OFF_.<br>Updated_Figure 18: STM32F40xxx memory map_.<br>Updated_Figure 20: Pin input voltage_.<br>Updated_Table 45: ESD absolute maximum ratings_.<br>Updated_Section 7.3: LQFP64 package information (5W)_.|
|18-Mar-2026|12|Re-numbering of_Section 3: Functional overview_ sub-sections.|


<u>DS8626 Rev 12</u> <u>205/206</u>



205


**STM32F405xx, STM32F407xx**


**IMPORTANT NOTICE – READ CAREFULLY**


STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and
improvements to ST products and/or to this document at any time without notice.


In the event of any conflict between the provisions of this document and the provisions of any contractual arrangement in force between the
purchasers and ST, the provisions of such contractual arrangement shall prevail.


The purchasers should obtain the latest relevant information on ST products before placing orders. ST products are sold pursuant to ST’s
terms and conditions of sale in place at the time of order acknowledgment.


The purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application
assistance or the design of the purchasers’ products.


No license, express or implied, to any intellectual property right is granted by ST herein.


Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.


If the purchasers identify an ST product that meets their functional and performance requirements but that is not designated for the
purchasers' market segment, the purchasers shall contact ST for more information.


ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to www.st.com/trademarks. All other product
or service names are the property of their respective owners.


Information in this document supersedes and replaces information previously supplied in any prior versions of this document.


© 2026 STMicroelectronics – All rights reserved


<u>206/206</u> <u>DS8626 Rev 12</u>


