# audioview

Simple script to view soundfiles in the terminal


## Installing

### Install Dependencies:

```bash
sudo pacman -S libsndfile # Or similar
pip install --user pysndfile
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
$ audioview /path/to/sound/file
      ┌┬─────────────────┬─────────────────┬─────────────────┬────────────────┬┐
 0.287┼┼───▐▄▄▄▖──▐█▙────┼──▗▄▄────────────┼─────▐───────────┼▗───────────────┼┤
 0.096┼┼─▄▗█████▙─▟██────┼─▄███───────███▖─┼─█▌──█▄▐████▖────▗▐█▄▄▟▄▄▄────────┼┤
     0┼▄▟████████████▙▄▄▟▙▄████▙▖▄▄▖▄▄███▙▄▄▄█▙▄▄██████████▙▄▟▟██████████▙▄▄▄▄▄┤
-0.096┼▀█████████████▀▀▀█▛▀████▛▀▀▀▀▀▀███▛▀▀▜█▛▀▀███████▛██▛▀▜█████████████▜▀▀▀┤
      ││   █████▛▘▜██    │ ▜███▌      ███▌ │ █▌  ██▜████▌    ▝▜██████████▛▘   ││
-0.192┼┼───▜███▛──▐██────┼─▐███───────▜██──┼─▜▘──▛▘▝▛▀▀▀─────┼▐████████▛──────┼┤
      └┼─────────────────┼─────────────────┼─────────────────┼────────────────┼┘
       0                0.6               1.2               1.8              2.4
[y] Channel 1                        Time (s) [x]                               
$ 

```

## Notes

- Multi-channel soundfiles should work fine

- This script addressed a need for a super-simple and maintainable python-based way of viewing recorded soundfiles without leaving the terminal


## Authors

- [**Christopher Brown**](https://github.com/cbrown1)


## License

This project is licensed under the GPLv3 - see the [LICENSE.md](LICENSE.md) file for details.
