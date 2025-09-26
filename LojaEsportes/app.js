const express = require('express');
const path = require('path');
const app = express();

// Middleware para ler os dados do formulário
app.use(express.urlencoded({ extended: true }));

// Servir arquivos estáticos da pasta 'site'
app.use(express.static('site'));

// Exibir o formulário de login
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'site', 'login.html'));
});

app.get('/loja', (req, res) => {
    res.sendFile(path.join(__dirname, 'site', 'loja.html'));
});

// Processar os dados do login
app.post('/', (req, res) => {
    const { usuario, senha } = req.body;

    if (usuario === 'admin' && senha === '1234') {
        res.send('Login bem-sucedido! Bem-vindo, Administrador!');
    } 
    
    else if (usuario === 'henrique' && senha === 'aleatorio123'){
        res.sendFile(path.join(__dirname, 'site', 'loja.html'));
    }

    else {
        res.send('Usuario ou senha inválidos!');
    }
});

app.use((req, res) => {
    res.status(404).send('<h1>Página não encontrada!</h1>');
});

app.listen(8080, () => {
    const date = new Date();
    console.log('Servidor iniciado em ' + date);
    console.log('Servidor rodando em http://localhost:8080');
});