<template>
    <h4>Todo App</h4>
    <div class="user-control-panel">
        <input class="input-box" v-model="toDoText" />
        <button @click="addToDo()" class="add-button"><img src='./icons/plus.png' /></button>
    </div>
</template>

<script>
export default {
    name: 'UserControlPanel',
    emits: ['add-to-do'],
    methods: {
        addToDo() {
            const todo = {
                text: this.toDoText
            }
            this.$emit('add-to-do', todo)
            this.toDoText = ''
        }
    },
    data() {
        return {
            toDoText: ""
        }
    }
}
</script>

<style scoped>
.user-control-panel {
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.input-box {
    width: 80%;
    position: relative;
}

.add-button {
    color: white;
    width: 25px;
    aspect-ratio: 1;
    position: relative;
    cursor: pointer;
}

img {
    width: 100%;
}
</style>
