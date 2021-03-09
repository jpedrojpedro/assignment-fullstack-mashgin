<template>
    <div class="col">
        <div class="card" style="width: 18rem;">
            <img :src="img_path" class="card-img-top" :alt="name" style="width: 18rem; height: 18rem;">
            <div class="card-body">
                <p class="card-text">{{ name }}</p>
                <p class="card-text">{{ format_currency }}</p>
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
            price: String,
        },
        computed: {
            format_currency() {
                return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(parseFloat(this.price))
            }
        }
    }
</script>

<style scoped>

</style>
