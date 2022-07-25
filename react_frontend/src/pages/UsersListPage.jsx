import React, {useState, useEffect} from 'react'
import axios from 'axios'
export const UsersListPage = () => {
    let [users, setUsers] = useState(null)
    useEffect(() => {
        getUsers()
    }, [])

    let getUsers = () => { axios.get(url).then((response) => {
        setUsers(response.data)
    })
}

    if (!users) return null
  return (
    <div>Users</div>
  )
}
