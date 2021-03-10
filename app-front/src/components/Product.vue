<template>
    <div class="col product-card">
        <div class="card" style="width: 18rem;">
            <img :src="img_path" class="card-img-top" :alt="name" style="width: 18rem; height: 18rem;">
            <div class="card-body">
                <p class="card-text">{{ name }}</p>
                <p class="card-text">{{ price | apply_currency }}</p>
                <button type="button" class="btn btn-sm btn-outline-primary" @click="add_to_cart">Add</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Product",
        props: {
            img_path: String,
            name: String,
            price: Number,
        },
        methods: {
            add_to_cart() {
                this.$emit("add_to_cart", {amount: this.price})
            }
        }
    }
</script>

<style scoped>

</style>
