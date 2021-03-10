<template>
    <div id="app">
        <div class="row">
            <div class="col"></div>
            <div class="col mb-3">
                <input id="search-product" type="text" class="form-control" placeholder="Type desired product name"
                   aria-label="Search for products" aria-describedby="button-addon2" v-on:keyup="search_elements">
            </div>
            <div class="col"></div>
        </div>
        <div id="products-list" class="row row-cols-1 row-cols-sm-2 row-cols-sm-3 row-cols-md-4 g-4 mb-5">
            <Product
                v-for="p in products"
                v-bind:key="p.id"
                :id="p.id"
                :img_path="build_assets_url(p.image_id)"
                :name="p.name"
                :price="p.price"
                @add_to_cart="update_order"
            />
        </div>
        <footer class="footer fixed-bottom py-2 bg-light" v-if="total_amount">
            <div class="row">
                <div class="col">
                    <span class="font-weight-black me-2"><b>Total:</b>&nbsp;{{ total_amount | apply_currency }}</span>
                </div>
                <div class="col">
                    <button type="button" class="btn btn-sm btn-outline-primary" @click="finish_order">Finish Order</button>
                </div>
                <div class="col">
                    <button type="button" class="btn btn-sm btn-outline-secondary" @click="clear_cart">Empty Cart</button>
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
            order: null,
            items: [],
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
        update_order(payload) {
            this.items.push(payload)
            this.total_amount += payload.price
            if (!this.order) {
                axios
                    .post('http://localhost:5000/orders')
                    .then(response => {
                        console.log("Route: create_order :: " + response.data.number)
                        this.order = response.data.id
                    })
            }
        },
        finish_order() {
            this.items.forEach((item) => {
                axios
                    .get(`http://localhost:5000/orders/${this.order}/products/${item.product_id}/add`)
                    .then(response => {
                        console.log("Route: add_product :: " + response.data)
                    })
            })
            this.clear_cart()
        },
        clear_cart() {
            this.order = null
            this.items = []
            this.total_amount = 0
        },
        search_elements() {
            let input, filter, pl, pi, a, i, txtValue;
            input = document.getElementById('search-product');
            filter = input.value.toUpperCase();
            pl = document.getElementById("products-list");
            pi = pl.getElementsByClassName('product-card');

            for (i = 0; i < pi.length; i++) {
                a = pi[i].getElementsByTagName("p")[0];
                txtValue = a.textContent || a.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    pi[i].style.display = "";
                } else {
                    pi[i].style.display = "none";
                }
            }
        },
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
