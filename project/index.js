const express = require('express');
const exphbs = require('express-handlebars');
           
const session = require('express-session');

const app = express();

app.set('port', 3997);
app.engine('hbs', exphbs({extname: '.hbs'}));
app.set('view engine', 'hbs');

app.use(session({secret: 'mysecret'}));
app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.use(express.static('public'));
app.use(express.static('carousel pic'));

app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.get('/', (req,res)=> {
      res.render('home');
    });

app.get('/japan', (req,res)=> {
    res.render('japan');
    });

app.get('/spain', (req,res)=> {
    res.render('spain');
    });

app.get('/thailand', (req,res)=> {
    res.render('thailand');
    });

app.listen(app.get('port'), function(){
    console.log(`Express started on http://${process.env.HOSTNAME}:${app.get('port')}; press Ctrl-C to terminate.`);
});
