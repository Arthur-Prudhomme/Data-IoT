import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import {Server} from "socket.io"
import http from "http";
// import axios from "axios";

import ip from "ip";

console.log(ip.address())

const app = express();
const httpServer = http.createServer(app)

const port = 3000

const io = new Server(httpServer, {
    cors: {
        origin: "*",
    }
})

io.on("connection", (socket) => {
    console.log('page');

    // socket.on("message", (data) => {
    //     io.emit("data", data)
    // })
})

app.post("/right", (req, res) => {
    console.log("right")
    res.send({ });
    io.emit("direction", "right")
})
app.post("/left", (req, res) => {
    console.log("left")
    res.send({ });
    io.emit("direction", "left")
})
app.post("/up", (req, res) => {
    console.log("up")
    res.send({ });
    io.emit("direction", "up")
})
app.post("/down", (req, res) => {
    console.log("down")
    res.send({ });
    io.emit("direction", "down")
})

app.use(cors())
app.use(bodyParser.urlencoded({extended: true}))

app.get("/", (req, res) => {
    console.log("get")
    res.send({"msg" : 'HELLO'});
})

httpServer.listen(port, () => {
    console.log(`Port ${port}`)
})