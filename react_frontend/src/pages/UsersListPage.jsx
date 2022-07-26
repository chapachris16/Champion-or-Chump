import React, {useState, useEffect} from 'react'
import axios from 'axios'
export const UsersListPage = () => {
    const [post, setPosts] = useState(null)
    useEffect(() => {
        axios.get('http://localhost:8000/api/').then((post) => {
           setPosts(post)
    })
    }, [])

    if (!post) return null
//     const getPosts = async () => { await axios.get('http://localhost:8000/api/').then((response) => {
//        data = setPosts(response.data)
//     })
// }

    if (!post) return null
  return (
    <>
        {post.data.map((post, id) => (
        <ul key={id}>
            <li>{post.user}</li>
            <li>{post.subject}</li>
            <li>{post.content}</li>
            
        </ul> 
        ))}
    </>
    
  )
}
