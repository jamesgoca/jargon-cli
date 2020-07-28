# Jargon CLI

A script to retrieve the Cool Jargon of the Day and display on my console.

[Cool Jargon of the Day](http://www.jargon.net) is written by jargon.net.

## Installation

First, clone a copy of this repository:

```
git clone https://github.com/jamesgoca/jargon-cli
```

Next, initialize a Python virtual environment and install the dependencies for this project:

```
python3 -m venv venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

You are now ready to use Jargon CLI.

### Create an Alias

I have created an alias for this project. You can do this by opening your terminal's configuration file (i.e. .bashrc or .zshrc) and adding this line of code (with the relevant file path):

```
alias jargon=/path/to/jargon.py
```

I have this script set up so that it opens every time I open my terminal. To achieve the same, add the following line after the alias:

```
jargon
```

This will run the `jargon` command when you open your terminal.

## Usage

You can run this script using the following command:

```
python3 jargon.py
```

This command will present you the Jargon of the Day.

You can open up the latest Jargon of the Day using the open command:

```
python3 jargon.py open
```

## Screenshot

![Screenshot of the Jargon CLI](https://github.com/jamesgoca/jargon-cli/blob/master/screenshot.png?raw=true)

## License

This project is licensed using an MIT license. See more information in [LICENSE](https://github.com/jamesgoca/jargon-cli/blob/master/LICENSE).

## Authors

James Gallagher
