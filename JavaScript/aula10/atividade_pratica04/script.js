function addParagrafo(){
    let container = document.getElementById('container');
    let add = document.createElement('p');
    add.textContent = 'We have a new text here';

    container.appendChild(add);
}

function delParagrafo(){
    let container = document.getElementById('container');
    let ultimoParagrafo = container.lastElementChild;

    if(ultimoParagrafo){
        container.removeChild(ultimoParagrafo);
    }else{
        alert('nao tem mais nada');
    }
}