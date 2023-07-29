export function sendImage(connection: WebSocket, selectedImage: File) {
  for (let i = 0; i < selectedImage.length; i++) {
    const reader = new FileReader();
    reader.readAsDataURL(selectedImage[i]);
    reader.onloadend = () => {
      let chunks = [];
      const chunkSize = 1024;
      const name = selectedImage[i].name;
      let base64data = reader.result as string;
      for (let i = 0; i < base64data.length; i += chunkSize) chunks.push(base64data.slice(i, i + chunkSize));

      for (let i = 0; i < chunks.length; i++) {
        const data = {
          index: i,
          name: name,
          data: chunks[i],
          total: chunks.length - 1,
        };
        console.log('Sending Chunk ', i);
        connection.send(JSON.stringify(data));
      }
    };
  }
}

