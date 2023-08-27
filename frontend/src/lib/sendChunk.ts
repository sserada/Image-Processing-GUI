export async function sendChunk(selectedImage: File, connection: WebSocket) {
  for (let i = 0; i < selectedImage.length; i++) {
    const reader = new FileReader();
    reader.readAsDataURL(selectedImage[i]);
    reader.onloadend = async () => {
      let chunks = [];
      const chunkSize = 1024;
      const name = selectedImage[i].name;
      let base64data = reader.result as string;
      for (let i = 0; i < base64data.length; i += chunkSize) chunks.push(base64data.slice(i, i + chunkSize));

      for (let i = 0; i < chunks.length; i++) {
        const data = {
          index: i,
          name: name,
          image_num: selectedImage.length,
          data: chunks[i],
          total: chunks.length - 1,
        };
        console.log(data);
        connection.send(JSON.stringify(data));
      }
    };
  }
}

