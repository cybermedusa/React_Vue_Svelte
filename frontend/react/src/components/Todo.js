
export const Todo = ({ todo, onRemove }) => {

    return (
        <div>
            <h4>
                {todo.text}
                <button className="btn" onClick={() => onRemove(todo.id)}>Remove</button>
            </h4>
        </div>
    )
}

export default Todo