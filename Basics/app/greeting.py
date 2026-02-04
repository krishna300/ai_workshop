from typing import Dict, TypedDict
from langgraph.graph import StateGraph 
from utilities.utility import export_graph_image

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

def run_graph(data):
    app = build_graph()
    export_graph_image(app, "greeting.png")

    return app.invoke(data)
