<template>
	<div class="Login_user">
		<div class= "container_login_user">
			<h2>Iniciar Sesion</h2>

			<form v-on:submit.prevent="processLoginUser">
				<input type="text" v-model="user.username" placeholder="Username">
				<br>
				<input type="password" v-model="user.password" placeholder="Password">
				<br>
				<button type="Submit">Iniciar Sesion</button>
			</form>
		</div>
	</div>
</template>
<script>
import axios from 'axios'

export default{
	name: "Login",
	data: function(){
		return{
			user:{
				username: "",
				password: "",
			}
		}
	},
	methods:{
		processLoginUser: function(){
			axios.post(
				"https://tiendaproyecto-be.herokuapp.com/login/",
				this.user,
				{headers:{}}
				)
				.then((result) => {
					let dataLogin={
						username: this.user.username,
						token_acces: result.data.acces,
						token_refresh: result.data.refresh,
					}

					this.$emit('completedLogin', dataLogin)
				})
				.catch((error)=>{
					if(error.response.status =="401")
						alert("ERROR 401: Credenciales incorrectas");
				});
			}
		}
}
</script>


<style>
	.Login_user{
		margin:0;
		padding: 0;
		height: 100%;
		width: 100%;

		display: flex;
		justify-content: center;
		align-items:center;
	}
	
	.container_login_user{
		border:3px solid violet;
		border-radius: 10px;
		width:25%;
		height: 60%;

		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	
	.Login_user h2{
		color: purple
	}

	.Login_user input{
		height: 40px;
		width: 100%;

		box-sizing: border-box;
		padding: 10px 20px;
		margin:5px 0;

		border: 1px solid black;
	}

	.Login_user button{
		width: 100%;
		height: 40px;

		color: white;
		background-color: purple;
		border: 1px solid black;

		border-radius: 5px;
		padding:10px 25px;
		margin:5px 0 ;	
	}

	.Login_user button:hover{
		color: black;
		background: crimson;
		border: 1px solid slategrey;		
	}

</style>
