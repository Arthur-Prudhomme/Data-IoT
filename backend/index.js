import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import {Server} from "socket.io"
import http from "http";

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
    console.log('user connected');

    socket.on("message", (data) => {
        io.emit("data", data)
    })
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