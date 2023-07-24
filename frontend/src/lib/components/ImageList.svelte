<script lang='ts'>
  export let selectedImages: FileList;
</script>

<section>
  <table>
    <tr>
      <td>Selected Images</td>
      <td>Processed Images</td>
    </tr>
    {#each selectedImages as image}
      <tr>
        <td><img src={URL.createObjectURL(image)} alt={image.name} /></td>
        <td><img src={URL.createObjectURL(image)} alt={image.name} /></td>
      </tr>
    {/each}
  </table>
</section>

<style>
  section {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 100px;
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
    width: 300px;
    border: 1px solid #ddd;
    padding: 20px;
    text-align: center;
  }

  img {
    width: 300px;
  }
</style>

