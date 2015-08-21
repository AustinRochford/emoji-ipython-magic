# `emoji-ipython-magic`
An IPython magic that renders emoji

## Demo

![Demo](https://raw.githubusercontent.com/AustinRochford/emoji-ipython-magic/master/demo.png)

## Usage

* The line magic `%emoji :emoji:` will render all the emoji on the following line

## Installation

To install, do `pip install emoji-ipython-magic` or `%load_ext https://github.com/AustinRochford/emoji-ipython-magic/emoji_magic.py`.

The only dependency (other that IPython) is [`emoji`](https://pypi.python.org/pypi/emoji).

## Docker

To build run `docker build --tag=emoji-magic .`
To run the container `docker run -d -p 443:8888 -e "PASSWORD=MakeAPassword" emoji-magic`
Replace MakeAPassword with a real one
You can change emoji-magic in both to any name you like.
To use get your docker host ip (ususally in the env var $DOCKER_HOST) and enter it in your browser with https and login. So for example I navigate to `https://192.168.59.107/`

## License

This code is distributed under the [MIT License](https://raw.githubusercontent.com/AustinRochford/s3img-ipython-magic/master/LICENSE).
