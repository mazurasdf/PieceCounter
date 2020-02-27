import React, { useState } from 'react';
import axios from 'axios';
import loadingGIF from '../loading.gif';

const HomeForm = (props) => {
	const [form, setForm] = useState({
		image: null
	});
	const [loading, setLoading] = useState(false);

	const onChangeHandler = (e) => {
        e.preventDefault();
        setForm({
          image: e.target.files[0]
        })
	}
	
	const onSubmitHandler = (e) => {
		e.preventDefault();
		setLoading(true)

		let form_data = new FormData();
		form_data.append('image', form.image, form.image.name);
		let url = "http://localhost:8000/api/puzzle_pieces/send/"

		axios.post(url, form_data, {
			headers: {
				'content-type': 'multipart/form-data'
			}
		})
			.then(res => {
				setLoading(false);
				props.onUpload(res);
				console.log(res);
			})
			.catch(err => {
				setLoading(false);
				console.log(err)
			});
	}

	return(
		<div>
			<h1 className="page-header">Piece Counter</h1>
			<form onSubmit={onSubmitHandler}>
				<input 	type="file"
						id="image"
						name="image"
						onChange={onChangeHandler} 
						accept="image/png, image/jpeg"
						className="form-control-file mx-auto col-3"
				/>
				<br />
				{
					loading &&
					<img src={loadingGIF} alt="Loading" className="col-1"/>
				}
				<br />
				<input
					type="submit"
					className="btn btn-success"
				/>
			</form>
		</div>
	)
}

export default HomeForm;