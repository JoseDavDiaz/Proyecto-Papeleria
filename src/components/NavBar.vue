<template>
  <div id="nav-bar">
    <router-link to="/products" id="products-link">
      <h1>PAPELERIA FUSION COLOR</h1>
           
    </router-link>
    <router-link to="/cart" id="cart-link">
      <button>Compra</button>
      <button>Iniciar Sesion</button>
      <button>Cerrar Sesion</button>
    </router-link>
  
    <router-link to="/login" id="login-link">
      <h5>Iniciar sesion</h5>
    </router-link>
    
  </div>
  
</template>

<script>
export default {
    name: 'NavBar',
}
</script>

<style scoped>
  #nav-bar {
    border-bottom: 1px solid #ddd;
    height: 75px;
    width: 100%;
  }

  #products-link {
    text-align: center;
    display: block;
    color: #34568B;
    font-size: 19px;
    left: 32px;
    position: absolute;
    top: 16px;
    text-decoration: none;
  }

  #products-link h1 {
      margin: 0;
  }

  #cart-link {
    position: absolute;
    right: 16px;
    top: 16px;
  }
</style>
