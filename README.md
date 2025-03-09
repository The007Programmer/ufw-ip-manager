# ufw-ip-manager

A simple tool for IP management on servers.

## Features
| Feature    | Implemented? |
| -------- | ------- |
|Can allow all IPs listed|✅|
|Stores and recieves IPs from JSON file|✅|
|Status commands (who is currently whitelisted)|❌|
|Interactive IP addition/removal|✅|
|Can clear DB of whitelisted or blacklisted users|❌|

## Usage

Download the ZIP file from the `CODE` tab, then run the shell file.

### Requirements
- `JQ` package for json handling

### Commits Key
- SAFE: Safe commit, latest code can be used
- UNST: Unstable commit, not to be used, solely for version control and code backup
- INCM: Safe but incomplete, not to be used
- HTFX: Hotfix for critical issue
- REFA: Refactored/Restructured code for better readability and/or efficiency
- RESD: Removed edits from latest previous commit, unstability issues occured after testing