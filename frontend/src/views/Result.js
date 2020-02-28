import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Result = (props) => {
	// const [img, setImg] = useState();
	const [src, setSrc] = useState(0);

	const onClickHandler = (e) => {
		e.preventDefault();
		setSrc(props.data.imgData);
	}

	useEffect(() => {
		setSrc(props.data.threshData);
	}, [props.data])

	return(
		<div>
			<h3>You have this many puzzle pieces:</h3>
			<h1>{props.data.count}</h1>
			<img id='Outlines' style={{width: 500 + 'px'}} src={"data:image/png;base64," + src} onClick = {onClickHandler}></img>
			{/* <img id='Threshold' style={{width: 500 + 'px'}} src={"data:image/png;base64," + props.data.threshData}></img> */}
		</div>
	)
}

export default Result;