import axios from "axios"
import { useEffect, useState } from "react"

export default function Todo () {
    const [ todoList, setTodoList] = useState<any>()

    useEffect(() => {
        fetchTodos();
    },[])

    async function fetchTodos () {
        const res = await axios.get("http://localhost:8000/")
        setTodoList(res);
    }

    function addTodos () {
        const res = axios.post("http://localhost:8000/add", {
            desc: "오늘 할거"
        })
        console.log(res)
    }

    console.log(todoList)
    return (
        <div>
            {todoList?.data[0]?.description}
        </div>
    )
}