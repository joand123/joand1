app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + CSV_DIR + 'bd.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
db.init_app(app)

from Usuarios import Usuario
from Chaves import Chave

@app.before_first_reqest
def inicializar_bd():
    db.create_all()

@app.route('/')
def rout():    

@app.route('/chave/cadastrar' ,methods = ['POST','GET'])
def cadastrar_chave():
    form = ChaveForm()
    if form.validate_on_submit():
        #PROCESSAMENTO DOS DADOS RECEBIDOS
        nome = request.form['nome']
        novaChave = chave(nome=nome)
        db.session,add(novaChave)
        db.session,comit()
        return(redirect(url_for("root")))
    return(render_template('form.html', form = form,action=url_for('cadastrar_chave')))

@app.route('/chave/listar')
def listar_chave():
    chaves = Chave.query.order_by(Chave.nome)
    return(render_template('chave.html', chaves=chaves))

@app.route('/usuario/listar')
def listar_usuario():
    return("Não implementado")

@app.route('/usuario/cadastrar' ,methods = ['POST','GET'])
def cadastrar_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        #PROCESSAMENTO DOS DADOS RECEBIDOS
        nome = request.form['nome']
        username = request.form['username']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        novoUsuario = Usuario(nome=nome,username=username,email,,telefone=telefone,senha=senha)
        db.session.add(npvpusuario)
        db.session.Comnit()
        return(redirect(url_for("root")))
    return(render_template('form.html', form = form,action=url_for('cadastrar_usuario')))