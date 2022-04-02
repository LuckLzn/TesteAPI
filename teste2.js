const {spawn}  = require('child_process');

const process = spawn('python', ['testeapi.py']);
process.stdout.on('data', data =>{
    console.log(data.toString());
})