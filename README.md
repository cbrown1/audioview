# audioview

Simple script to view soundfiles in the terminal

audioview depends on [pysndfile](https://forge-2.ircam.fr/roebel/pysndfile) and [plotext](https://github.com/piccolomo/plotext)

## Installing

### Install External Dependencies:

```bash
$ sudo pacman -S libsndfile # Or similar
```

### Download and Install:

```bash
$ pip install --user git+https://github.com/cbrown1/audioview.git#egg=audioview
```

## Usage

Just pass a soundfile path as an input argument (no color is shown here):

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

You can optionally specify the start and duration times to plot. Here, from 1 sec to 2.5 sec (1.5 s dur) of the soundfile will be plotted:

```bash
$ audioview /path/to/soundfile 1 1.5 
```

## Notes

- For multi-channel soundfiles, a separate plot will be generated for each channel maintaining y-axis scaling

- This script addressed the need for a super-simple and maintainable python-based way of viewing recorded soundfiles without leaving the terminal


## Authors

- [**Christopher Brown**](https://github.com/cbrown1)


## License

This project is licensed under the GPLv3 - see the [LICENSE.md](LICENSE.md) file for details.
