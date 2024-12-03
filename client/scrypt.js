const socket = new WebSocket("ws://127.0.0.1:9000");

socket.onopen = () => {
	console.log("Connecté au serveur WebSocket.");
};

document.addEventListener('click', function (event) {
	const x = event.clientX;
	const y = event.clientY;

	console.log(`Position du clic: x=${x}, y=${y}`);

	const data = JSON.stringify({ x: x, y: y, sw: window.innerWidth, sh: window.innerHeight });

	socket.send(data)
});
