# UFW-Manager

A simple tool for IP management on servers. Currently this python file is executable exclusively on Debian-based servers, as the bash commands are specific to the filepath and syntax of Debian architecture.

## Features
| Feature    | Implemented? |
| -------- | ------- |
|Can allow all IPs listed|✅|
|Stores and recieves IPs from JSON file|✅|
|Status commands (who is currently whitelisted)|✅|
|Interactive IP addition/removal|✅|
|Windows Server support|✅|

## Installation and Usage

1. Download the ZIP file from the `CODE` tab in this repository.
2. Extract contents to desired run folder (move to server if downloaded on computer).
3. Open or `cd` to the project directory in a terminal.
4. Run `python3 tool.py` to open the tool.

### Requirements
- `Python 3.10+` for running the application.
- `json` python package for json handling.
- `os` python package for bash commands.
- `subprocess` for bash handling.

### Commits Key
- SAFE: Stable and production-ready code; can be safely deployed.
- TEST: Code meant for testing or experimental changes; safe but does not affect the main program directly; stable for version control.
- UNST: Unstable commit with potential issues; not suitable for production, used for backup or testing phases.
- HTFX: Hotfix for critical issues.
- REFA: Refactor or restructure code for improved readability, maintainability, or efficiency, with no changes to core functionality.
- RESD: Revert previous changes due to instability or issues encountered during testing; restores the code to a prior stable state.
- BUGF: Bug fix or issue resolution, fixing known problems in the code without adding new functionality.
- DOCS: Documentation update, including comments, README files, or other forms of documentation to improve clarity and understanding.