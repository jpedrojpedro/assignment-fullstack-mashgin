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
      <div class="row row-cols-1 row-cols-sm-2 row-cols-sm-3 row-cols-md-4 g-4">
          <Product
              v-for="p in products"
              v-bind:key="p.id"
              :img_path="build_assets_url(p.image_id)"
              :name="p.name"
              :price="p.price"
              @add="added"
          />
      </div>
      <footer class="footer fixed-bottom mt-auto py-2 bg-light" v-if="total">
          <span class="font-weight-black">{{ total | apply_currency }}</span>
      </footer>
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
            total: 0,
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
        },
        added({value}) {
            this.total += value
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
