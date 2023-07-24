<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  // Create an event dispatcher
  const dispatch = createEventDispatcher();

  // Handler for the image selection event
  function handleImageChange(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files) {
      dispatch('change', Array.from(input.files));
    }
  }

  // Handler for the drop event
  function handleDrop(event: DragEvent) {
    event.preventDefault();
    const files = event.dataTransfer?.files;
    if (files) {
      dispatch('drop', Array.from(files));
    }
  }

  // Prevent the default behavior for the dragover event
  function handleDragOver(event: DragEvent) {
    event.preventDefault();
  }
</script>

<div class="container">
  <div
    class="drop-area"
    on:drop={handleDrop}
    on:dragover={handleDragOver}
  >
    <p>Drag and drop files here, or click to select files</p>
    <input
      type="file"
      id="images"
      on:change={handleImageChange}
      style="display: none"
      multiple
    />
    <label for="images">Select Images</label>
  </div>
</div>

<style>
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
  }

  .drop-area {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 2px dashed #333;
    border-radius: 10px;
    width: 100%;
    height: 300px;
  }

  .drop-area p {
    font-size: 1.5rem;
    font-weight: bold;
    color: #333;
  }

  .drop-area label {
    font-size: 1.2rem;
    font-weight: bold;
    color: #eee;
    background-color: #333;
    padding: 10px 20px;
    border-radius: 20px;
    cursor: pointer;
  }

  .drop-area label:hover {
    background-color: #111;
  }

  .drop-area label:focus {
    outline: none;
  }
</style>

