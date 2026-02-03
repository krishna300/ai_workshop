from typing import TypedDict
from langgraph.graph import StateGraph
import os

class AgentState(TypedDict): # Our state schema
    message : str 

def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds a greeting message to the state"""

    state['message'] = "Hey " + state["message"] + ", how is your day going?"

    return state

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("greeter", greeting_node)
    graph.set_entry_point("greeter")
    graph.set_finish_point("greeter")
    return graph.compile()

def run_graph(name: str):
    app = build_graph()
    export_graph_image(app)
    return app.invoke({"message": name})

def export_graph_image(app):
    assets_dir = os.path.join(
        os.path.dirname(__file__), "..", "assets"
    )
    os.makedirs(assets_dir, exist_ok=True)

    graph_path = os.path.join(assets_dir, "greeting_graph.png")

    with open(graph_path, "wb") as f:
        f.write(app.get_graph().draw_png())

    print(f"✅ Graph image saved at: {graph_path}")
