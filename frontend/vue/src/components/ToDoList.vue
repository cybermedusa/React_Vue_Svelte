<template>
    <div class="to-do-list">
        <UserControlPanel @add-to-do="addToDo" />
        <ToDos @delete-todo="deleteToDo" :todos="todos" />
    </div>
</template>

<script>
import UserControlPanel from './UserControlPanel.vue'
import ToDos from './ToDos.vue'
export default {
    name: 'ToDoList',
    components: {
        UserControlPanel,
        ToDos
    },
    methods: {
        async deleteToDo(todo_id) {
            try {
                const res = await fetch(`http://127.0.0.1:8001/${todo_id}`, {
                    method: 'DELETE',
                })
                if (!res.ok) {
                    throw new Error(`HTTP error: ${res.status}`)
                }
                this.todos = this.todos.filter((todo) => todo.id !== todo_id)

            } catch (error) {
                console.dir(error)
            }

        },

        async addToDo(todo) {
            try {
                const res = await fetch('http://127.0.0.1:8001/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(todo),
                })
                if (!res.ok) {
                    throw new Error(`HTTP error: ${res.status}`)
                }
                const data = await res.json()

                this.todos = [...this.todos, data]
            } catch (error) {
                console.dir(error)
            }

        },

        async fetchTodos() {
            const res = await fetch('http://127.0.0.1:8001/')

            const data = await res.json()

            return data
        }

    },
    data() {
        return {
            todos: []
        }
    },
    async created() {
        this.todos = await this.fetchTodos()
    }
}
</script>

<style>
body {
    background-color: #e7e7e7;
    font-family: sans-serif;
}

.to-do-list {
    height: 400px;
    aspect-ratio: 0.8;
    background-color: white;
    margin: 0 auto;
    margin-top: 5em;
    position: relative;
    padding: 15px;
    box-sizing: border-box;
}

.to-do-list>div {
    margin: 15px 0;
}
</style>