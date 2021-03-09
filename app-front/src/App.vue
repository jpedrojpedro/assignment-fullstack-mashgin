<template>
  <div id="app">
      <Product
              img_path="https://www.alegrafoods.com.br/wp-content/uploads/2020/09/hot-dogs-pwy2hz8-620x350.jpg"
              name="Cachorro Quente"
      />
      {{ categories }}
  </div>
</template>

<script>
import Product from './components/Product.vue'

import data from './menu.json'

// testar axios aqui dentro

export default {
    name: 'App',
    components: {
        Product,
    },
    data() {
        return {
            categories: data.categories,
            products: data.products,
        }
    }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
