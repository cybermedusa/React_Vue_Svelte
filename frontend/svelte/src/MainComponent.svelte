<script>
	let newItem = "";

	let todoList = [];

	let todo;
	import { onMount } from "svelte";

	onMount(async () => {
		const response = await fetch("http://localhost:8001", {
			method: "GET",
			headers: { "Content-type": "application/json" },
		});
		const data = await response.json();
		console.log(data);
		todoList = data;
	});

	async function addToList() {
		const response = await fetch("http://localhost:8001", {
			method: "POST",
			headers: {
				"Content-type": "application/json",
			},
			body: JSON.stringify({ text: newItem }),
		});
		const insertedItem = await response.json();

		console.log(insertedItem);
		todoList = [...todoList, insertedItem];
		newItem = "";
	}

	function removeFromList(index) {
		let id = todoList[index].id;
		todoList.splice(index, 1);
		todoList = todoList;
		let url = "http://localhost:8001/" + id;
		const response = fetch(url, {
			method: "DELETE",
		});
	}
</script>

<input bind:value={newItem} type="text" placeholder="new todo item.." />
<button on:click={addToList}>Add</button>

<br />
{#each todoList as item, index}
	<input bind:checked={item.status} type="checkbox" />
	<span class:checked={item.status}>{item.text}</span>
	<span on:click={() => removeFromList(index)}>❌</span>
	<br />
{/each}

<style>
	.checked {
		text-decoration: line-through;
	}
</style>
