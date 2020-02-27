import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Result = (props) => {
	const [img, setImg] = useState();

	// useEffect(() => {
	// 	axios.get('http://localhost:8000/api/puzzle_pieces/read_img/')
	// 		.then(res => console.log(res))
	// 		.catch(err => console.log(err));
	// }, [img])

	return(
		<div>
			<h3>You have this many puzzle pieces:</h3>
			<h1>{props.data.count}</h1>
		</div>
	)
}

export default Result;