
<script>
export default {
  name: 'App',

  data: function(){
      return{
        is_auth: false
      }
  },

  components: {
  },

  methods:{
    verifyAuth: function() {
    this.is_auth = localStorage.getItem("isAuth") || false;

    if(this.is_auth == false)
      this.$router.push({name: "logIn"});
    else
      this.$$router.push({name: "Home"});
    },

    loadLogIn: function(){
      this.$router.push({name: "logIn"})
    },

    loadSignUp: function(){
      this.$router.push({name: "signUp"})
    },

    completedLogIn: function(data) {
      localStorage.setItem("isAuth",true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token.access);
      localStorage.setItem("token_refresh", data.token.refresh);
      alert("Autentificacion Exitosa!")
      this.verifyAuth();
    },

    completedSignUp: function(data) {
      alert("Registro Exitozidao");
      this.completedLogIn(data);
    },

    loadHome: function(){
      this.$router.push({name: "Home"});
    },

    logOut: function(){
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },

    loadAccount: function(){
      this.$router.push({name: 'Account'})
    }

  },

  created: function(){
    this.verifyAuth()
  }

}
</script>

