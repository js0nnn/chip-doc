"""Download extra MCU datasheets from vendor sites into dataset/raw/.

Files are numbered after the existing ones. Anything that fails (some vendors
block scripted downloads) is listed at the end for manual download.
Usage: python scripts/download_datasheets.py
"""
import re
from pathlib import Path

import requests

RAW = Path(__file__).resolve().parents[1] / "dataset" / "raw"
MAX_BYTES = 100 * 2**20

DATASHEETS = {
    "STM32L476RG": "https://www.st.com/resource/en/datasheet/stm32l476rg.pdf",
    "STM32F030F4": "https://www.st.com/resource/en/datasheet/stm32f030f4.pdf",
    "STM32WB55RG": "https://www.st.com/resource/en/datasheet/stm32wb55rg.pdf",
    "ESP32-C3": "https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf",
    "ESP8266EX": "https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf",
    "ESP32-C6": "https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf",
    "ATmega2560": "https://ww1.microchip.com/downloads/en/devicedoc/atmel-2549-8-bit-avr-microcontroller-atmega640-1280-1281-2560-2561_datasheet.pdf",
    "ATmega32U4": "https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf",
    "PIC18F45K22": "https://ww1.microchip.com/downloads/en/DeviceDoc/40001412G.pdf",
    "SAM3X8E": "https://ww1.microchip.com/downloads/en/devicedoc/atmel-11057-32-bit-cortex-m3-microcontroller-sam3x-sam3a_datasheet.pdf",
    "MSP430G2553": "https://www.ti.com/lit/ds/symlink/msp430g2553.pdf",
    "CC2640R2F": "https://www.ti.com/lit/ds/symlink/cc2640r2f.pdf",
    "MSPM0G3507": "https://www.ti.com/lit/ds/symlink/mspm0g3507.pdf",
    "ESP32-S2": "https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf",
    "ESP32-H2": "https://www.espressif.com/sites/default/files/documentation/esp32-h2_datasheet_en.pdf",
    "MSP430FR2433": "https://www.ti.com/lit/ds/symlink/msp430fr2433.pdf",
    "CC2652R": "https://www.ti.com/lit/ds/symlink/cc2652r.pdf",
    "ATtiny1614": "https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-16-17-DataSheet-DS40002204A.pdf",
    "PIC32MX1XX": "https://ww1.microchip.com/downloads/en/DeviceDoc/PIC32MX1XX2XX-28-36-44-PIN-DS60001168L.pdf",
}

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}


def main():
    existing = {re.sub(r"^\d+_", "", p.stem): p for p in RAW.glob("*.pdf")}
    n = max(int(p.name.split("_")[0]) for p in RAW.glob("*.pdf"))
    failed = []
    for name, url in DATASHEETS.items():
        if name in existing:
            print(f"{name:14} already present")
            continue
        try:
            r = requests.get(url, headers=HEADERS, timeout=60)
            r.raise_for_status()
            if not r.content.startswith(b"%PDF-") or len(r.content) > MAX_BYTES:
                raise ValueError(f"not a PDF or too large ({r.headers.get('content-type')})")
        except Exception as e:
            failed.append((name, url, e))
            print(f"{name:14} FAILED: {e}")
            continue
        n += 1
        (RAW / f"{n}_{name}.pdf").write_bytes(r.content)
        print(f"{name:14} ok  {len(r.content) / 2**20:5.1f} MB")
    if failed:
        print("\nDownload these by hand into dataset/raw/ as <N>_<NAME>.pdf:")
        for name, url, _ in failed:
            print(f"  {name}: {url}")


if __name__ == "__main__":
    main()
