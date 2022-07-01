import { useState } from "react"

const AddTodo = ({ onAdd }) => {
    const [text, setText] = useState('')
    const onSubmit = () => {
        if (!text) {
            alert('Add todo')
            return
        }
        onAdd({ text })

        setText('')
    }
    return (
        <div>
            <header className="header">My todos</header>
            <input className="input-box" placeholder="Enter new todo" value={text} onChange={(event) => setText(event.target.value)}></input>
            <button className="btn" onClick={onSubmit}>Add</button>
        </div>

    )
}

export default AddTodo