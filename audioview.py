#!/usr/bin/env python

import sys
import numpy as np
import wavefile as wf    # pip install wavefile (dependency: libsndfile)
import plotext as plx    # pip install plotext


if len(sys.argv) == 1:
    print("Usage: audioview /path/to/audio/file")

else:
    filename = sys.argv[1]
    fs, data = wf.loadWave(filename)

    data = np.atleast_2d(data.T)

    x = np.linspace(0, data.size/fs, data.size)
    mx = np.max(data)

    #plx.subplots(data.shape[1], 1)

    for channel in range(data.shape[1]):

    #    plx.subplot(channel, 1)
        plx.plot(x, data[:, channel], color = "blue", marker = "small")
        plx.plotsize(200,10)
        plx.canvas_color("black")
        plx.axes_color("black")
        plx.ticks_color("iron")
        plx.ylabel(f"Channel {channel+1}")
        plx.xlabel(f"Time (s)")
        plx.grid(True)
        plx.ylim(-mx, mx)

        plx.show()

