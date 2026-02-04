from typing import TypedDict # Imports all the data types we need
from langgraph.graph import StateGraph
from utilities.utility import export_graph_image

class AgentState(TypedDict):
    name: str
    age: str
    final: str

def first_node(state:AgentState) -> AgentState:
    """This is the first node of our sequence"""

    state["final"] = f"Hi {state["name"]}!"
    return state

def second_node(state:AgentState) -> AgentState:
    """This is the second node of our sequence"""

    state["final"] = state["final"] + f" You are {state["age"]} years old!"

    return state

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("first_node", first_node)
    graph.add_node("second_node", second_node)

    graph.set_entry_point("first_node")
    graph.add_edge("first_node", "second_node")
    graph.set_finish_point("second_node")
    return graph.compile()

def run_graph(data):
    app = build_graph()
    export_graph_image(app, "sequential_agent.png")

    return app.invoke(data)