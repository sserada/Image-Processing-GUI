<script lang='ts'>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  function send() {
    dispatch('send');
  }
</script>

<button on:click={send}>Send</button>

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

