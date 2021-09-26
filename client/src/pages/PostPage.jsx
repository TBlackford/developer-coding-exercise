import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import ReactMarkdown from 'react-markdown'
import TagList from "../components/TagList";


const PostPage = (props) => {
    const [isLoading, setIsLoading] = useState(true);
    const [post, setPost] = useState({});

    useEffect(() => {
        // Ideally, I'd move this to an ENV variable
        fetch('http://localhost:8000/posts/' + props.match.params.slug + '/')
            .then(response => response.json())
            .then(data => {
                console.log(data.post);
                setPost(data.post)
                setIsLoading(false);
            });
    }, [setPost, props.match.params.slug])

    return isLoading && <div>Loading...</div> || (
        <div>
            <Link to="/">Home</Link>

            <h1>{post.title}</h1>
            <h2>{post.author}</h2>

            <ReactMarkdown children={post.content} />

            <h3>Tags</h3>
            <TagList tags={post.tags} />
        </div>
    )
}

export default PostPage;