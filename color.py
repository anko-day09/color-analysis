from PIL import Image
import matplotlib.pyplot as plt
import extcolors
from collections import Counter

def rgb_to_hex(rgb):
    # RGBA形式の場合、最後の要素（アルファチャンネル）を無視する
    rgb = rgb[:3]
    return "#{:02x}{:02x}{:02x}".format(*rgb).lower()

def extract_colors(image_path, num_colors=6):
    # 画像から色を抽出
    colors, pixel_count = extcolors.extract_from_path(image_path)

    # 上位6色を取得
    most_common_colors = colors[:num_colors]

    # 画像の表示
    img = Image.open(image_path)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # 画像のプロット
    ax1.imshow(img)
    ax1.axis('off')
    ax1.set_title("Image")

    # 棒グラフの作成
    labels = [f"{rgb_to_hex(color)}" for color, _ in most_common_colors]
    sizes = [count / pixel_count for _, count in most_common_colors]
    colors = [rgb_to_hex(color) for color, _ in most_common_colors]

    indices = range(len(labels))
    bars = ax2.bar(indices, sizes, color=colors)

    # 割合を表示
    for bar, label, color, size in zip(bars, labels, colors, sizes):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f"{label}\n{size:.2%}", ha='center', va='bottom', fontsize=8, color='black')

    # グラフの設定
    ax2.set_xticks(indices)
    ax2.set_xticklabels(labels)
    ax2.set_title("Top 6 Colors - Bar Plot")

    plt.show()

if __name__ == "__main__":
    # 画像ファイルのパスを指定
    image_path = ""

    # 色を抽出して画像とBar Plotを同時に可視化
    extract_colors(image_path)
