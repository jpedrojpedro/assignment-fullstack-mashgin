<template>
    <div class="card" style="width: 18rem;">
        <img :src="img_path" class="card-img-top" alt="...">
        <div class="card-body">
            <p class="card-text">{{ name }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Product",
        props: {
            img_path: String,
            name: String,
        }
    }
</script>

<style scoped>

</style>
