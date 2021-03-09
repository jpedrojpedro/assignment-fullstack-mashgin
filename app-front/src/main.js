import Vue from 'vue'
import App from './App.vue'
// import axios from "axios"

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  // el: '#app',
  // data () {
  //   return {
  //     info: null
  //   }
  // },
  // mounted () {
  //   axios
  //     .get('http://localhost:5000/menu')
  //     .then(response => (this.info = response))
  // }
}).$mount('#app')
