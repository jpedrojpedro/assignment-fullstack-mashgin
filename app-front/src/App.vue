<template>
  <div id="app">
      <Product
              img_path="https://www.alegrafoods.com.br/wp-content/uploads/2020/09/hot-dogs-pwy2hz8-620x350.jpg"
              name="Cachorro Quente"
      />
      {{ categories }}
      {{ products }}
      Complete: {{ full_info }}
  </div>
</template>

<script>
import axios from 'axios'
import Product from './components/Product.vue'
import data from './menu.json'

export default {
    name: 'App',
    components: {
        Product,
    },
    data() {
        return {
            categories: data.categories,
            products: data.products,
            full_info: null,
        }
    },
    mounted() {
      axios
        .get('http://localhost:5000/menu')
        .then(response => (this.full_info = response))
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
