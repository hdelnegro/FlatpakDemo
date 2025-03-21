# FlatpakDemo

## Overview
FlatpakDemo is a simple graphical application that demonstrates how to create a Flatpak package for a Python application running in a GNOME environment. The application displays a welcome message and includes a button to close the window.

## Project Structure
```
FlatpakDemo
├── .flatpak-builder
│   └── manifest.json
├── src
│   ├── main.py
│   └── assets
│       └── icon.svg
├── requirements.txt
└── README.md
```

## Requirements
- Python 3
- Flatpak
- Flatpak Builder

## Dependencies
The application requires the following Python packages:
- PyGObject

These dependencies are listed in the `requirements.txt` file.

## Building the Flatpak
To build the Flatpak application, navigate to the project directory and run the following command:

```
flatpak-builder --force-clean build-dir .flatpak-builder/manifest.json
```

## Running the Application
After building the Flatpak, you can run the application using:

```
flatpak run com.example.FlatpakDemo
```

## Icon
The application icon is located in the `src/assets/icon.svg` file and will be used in the GNOME activities menu.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.