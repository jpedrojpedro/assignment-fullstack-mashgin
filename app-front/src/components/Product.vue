<template>
    <div class="col">
        <div class="card" style="width: 18rem;">
            <img :src="img_path" class="card-img-top" :alt="name" style="width: 18rem; height: 18rem;">
            <div class="card-body">
                <p class="card-text">{{ name }}</p>
                <p class="card-text">{{ price | apply_currency }}</p>
                <button type="button" class="btn btn-sm btn-outline-primary" @click="foo">Add</button>
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
            foo() {
                this.$emit("add", {value: this.price})
            }
        }
    }
</script>

<style scoped>

</style>
