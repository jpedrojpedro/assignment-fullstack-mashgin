<template>
  <div id="app">
      <select class="form-select" aria-label="Default select example">
          <option selected>Select category...</option>
          <option
              v-for="c in categories"
              v-bind:key="c.id"
              :value="c.id"
          >{{ c.name }}</option>
      </select>
      <Product
          v-for="p in products"
          v-bind:key="p.id"
          :img_path="build_assets_url(p.image_id)"
          :name="p.name"
      />
  </div>
</template>

<script>
import axios from 'axios'
import Product from './components/Product.vue'

export default {
    name: 'App',
    components: {
        Product,
    },
    data() {
        return {
            categories: [],
            products: [],
        }
    },
    beforeMount() {
      axios
        .get('http://localhost:5000/menu')
        .then(response => {
            this.categories = response.data.categories
            this.products = response.data.products
        })
    },
    methods: {
        build_assets_url(filename) {
            return `http://localhost:5000/assets/${filename}.jpg`
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
