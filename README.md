[![Build Status](https://travis-ci.org/cbrown1/arrow1.svg?branch=master)](https://travis-ci.org/cbrown1/arrow1)

# audioview

Simple script to view soundfiles in the terminal

## Usage

    audioview /path/to/sound/file

## Prerequisites

### Python Dependencies

- [wavefile](https://github.com/vokimon/python-wavefile)

- [plotext](https://github.com/piccolomo/plotext)

- [libsndfile](http://www.mega-nerd.com/libsndfile/)

## Installing

### Install Dependencies:

```bash
sudo pacman -S libsndfile
pip install --user wavefile
pip install --user plotext
```

### Download and Install:

```bash
git clone https://github.com/cbrown1/audioview.git
cd audioview
sudo make install
```

## Usage

Just pass the path to a soundfile:

```bash
audioview /path/to/sound/file
```

## Notes

- Multi-channel soundfiles should work fine

- This script addressed a need for a super-simple and maintainable way of viewing recorded soundfiles without leaving the terminal


## Authors

- [**Christopher Brown**](https://github.com/cbrown1)


## License

This project is licensed under the GPLv3 - see the [LICENSE.md](LICENSE.md) file for details.
