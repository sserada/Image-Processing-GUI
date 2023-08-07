<script lang='ts'>
  import ImageUploader from '$lib/components/ImageUploader.svelte';
  import ImageList from '$lib/components/ImageList.svelte';
  import SendButton from '$lib/components/SendButton.svelte';
  import ResetButton from '$lib/components/ResetButton.svelte';

  import { generateUUID } from '$lib/generateUUID';
  import { openSocket } from '$lib/openSocket';
  import { sendChunk } from '$lib/sendChunk';

  // Variable to store the id of the current session
  const clientId: string = generateUUID();

  // Variable to store the selected images
  let selectedImages: File[] = [];

  // Variable to store the websocket
  let connection: WebSocket;

  // Function to handle the change event
  function handleImageChange(images: File[]) {
    // Save the selected images
    selectedImages = images.detail;
  }

  // Function to handle the send event
  function handleSendImage() {
    connection = openSocket(`ws://localhost:80/backend/websocket/${clientId}`);
    connection.onopen = () => {
      // Send the images
      sendChunk(selectedImages, connection);
    };
  }
</script>

<svelte:head>
	<title>Image Processing UI</title>
</svelte:head>

<section>
  <ImageUploader on:change={handleImageChange} on:drop={handleImageChange} />
  <div class="buttons">
    <SendButton on:send={handleSendImage} />
    <ResetButton />
  </div>
  <ImageList selectedImages={selectedImages} />
</section>

<style>
  section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 0.6;
  }

  .buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 1rem;
  }
</style>

