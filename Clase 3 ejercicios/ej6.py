import builtins

printOG = builtins.print


def printSobre(*args, **kwargs):
    printOG("---", *args, "----")


builtins.print = printSobre

print("hola")

builtins.print = printOG

print("hola")
