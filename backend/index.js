import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import ip from "ip";

console.log(ip.address())

const app = express();
const port = 3000

app.use(cors())
app.use(bodyParser.urlencoded({extended: true}))

app.get("/", (req, res) => {
    console.log("get")
    res.send({"msg" : 'HELLO'});
})

app.listen(port, () => {
    console.log(`port ${port}`)
})