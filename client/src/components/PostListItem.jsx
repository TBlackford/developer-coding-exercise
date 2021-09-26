import React from "react";

import { Link } from "react-router-dom";


const PostListItem = (props) => {
    return (
        <li>
            <Link to={`/${props.slug}`}>{props.title}</Link>
        </li>
    )
}

export default PostListItem;