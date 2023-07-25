<script lang='ts'>
  import ImageUploader from '$lib/components/ImageUploader.svelte';
  import ImageList from '$lib/components/ImageList.svelte';
  import ResetButton from '$lib/components/ResetButton.svelte';

  import { generateUUID } from '$lib/generateUUID';

  // Variable to store the id of the current session
  let id: string = generateUUID();

  // Variable to store the selected images
  let selectedImages: File[] = [];

  // Function to handle the change event
  function handleImageChange(images: File[]) {
    // Save the selected images
    selectedImages = images.detail;
  }
</script>

<svelte:head>
	<title>Image Processing UI</title>
</svelte:head>


<section>
  <ImageUploader on:change={handleImageChange} on:drop={handleImageChange} />
  <div class="buttons">
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
