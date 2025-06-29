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

* **Torus Geometry**: A donut (torus) is drawn by rotating a circle of radius `R1` around a larger circle of radius `R2`, creating a solid of revolution.

* **3D Rotation**: The shape rotates dynamically around the X and Z axes via angles `A` and `B`, with sin/cos values updating each frame.

* **Z-buffering**: A depth buffer tracks the closest surface points to correctly handle overlaps.

* **Projection**: 3D points `(x, y, z)` are projected to 2D screen space using:

  ```python
  x' = K1 * x / (K2 + z)
  y' = K1 * y / (K2 + z)
  ```

* **Lighting & Shading**: Surface normals are derived using the same rotation math and used with a light vector `(0, 1, -1)` to compute luminance, which determines brightness:

  ```python
  L = cos(φ) * sin(θ) * sin(B) - cos(A) * sin(θ) * sin(φ) - sin(A) * cos(θ) + cos(B) * (cos(A) * cos(θ) - sin(A) * sin(θ) * sin(φ))
  ```

* **ASCII Rendering**: Brightness levels map to characters like `.,-~:;=!*#$@` from darkest to lightest.

> This Python implementation closely follows the math detailed in Andy Sloane's writeup, performing matrix-based transformations and perspective projection in a simplified yet effective way.

For more detail, see the original explanation: [Donut math: how donut.c works](https://www.a1k0n.net/2011/07/20/donut-math.html).

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

This project is licensed under the [MIT License](./LICENSE) — free to use, modify, and distribute.
