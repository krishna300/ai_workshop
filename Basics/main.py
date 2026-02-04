# from app.greeting import run_graph
# data = {"message":"Raghavan"}


# from app.multiple_inputs import run_graph
# data = {
#     "values":[2,4,6,8],
#     "name": "Krishna"
# }

# from app.sequential_agent import run_graph
# data = {"name": "Charlie", "age": 20}

# from app.conditional_agent import run_graph
# data = {
#         "number1":15,
#         "operation":"+",
#         "number2":21,                        
#     }

from app.looping import run_graph
data = {"name":"Kalyan", "number":[], "counter":-100}

def main():
    print("Hello from basics!")
    result = run_graph(data)
    print(result)

if __name__ == "__main__":
    main()
