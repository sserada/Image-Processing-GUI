<script lang='ts'>
  import ImageUploader from '$lib/components/ImageUploader.svelte';
  import ImageList from '$lib/components/ImageList.svelte';

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
</style>
