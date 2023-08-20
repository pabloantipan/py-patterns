from context_state import Context
from state import ConcreteStateA


if __name__ == "__main__":
    # The client code.

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
