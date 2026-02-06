# gScan — Google Dorking Automation Tool for OSINT & Recon

## Description
gScan is a lightweight Python-based Google dorking automation tool designed for OSINT, reconnaissance, and bug bounty workflows. It helps security researchers quickly generate targeted Google search queries (dorks) to discover indexed subdomains, exposed files, login portals, and publicly accessible sensitive information.

This tool streamlines manual Google dorking by automating query generation and launching searches directly in the browser.

---

## Features
- Automated Google dork generation
- Subdomain discovery via search indexing
- Sensitive file discovery (PDF, logs, backups, configs)
- Login portal discovery
- Domain-focused search filtering
- Simple CLI-based workflow
- Browser-integrated search execution

---

## Installation

### Requirements
- Python 3.x
- pyfiglet
- printy

### Install gScan

## Clone the repository:

```
git clone https://github.com/0x9Fahad/gScan
cd gScan
```

## Install dependencies:
```
pip install pyfiglet
pip install printy
```

## Run the tool:
```
python3 gScan.py
```
## Usage

- Enter a target domain or IP address.

- Choose a search option from the menu.

- gScan will automatically open your browser and execute the selected Google dork.

## Example Use Cases

- Bug bounty reconnaissance

- OSINT investigations

- Discovering indexed sensitive files

- Finding login panels

- Subdomain discovery via search engines


## Disclaimer

This tool is intended for authorized security testing, OSINT, and educational purposes only. Users are responsible for complying with applicable laws and bug bounty program policies.

