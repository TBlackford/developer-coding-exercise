import React from "react";


const TagList = (props) => {
    return (
        <p>{props.tags.join(", ")}</p>
    )
}

export default TagList;