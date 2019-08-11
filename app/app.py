import os
#import magic
import urllib.request
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import subprocess
import logging, logging.config, yaml
import json
import jinja2
from jinja2.ext import with_
UPLOAD_FOLDER = '/var/spool/uploads/'


####### LOG
logging.basicConfig(level=logging.INFO)
logging.config.dictConfig(yaml.load(open('logging.conf')))
logger = logging.getLogger(__name__)
logfile    = logging.getLogger('file')
logconsole = logging.getLogger('console')
logconsole.debug("Debug CONSOLE")
####### End of LOG

app = Flask(__name__, static_url_path='/app/views')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    logfile.info("raiz")
    return redirect("views/index.html", code=302)

@app.route('/views/<view>')
def default_view(view=None):
    busqueda = request.args.get('busqueda' , 'no_busqueda')
    size = request.args.get('size' , '100')
    logfile.info('%s] [%s] [%s' % (request.environ['REMOTE_ADDR'],view,busqueda))


    # Prework
    vacio = json.loads('[]')
    resultados = {}
    #resultados = dict([("inventario", vacio), ("ticket", vacio),("jira", vacio),("cmdb", vacio),("wiki", vacio),("udo", vacio),("recuento", vacio),("config", vacio),("index", vacio),("quick", vacio), ("ayuda", vacio) , ("dcip", vacio) ])

    # Load Jinja environment
    templateLoader = jinja2.FileSystemLoader( searchpath=['/app/views/'] )
    templateEnv = jinja2.Environment( loader=templateLoader , extensions=['jinja2.ext.with_'])
    template = templateEnv.get_template( view )

    # if output.find("head") != -1:
    #  return output
    #tipo_devuelto = {slim_codename : get_elemento(slim_codename,busqueda=busqueda,size=size)}
    #resultados.update(tipo_devuelto)
    # Load config
    #   print slim_codename,busqueda,size

    slim_codename= view.split(".")[0]
    #resultados[slim_codename] = get_elemento(slim_codename, busqueda=busqueda, size=size)
    #resultados["recuento"]    = get_elemento("recuento"   , busqueda=busqueda, size=size)
    #resultados["quick"   ]    = get_elemento("quick"      , busqueda=busqueda, size=size)

    # If quick result are found and we come from start page, switch to quick view
    #if request.referrer != None :
    #   if "index.html" in request.referrer \
    #       and view == 'inventario.2.html' \
    #       and resultados["quick"]["RESULTADOS_QUICK"] > 0 \
    #       and busqueda != "m2m" and busqueda != "M2M" :
    #       return redirect("views/quick.html?busqueda=%s" % busqueda, code=302)


    #resultados["config"  ]    = json.loads('  { "SEARCH_DECODED" : "%s"  ,   "VIEW" : "%s"   ,  "VIEW_SLIM" : "%s" } ' % ( busqueda, view, slim_codename   ) )



    #print("resultados[slim_codename]" , resultados[slim_codename] )
    #print("resultados[config]="       , resultados["config"]      )
    #print("resultados[quick]="        , resultados["quick"]       )
    #print("resultados[recuento]="     , resultados["recuento"]    )
    #print("resultados[ayuda]="        , resultados["ayuda"]    )


    try :
       salida = template.render( )
       return salida
    #   salida = template.render(
    #            cmdb       = resultados["cmdb"]      ,
    #            config     = resultados["config"]    ,
    #            index      = resultados["index"]     ,
    #            inventario = resultados["inventario"],
    #            jira       = resultados["jira"]      ,
    #            quick      = resultados["quick"]     ,
    #            recuento   = resultados["recuento"]  ,
    #            ticket     = resultados["ticket"]    ,
    #            udo        = resultados["udo"]       ,
    #            dcip       = resultados["dcip"]      ,
    #            ayuda      = resultados["ayuda"]     ,
    #            wiki       = resultados["wiki"] )
    #  return salida

    except Exception:
       logfile.error('Cannos open %s %s %s' % (view,Exception,busqueda))
       print ('cannot open', Exception)
       #return template.render(
        #        cmdb       = resultados["cmdb"],
        #        config     = resultados["config"] ,
        #        index      = resultados["index"],
        #        inventario = resultados["inventario"],
        #        jira       = resultados["jira"],
        #        quick      = resultados["quick"],
        #        recuento   = resultados["recuento"],
        #        ticket     = resultados["ticket"],
        #        udo        = resultados["udo"],
        #        dcip        = resultados["dcip"],
        #        ayuda      = resultados["ayuda"],
        #        wiki       = resultados["wiki"])



if __name__ == "__main__":
    app.run()
