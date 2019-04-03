# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:57:57 2019

@author: P088904
"""
# matplotlibで簡単にアニメーションをつくる（mp4, gif)
# https://qiita.com/msrks/items/e264872efa062c7d6955

# ImageMagickを使用するための、matplotlibの環境設定関係
# https://qiita.com/wisteriq/items/1c3a91b52c1fe4585499

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
x = np.arange(0, 10, 0.1)

ims = []
for a in range(50):
    y = np.sin(x - a)
    line, = plt.plot(x, y, "r")
    ims.append([line])

ani = animation.ArtistAnimation(fig, ims)
ani.save('anim.gif', writer="imagemagick")
#ani.save('anim.mp4', writer="ffmpeg")
plt.show()