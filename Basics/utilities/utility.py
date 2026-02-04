import os

def export_graph_image(app, filename):
    assets_dir = os.path.join(os.getcwd(), "assets")
    os.makedirs(assets_dir, exist_ok=True)

    graph_path = os.path.join(assets_dir, filename)

    with open(graph_path, "wb") as f:
        f.write(app.get_graph().draw_png())

    print(f"✅ Graph image saved at: {graph_path}")