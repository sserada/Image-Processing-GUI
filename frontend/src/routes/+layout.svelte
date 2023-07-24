<script>
  import Header from '$lib/components/Header.svelte';
</script>

<div class="app">

  <header>
    <Header />
  </header>

	<main>
		<slot />
	</main>

</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

  header {
    position: sticky;
    top: 20;
    z-index: 1;
    margin: 40px auto;
    padding: 0 5rem;
  }
</style>
