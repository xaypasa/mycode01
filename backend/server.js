var express = require('express')
var cors = require('cors')
const mysql = require('mysql2');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'mydb',
  password : ''
});

var app = express()
app.use(cors())
app.use(express.json())

app.get('/', function (req, res, next){
    res.send('Hello World! from server')
})

app.get('/users', function (req, res, next){
    connection.query(
        'SELECT * FROM `users`',
        function(err, resulte, fields){res.send(resulte)}
    )
})

// pp.post('/signup', function (req, res, next) {
//     connection.query(
//       'INSERT INTO `users`(`fname`, `lname`, `username`, `password`, `avatar`) VALUES (?, ?, ?, ?, ?)',
//       [req.body.fname, req.body.lname, req.body.username, req.body.password, req.body.avatar],
//       function(err, results) {
//         res.json(results);
//       }
//     );
//   })

app.listen(5000, function () {
  console.log('CORS-enabled web server listening on port 5000')
})