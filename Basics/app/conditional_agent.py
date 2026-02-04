from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from utilities.utility import export_graph_image

class AgentState(TypedDict):
    number1: int 
    operation: str 
    number2: int
    finalNumber: int

def adder(state:AgentState) -> AgentState:
    """This node adds the 2 numbers"""
    state["finalNumber"] = state["number1"] + state["number2"]

    return state

def subtractor(state:AgentState) -> AgentState:
    """This node subtracts the 2 numbers"""
    state["finalNumber"] = state["number1"] - state["number2"]
    return state


def decide_next_node(state:AgentState) -> AgentState:
    """This node will select the next node of the graph"""

    if state["operation"] == "+":
        return "addition_operation"
    
    elif state["operation"] == "-":
        return "subtraction_operation"

def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("add_node", adder)
    graph.add_node("subtract_node", subtractor)
    graph.add_node("router", lambda state:state) # passthrough function

    graph.add_edge(START, "router") 

    graph.add_conditional_edges(
        "router",
        decide_next_node, 

        {
            # Edge: Node
            "addition_operation": "add_node",
            "subtraction_operation": "subtract_node"
        }

    )

    graph.add_edge("add_node", END)
    graph.add_edge("subtract_node", END)

    return graph.compile()

def run_graph(data):
    app = build_graph()
    export_graph_image(app, "conditional_agent.png")
    return app.invoke(data)
