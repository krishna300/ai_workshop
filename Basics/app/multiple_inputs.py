from typing import TypedDict, List
from langgraph.graph import StateGraph
from utilities.utility import export_graph_image

class AgentState(TypedDict):
    values: List[int]
    name: str 
    result: str

def process_values(state: AgentState) -> AgentState:
    """This function handles multiple different inputs"""
    print(state)

    state["result"] = f"Hi there {state["name"]}! Your sum = {sum(state["values"])}"

    print(state)
    return state

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("processor", process_values)
    graph.set_entry_point("processor") # Set the starting node
    graph.set_finish_point("processor") # Set the ending node

    return graph.compile() # Compiling the graph



def run_graph(data):
    app = build_graph()
    export_graph_image(app, "multiple_inputs.png")

    return app.invoke({
        "values": data.get("values"),
        "name": data.get("name")
    })
