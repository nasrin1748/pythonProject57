from pyscript import when
from js import document

@when("click","#greet-but")
def greet_user(event):
    #print("hello")
    name = document.querySelector("#name").value
    output = f"Nice,{name}"
    print(output)
    document.querySelector("#output").innerText = output