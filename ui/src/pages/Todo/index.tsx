import axios from "axios"
import { useEffect } from "react"

export default function Todo () {
    useEffect(() => {
        fetchTodos();
    },[])

    function fetchTodos () {
        const res = axios.get("http://127.0.0.1:8000/")
        console.log(res)
    }

    return (
        <div>
    </div>
    )
}