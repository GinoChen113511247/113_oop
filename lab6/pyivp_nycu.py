import pyivp
import matplotlib.pyplot as plt

# --- 各字母座標定義 ---
n_path = [
    pyivp.XYPoint(0, 0),
    pyivp.XYPoint(0, 5),
    pyivp.XYPoint(2, 0),
    pyivp.XYPoint(2, 5),
]

y_path = [
    pyivp.XYPoint(3, 5),
    pyivp.XYPoint(4, 3),
    pyivp.XYPoint(5, 5),
    pyivp.XYPoint(4, 3),
    pyivp.XYPoint(4, 0),
]

c_path = [
    pyivp.XYPoint(6, 5),
    pyivp.XYPoint(6, 0),
    pyivp.XYPoint(8, 0),
    pyivp.XYPoint(8, 1),
    pyivp.XYPoint(7, 1),
    pyivp.XYPoint(7, 4),
    pyivp.XYPoint(8, 4),
    pyivp.XYPoint(8, 5),
]

u_path = [
    pyivp.XYPoint(9, 5),
    pyivp.XYPoint(9, 0),
    pyivp.XYPoint(11, 0),
    pyivp.XYPoint(11, 5),
]

# --- 畫圖函數 ---
def draw_letter(ax, path, label, color):
    x = [pt.x() for pt in path]
    y = [pt.y() for pt in path]
    ax.plot(x, y, marker='o', label=label, color=color)

# --- 開始畫 ---
fig, ax = plt.subplots(figsize=(10, 6))
draw_letter(ax, n_path, "N", 'blue')
draw_letter(ax, y_path, "Y", 'red')
draw_letter(ax, c_path, "C", 'green')
draw_letter(ax, u_path, "U", 'purple')

ax.set_title("Path Simulation: NYCU")
ax.set_aspect('equal')
ax.legend()
plt.grid(True)
plt.show()
