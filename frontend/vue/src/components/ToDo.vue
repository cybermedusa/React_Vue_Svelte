<template>
    <div class="to-do">
        <h3>{{ todo.text }}</h3>
        <img @click="DeleteToDo(todo.id)" src="./icons/bin.png" />
    </div>
</template>

<script>
export default {
    name: 'ToDo',
    props: {
        todo: Object
    },
    methods: {
        DeleteToDo(id) {
            this.$emit('delete-todo', id)
        }
    }
}
</script>

<style scoped>
img {
    height: 20px;
    aspect-ratio: 1;
    cursor: pointer;
}

h3 {
    font-size: .8em;
}

.to-do {
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #f2f2f2;
    height: auto;
    box-sizing: border-box;
    padding: 5px;
}
</style>