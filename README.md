# ASCII Spinning Donut

Render a colorful, spinning ASCII donut in your terminal — featuring dynamic color effects, real-time speed control via arrow keys, and smooth animated motion trails for an engaging CLI experience.

![](./donut.gif)

---

## Features

* Smooth, continuous spinning animation
* Automatically transitioning ASCII color palette
* Keyboard input to control spin speed in real time
* Lightweight: no graphics engine, pure Python math
* Motion trail effects for a sleek, glowing aesthetic
* Compatible with macOS Terminal & most modern terminals

---

## Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```text
colorama
pynput
```

---

## How to Run

```bash
python donut.py
```

* Press ↑ to speed up rotation
* Press ↓ to slow down rotation
* Real-time speed display shown at bottom
* Exit anytime with `Ctrl+C`

---

## How It Works

This spinning donut is a faithful Python adaptation of [Andy Sloane's original `donut.c`](https://www.a1k0n.net/2011/07/20/donut-math.html). The rendering relies on clever 3D math and ASCII projection:

* **Torus Geometry**: A donut (torus) is drawn by rotating a circle around an axis. This is defined using two angles — `θ` (theta) for the inner circle and `φ` (phi) for the revolution.

* **3D Rotation**: Applies transformations around the X and Z axes using sin/cos of time-based variables `A` and `B`, which increment each frame.

* **Z-buffering**: A simple depth buffer ensures correct rendering order of surface points.

* **Projection**: The 3D `(x, y, z)` points are projected onto a 2D screen using a perspective formula:

  ```
  x' = K1 * x / (K2 + z)
  y' = K1 * y / (K2 + z)
  ```

* **Lighting & Shading**: Illumination is calculated using dot product of the surface normal and a light vector `(0, 1, -1)`, determining the brightness level.

* **ASCII Rendering**: The brightness is mapped to ASCII characters like `.,-~:;=!*#$@` to simulate shading.

The Python version adds real-time speed control and color effects, preserving the algorithm’s charm while modernizing the experience.

---

## Create a GIF from Terminal

To capture a `.gif` animation from your terminal:

```bash
python record_donut.py
```

This will save a `donut.gif` using `pyautogui` and `imageio`. Ensure terminal is in focus during recording.

---

## Project Structure

```
├── donut.py             # Main donut animation script
├── record_donut.py      # Optional screen recorder script
├── donut.gif            # Sample animated output
├── .gitignore
└── requirements.txt
```

---

## Inspiration

This project was inspired by [a1k0n's legendary donut math demo](https://www.a1k0n.net/2011/07/20/donut-math.html), originally written in C. It’s reimagined here in Python, with interactivity, animated colors, and terminal-ready enhancements.

> “Donuts, math, and ASCII — what's not to love?”

---

## Future Ideas

* Add mouse interaction (e.g. drag to rotate, click to pause)
* Toggle animation modes: wireframe, filled, shadows
* Support ASCII shading themes (classic, neon, retro)
* Publish as a pip package (`pip install ascii-donut`)
* Turn into a desktop widget using tkinter or Electron

---

## Credits

* Core algorithm and math: [Andy Sloane (a1k0n)](https://www.a1k0n.net/2011/07/20/donut-math.html)
* Python adaptation & enhancements: [@Prasadkurapati](https://github.com/Prasadkurapati)
* Terminal ASCII inspiration: CLI artists and retro devs everywhere

---

## License

MIT License — free to use, modify, and distribute.





























# ASCII Spinning Donut

Render a colorful, spinning ASCII donut in your terminal — featuring dynamic color effects, real-time speed control via arrow keys, and smooth animated motion trails for an engaging CLI experience.

![](./donut.gif)

---

## Features

- Smooth, continuous spinning animation
- Automatically transitioning ASCII color palette
- Keyboard input to control spin speed in real time
- Lightweight: no graphics engine, pure Python math
- Motion trail effects for a sleek, glowing aesthetic
- Compatible with macOS Terminal & most modern terminals

---

## Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```text
colorama
pynput
```

---

## How to Run

```bash
python donut.py
```

- Press ↑ to speed up rotation
- Press ↓ to slow down rotation
- Real-time speed display shown at bottom
- Exit anytime with `Ctrl+C`

---

## Create a GIF from Terminal

To capture a `.gif` animation from your terminal:

```bash
python record_donut.py
```

This will save a `donut.gif` using `pyautogui` and `imageio`. Ensure terminal is in focus during recording.

---

## Project Structure

```
├── donut.py             # Main donut animation script
├── donut.gif            # Sample animated output
├── .gitignore
└── requirements.txt
```

---

## Inspiration

This project was inspired by [a1k0n's legendary donut math demo](https://www.a1k0n.net/2011/07/20/donut-math.html), originally written in C. It’s reimagined here in Python, with interactivity, animated colors, and terminal-ready enhancements.

> “Donuts, math, and ASCII — what's not to love?”

---

## Future Ideas

- Add mouse interaction (e.g. drag to rotate, click to pause)
- Toggle animation modes: wireframe, filled, shadows
- Support ASCII shading themes (classic, neon, retro)
- Publish as a pip package (`pip install ascii-donut`)
- Turn into a desktop widget using tkinter or Electron

---

## Credits

- Core algorithm and math: [Andy Sloane (a1k0n)](https://www.a1k0n.net/2011/07/20/donut-math.html)
- Python adaptation & enhancements: [@Prasadkurapati](https://github.com/Prasadkurapati)
- Terminal ASCII inspiration: CLI artists and retro devs everywhere

---

## License

This project is licensed under the [MIT License](./LICENSE) — free to use, modify, and distribute.
