<script lang='ts'>
  function reset() {
    window.location.reload();
  }
</script>

<button on:click={reset}>Reset</button>

<style>
  button {
    background-color: #333;
    border: 1px solid #ccc;
    border-radius: 30px;
    color: #eee;
    cursor: pointer;
    font-size: 1.2rem;
    font-weight: bold;
    padding: 0.5rem 1rem;
  }

  button:hover {
    background-color: #111;
  }
</style>

