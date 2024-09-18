
const express = require('express')
const fs = require("fs")
const bodyParser = require('body-parser')
const path = require('path')
const https = require('https')


const DataTools = require('./datatools');

const app = express()
// Pour accepter les connexions cross-domain (CORS)
app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
    next();
});

app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, 'views'))

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const prefix = '/datalens'

app.use(prefix, express.static(path.join(__dirname, 'public')))

// Serve static files from 'node_modules' (optional: use a prefix to avoid conflicts)
app.use(prefix + '/node_modules', express.static(path.join(__dirname, 'node_modules')));


app.get(prefix, (req, res) => {
    res.render('about')
})

app.get(prefix + '/explorer', (req, res) => {
    res.render('index')
})

app.post(prefix + '/data/:action', async (req, res) => {
    let filters = req.body; // expects { modality: [], license: [], tasks: [] }

    const folderPath = 'data/modality_datasets';
    const dataTools = new DataTools(folderPath);
    // console.log(filters)
   
    let filterPath = path.join(__dirname, 'data/filters.json')
    let result;
    if (req.params.action === 'filters' && fs.existsSync(filterPath)) {
        result = fs.readFileSync(filterPath)
    } else {
        let cachefile = `data/cache/${dataTools.getFilterHash(filters)}.json`
        if (fs.existsSync(path.join(__dirname, cachefile))) {
            // console.log(`Loading cache file ${cachefile}`)
            result = fs.readFileSync(path.join(__dirname, cachefile))
            // console.log(`Dataset has ${result.data.length} entries.`)
        } else {        
            await dataTools.init(req.params.action, filters)
            result = await dataTools.getData()
            try {
                result = JSON.stringify(result, null, 4)
            } catch(e) {
                result = { message: 'The resulting dataset is too large to be displayed. Please review your filters.' }
                result = JSON.stringify(result)
            }
        }
    }

    res.send(result)
    // res.json(result);
});


const port = 8010 // verify the availability of this port on the server
const portHTTPS = 8013

app.listen(port, async () => { console.log(`HTTP Server started at port ${port}.`) })

try {
    var privateKey = fs.readFileSync( '/etc/httpd/certificate/exp_20240906/dataviz_i3s_unice_fr.key' );
    var certificate = fs.readFileSync( '/etc/httpd/certificate/exp_20240906/dataviz_i3s_unice_fr_cert.crt' );
    var ca = fs.readFileSync( '/etc/httpd/certificate/exp_20240906/dataviz_i3s_unice_fr_AC.cer' );
    var options = {key: privateKey, cert: certificate, ca: ca};
    https.createServer( options, function(req,res)
    {
        app.handle( req, res );
    } ).listen( portHTTPS, async () => { console.log(`HTTPS Server started at port ${portHTTPS}.`) } );
} catch(e) {
    console.log("Could not start HTTPS server")
}
