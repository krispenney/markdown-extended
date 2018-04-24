# Extended Markdown
Extend the capabilities of Markdown with diagrams and LaTeX.

### Work in Progress :wrench:

The goal of this project is to process **Extended Markdown** files (`.mdx`) into **Markdown** files (`.md`), by rending complex objects as images that can be conveniently displayed on services that can render traditional Markdown (ex. GitHub). This extension adds useful capabilities such as:
- [x] Graph diagrams
- [x] Block LaTeX rendering
- [x] Inline LaTex rendering (i.e. `y = mx + b is a rational function!` )

### Examples

#### Graphs

##### Source

```
-------
a -> b
a -> c
a -> d
b -> e
c -> e
d -> e
-------
```

##### Results

![graph-9c3dacad-2909-4db0-a1b4-8526c83b9a03](data/README/graph-9c3dacad-2909-4db0-a1b4-8526c83b9a03.svg)

#### Latex Equations

##### Source

```
You can perform complex inline Latex:
- A fraction: $$\frac{x_1 - x_2}{y_1 - y_2}$$.
- You can use symbols such as: $$\sum_{x \in X} \frac{x}{\mid X \mid}$$
```

##### Results

You can perform complex inline Latex:
- A fraction: ![latex-393a5b25-f7df-42c5-a60e-80be1b35b0cd](data/README/latex-393a5b25-f7df-42c5-a60e-80be1b35b0cd.png).
- You can use symbols such as: ![latex-c00a53d9-7714-4a7d-ad96-8a1d830a21e9](data/README/latex-c00a53d9-7714-4a7d-ad96-8a1d830a21e9.png)
