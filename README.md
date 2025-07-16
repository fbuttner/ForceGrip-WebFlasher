# ForceGrip Firmware Uploader (via Web Browser)

This tool allows you to install or update the firmware on your ForceGrip device directly from a compatible web browser. It uses the [ESP Web Tools](https://github.com/esphome/esp-web-tools) project to flash the device over a USB connection.

## User Instructions

Follow these steps to program your ForceGrip device.

### Requirements

1.  **A ForceGrip Device**: The hardware you want to program.
2.  **A USB-C Cable**: For connecting the device to your computer.
3.  **A Compatible Web Browser**:
    - Google Chrome
    - Microsoft Edge
    - *Other Chromium-based browsers may work but are not officially supported.*
4.  **Drivers**: For most modern operating systems (Windows 10/11, macOS, Linux), the USB drivers for the ESP32-C3 are installed automatically. If your device is not detected, you may need to install drivers for its USB-to-serial chip.

### Flashing Steps

1.  **Open the Web Tool**:
    - Go to `https://fbuttner.github.io/ForceGrip-WebFlasher` using Google Chrome or Microsoft Edge.

2.  **Connect to the Device**:
    - Connect the ForceGrip to your computer via USB. To flash it, you may need to press and **hold** the button on the ForceGrip while connecting it to your computer.
    - Click the `CONNECT` button on the web page.
    - A pop-up window will appear asking you to select a serial port. Choose the port corresponding to your ForceGrip device (e.g., `COM3` on Windows, `/dev/ttyUSB0` on Linux, `/dev/cu.usbserial-XXXX` on macOS) and click "Connect".


3.  **Install the Firmware**:
    - Once connected, the button will change to `INSTALL ForceGrip`. Click it.
    - You will be prompted to confirm the installation and erase the device. Choose **"INSTALL"**.
    - The tool will now erase the old firmware and flash the new version. Wait for the process to complete. It may take a minute or two.


4.  **Finish**:
    - Once the "Installation complete!" message appears, the process is done.
    - You can now unplug the ForceGrip from your computer.


## Troubleshooting

If you encounter issues, here are some common solutions:

-   **Device Not Detected**:
    -   Ensure you are using a USB-C **data** cable, not a charge-only cable.
    -   Try using a different USB port on your computer.
    -   Make sure you have correctly put the device into bootloader mode: disconnect the device, press and **hold** the button on the ForceGrip, then reconnect the USB cable while still holding the button.
    -   If the device is still not showing up, you may need to manually install the drivers mentioned in the "Requirements" section.

-   **Flashing Fails**:
    -   If the process fails, disconnect the device and repeat the connection steps, ensuring it's in bootloader mode before you click "CONNECT".
    -   Close any other programs that might be using the serial port (e.g., Arduino IDE, a serial monitor, etc.).
