const btn = document.getElementById("btn");
const btnSocket = document.getElementById("btnSocket");
const ul = document.querySelector("ul");

const url = "http://localhost:3000/";

btn.addEventListener("click", () => {
    fetch(url, {
        method: "POST",
        body: JSON.stringify({
           "school": "ENS",
        }),
        headers: {
        "Content-Type": "application/json;charset=utf-8"
        }
    }).then(d => {
        return d.json()
    }).then(dd => {
        console.log(dd);
    })
});

const socket = io(url);

btnSocket.addEventListener("click", () => {
    socket.emit("message", 
    {
        msg: "1"
    })
});
 
socket.on("data", (data) => {
    console.log(socket.id); 
    const li = document.createElement('li');
    li.innerText = data.msg;
    ul.append(li);
})