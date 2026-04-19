function mudarTudo(){
    let imagem = document.getElementById('minhaImagem');
    imagem.setAttribute('src', 'https://br.pinterest.com/pin/783344928950714597/');

    let link = document.getElementById('meuLink');
    link.setAttribute('href', 'https://infinityschool.com.br');
    link.textContent = 'link infinity';
}