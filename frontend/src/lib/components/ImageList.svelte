<script lang='ts'>
  export let selectedImages: FileList;
  export let processedImages: string[];
</script>

<section>
  <table>
    <tr>
      {#if selectedImages.length > 0}
        <td id="headline">Selected Images</td>
        <td id="headline">Processed Images</td>
      {/if}
    </tr>
    {#each selectedImages as image}
      <tr>
        <td><img src={URL.createObjectURL(image)} alt={image.name} /></td>
        {#if processedImages[image.name]}
          <td><img src={processedImages[image.name]} alt={image.name} /></td>
          {:else}
          <td><p>Unprocessed</p></td>
        {/if}
      </tr>
    {/each}
  </table>
</section>

<style>
  section {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
  }

  tr {
    margin-top: 100px;
    width: 80%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin: auto auto;
  }

  td {
    width: 400px;
    border: 1px solid #ddd;
    text-align: center;
  }

  p {
    margin-top: 100px;
  }

  #headline {
    font-size: 15px;
    font-weight: bold;
    padding: 20px;
  }

  img {
    width: 400px;
    padding: 5px;
  }
</style>

