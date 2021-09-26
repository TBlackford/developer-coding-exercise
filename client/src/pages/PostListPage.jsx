import React, { useEffect, useState } from "react";
import PostListItem from "../components/PostListItem";



const PostListPage = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        // Ideally, I'd move this to an ENV variable
        fetch('http://localhost:8000/posts/')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setPosts(data)
            });
    }, [setPosts])

    return (
        <div>
            <h1>Posts</h1>
            <ul>
                {posts.map(post => <PostListItem slug={post} title={post} key ={post} />)}
            </ul>
        </div>
    )
}

export default PostListPage;