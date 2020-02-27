import React, { useState, useEffect } from 'react';
import HomeForm from './HomeForm';
import Result from './Result';

const Main = () => {
	const [uploaded, setUploaded] = useState(false);
	const [puzzleData, setPuzzleData] = useState({});

	const onUpload = (data) => {
		setUploaded(true);
		setPuzzleData(data.data);
	}

	useEffect(() => {
		console.log(puzzleData);
	},[puzzleData])

	return(
		<div>
			{!uploaded &&
				<HomeForm onUpload={onUpload}/>
			}
			{uploaded &&
				<Result data={puzzleData}/>
			}
		</div>
	)
}

export default Main;
