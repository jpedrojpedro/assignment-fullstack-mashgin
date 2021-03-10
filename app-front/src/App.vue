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
              @add_to_cart="update_total_amount"
          />
      </div>
      <footer class="footer fixed-bottom mt-auto py-2 bg-light" v-if="total_amount">
          <div class="row">
            <div class="col">
                <span class="font-weight-black me-2"><b>Total:</b>&nbsp;{{ total_amount | apply_currency }}</span>
            </div>
            <div class="col">
                <button type="button" class="btn btn-sm btn-outline-primary" @click="clear_cart">Empty Cart</button>
            </div>
          </div>
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
            total_amount: 0,
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
        update_total_amount({amount}) {
            this.total_amount += amount
        },
        clear_cart() {
            this.total_amount = 0
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
