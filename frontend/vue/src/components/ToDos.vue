<template>
    <div class="to-dos">
        <div :key="todo.id" v-for="todo in todos">
            <ToDo @delete-todo="$emit('delete-todo', todo.id)" :todo="todo" />
        </div>
    </div>
</template>

<script>
import ToDo from './ToDo.vue'
export default {
    name: 'ToDos',
    components: {
        ToDo
    },
    props: {
        todos: Array
    },
    emits: ['delete-todo']
}
</script>

<style>
.to-dos {
    position: relative;
    display: flex;
    flex-direction: column;
    row-gap: 10px;
    height: 250px;
    overflow-y: scroll;
}
</style>