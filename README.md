# audioview

Simple script to view soundfiles in the terminal


## Installing

### Install External Dependencies:

```bash
sudo pacman -S libsndfile # Or similar
```

### Download and Install:

```bash
git clone https://github.com/cbrown1/audioview.git
cd audioview
pip install .
```

## Usage

Just pass the path to a soundfile (no color is shown here):

```bash
$ audioview /path/to/amtone.wav
     ┌┬──────────────────┬───────────────────┬───────────────────┬──────────────────┬┐
  1.0┼┼▄██████▄──────────┼▗▄█████▙▄──────────┼▗▟█████▙▖──────────┼▄▟█████▄▖─────────┼┤
 0.33┼██████████▄───────▗▟██████████▄───────▄▟█████████▙▖───────▄██████████▙▖──────▗▄┤
    0┼████████████▙▄▄▄▄███████████████▄▄▄▄▄███████████████▄▄▄▄▟██████████████▙▄▄▄▄▟██┤
-0.33┼████████████▛▀▀▀▀▜██████████████▀▀▀▀▀███████████████▀▀▀▀▀██████████████▛▀▀▀▀▜██┤
-0.67┼██████████▀───────▝▜██████████▀───────▀▜█████████▛▘───────▀██████████▛▘──────▝▀┤
 -1.0┼┼▀██████▀──────────┼▝▀█████▛▘──────────┼▝▜█████▛▘──────────┼▀▜█████▀▘─────────┼┤
     └┼──────────────────┼───────────────────┼───────────────────┼──────────────────┼┘
      0                 0.2                 0.5                 0.8                 1 
[y]                                    Time (s) [x]                                   

$ 

```

## Notes

- Multi-channel soundfiles should work fine

- This script addressed a need for a super-simple and maintainable python-based way of viewing recorded soundfiles without leaving the terminal


## Authors

- [**Christopher Brown**](https://github.com/cbrown1)


## License

This project is licensed under the GPLv3 - see the [LICENSE.md](LICENSE.md) file for details.
