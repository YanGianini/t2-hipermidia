function abrirJanela(){
    janela = window.document.getElementById("formulario_suspenso");
    janela.style.display = "block";
}

function fecharJanela(){
    janela = window.document.getElementById("formulario_suspenso");
    janela.style.display = "None";
}

function pop_excluir(nome){
    janela = window.document.getElementById(nome);
    janela.style.display = "block"; 
}