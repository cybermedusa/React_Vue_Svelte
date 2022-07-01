import AddTodo from "./components/AddTodo";
import Todos from "./components/Todos";
import { useState, useEffect } from "react";

function App() {
  const [todos, setTodos] = useState([])

  useEffect(() => {
    const getTodos = async () => {
      const todosFromServer = await fetchTodos()
      setTodos(todosFromServer)
    }
    getTodos()
  }, [])

  const fetchTodos = async () => {
    const response = await fetch('http://localhost:8001')
    const data = await response.json()
    return data
  }


  const addTodo = async (todo) => {
    const response = await fetch('http://localhost:8001', {
      method: "POST",
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(todo)
    })
    const data = await response.json()

    setTodos([...todos, data])

  }

  const removeTodo = async (id) => {
    await fetch(`http://localhost:8001/${id}`, {
      method: "DELETE",
    })
    setTodos(todos.filter((todo) => todo.id !== id))
  }

  return (
    <div className="container">
      <AddTodo onAdd={addTodo} />
      <Todos todos={todos} onRemove={removeTodo} />
    </div>
  );
}

export default App;
