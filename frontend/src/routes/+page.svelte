<script lang='ts'>
  import ImageUploader from '$lib/components/ImageUploader.svelte';

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

  <div>
    <h2>Selected Images</h2>
    <ul>
      {#each selectedImages as image}
        <li>{image.name}</li>
        <img src={URL.createObjectURL(image)} />
      {/each}
    </ul>
  </div>
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
