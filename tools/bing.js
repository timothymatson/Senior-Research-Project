let images = document.getElementsByClassName('iusc');

let urls = '';

for (let image of images) {
	let url = JSON.parse(image.getAttribute('m')).murl;
	urls += url + '\n'
}
console.log(urls);
