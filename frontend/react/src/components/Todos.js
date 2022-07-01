import { Todo } from "./Todo"

const Todos = ({ todos, onRemove }) => {

    return (
        <>
            {todos.map((todo) => (
                <Todo key={todo.id} todo={todo} onRemove={onRemove} />
            ))}

        </>
    )
}

export default Todos