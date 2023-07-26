export function openSocket(url: string) {
  return new WebSocket(url);
}

export function sendImage(socket: WebSocket, selectedImage: File) {
  const base64data = [];
  for (let i = 0; i < selectedImage.length; i++) {
    const reader = new FileReader();
    reader.readAsDataURL(selectedImage[i]);
    reader.onloadend = () => {
      base64data.push(reader.result);
    };
    const chunks = [];
    const chunkSize = 1024;
    const bufferLength = selectedImage[i].size;
    const slice = selectedImage[i].slice || selectedImage[i].webkitSlice || selectedImage[i].mozSlice;
    let start = 0;
    let end = chunkSize;
    while (start < bufferLength) {
      chunks.push(selectedImage[i].slice(start, end));
      start = end;
      end = start + chunkSize;
    }
    chunks.forEach((chunk, index) => {
      const data = {
        chunkNumber: index,
        totalChunks: chunks.length,
        image: chunk,
      };
      socket.send(JSON.stringify(data));
    });
  }
}
