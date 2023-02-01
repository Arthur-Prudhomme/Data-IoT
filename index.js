import express from "express";
import cors from "cors";
import bodyParser from "body-parser"

const app = express();
const port = 3000

app.use(cors())
app.use(bodyParser.json())

app.get("/", (req, res) => {
    console.log("get")
    res.json({msg: 'HELLO'});
})

app.listen(port, () => {
    console.log(`port ${port}`)
})