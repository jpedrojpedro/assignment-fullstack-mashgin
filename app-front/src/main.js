import Vue from 'vue'
import App from './App.vue'
import {apply_currency} from "./filters";

Vue.filter("apply_currency", apply_currency)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
