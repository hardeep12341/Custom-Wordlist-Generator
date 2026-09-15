# Custom Wordlist Generator

A Python-based command-line tool for generating customized wordlists from user-provided information. The project is designed for **Capture The Flag (CTF) challenges, cybersecurity labs, and authorized security testing environments**.

## Overview

The Custom Wordlist Generator automates the creation of wordlist entries by combining user-provided keywords with configurable variations such as capitalization, numbers, separators, and special characters.

The project was developed as a practical exercise in **Python programming and cybersecurity automation**.

## Features

* Custom keyword collection
* Lowercase, uppercase, and capitalized variations
* Two-word combinations
* Three-word combinations
* Numeric variations
* Custom special characters
* Multiple separators (`_`, `-`, `.`)
* Duplicate removal
* Configurable generation options
* `.txt` wordlist export
* Simple command-line interface

## Technologies

* **Python 3**
* `itertools`
* File I/O
* Sets and lists
* String manipulation
* Command-line interface

## Project Structure

```text
custom-wordlist-generator/
│
├── wordlist_maker.py
├── README.md
└── .gitignore
```

## Requirements

* Python 3.x
* Linux, Kali Linux, macOS, or Windows

No third-party Python packages are required.

Check your Python installation:

```bash
python3 --version
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/custom-wordlist-generator.git
```

Navigate to the project:

```bash
cd custom-wordlist-generator
```

## Usage

Run the program:

```bash
python3 wordlist_maker.py
```

The program collects optional information such as:

```text
Name / Nickname
Favorite Game
Favorite Song / Artist
Pet Name
City
Favorite Team
Important Year
```

You can then configure the generation options:

```text
Use numbers? (y/n)
Use special characters? (y/n)
Generate 2-word combinations? (y/n)
Generate 3-word combinations? (y/n)
```

The generated wordlist can be saved with a custom filename or the default:

```text
wordlist.txt
```

## Example

Example input:

```text
Name / Nickname: alex
Favorite Game: mario
Favorite Song / Artist: queen
Pet Name: rocky
City: delhi
Favorite Team: united
Important Year: 2000
```

Example configuration:

```text
Use numbers? (y/n): y
Use special characters? (y/n): y
Generate 2-word combinations? (y/n): y
Generate 3-word combinations? (y/n): y
```

The program then generates customized combinations according to the selected options.

## Learning Outcomes

This project demonstrates practical experience with:

* Python programming fundamentals
* Functions and modular code
* Loops and conditional logic
* Lists and sets
* String manipulation
* File handling
* `itertools.permutations()`
* Duplicate elimination
* CLI-based tool development
* Basic cybersecurity automation

## Use Cases

This tool can be used in controlled environments for:

* CTF challenges
* Cybersecurity training labs
* Authorized penetration-testing exercises
* Security research
* Python automation practice

## Future Improvements

Planned enhancements:

* [ ] Interactive menu interface
* [ ] Custom number ranges
* [ ] Prefix and suffix configuration
* [ ] Maximum wordlist-size control
* [ ] Progress indicator
* [ ] Generation statistics
* [ ] Configuration file support
* [ ] Unit testing
* [ ] GUI version

## Responsible Use

This project is intended for **educational and authorized security-testing purposes only**.

Do not use this tool to attempt unauthorized access to accounts, systems, networks, or services. Always obtain appropriate permission before conducting security testing.

## Author

**Your Name**

Cybersecurity Student | Python Learner | CTF Enthusiast

### Skills Demonstrated

`Python` · `Linux` · `Cybersecurity` · `CTF` · `Git` · `GitHub` · `Automation`

## License

This project is provided for educational purposes. Users are responsible for ensuring that their use of the software complies with applicable laws, policies, and authorization requirements.
