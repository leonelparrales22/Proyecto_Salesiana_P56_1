// Componentes principales
import Vue from "vue";
import App from "./App.vue";
// Plugins
import VueRouter from "vue-router";
import Vuelidate from "vuelidate";
// Subrutas
import BienvenidoCajero from "./views/BienvenidoCajero.vue";
import Preventa from "./views/Preventa.vue";
import Clientes from "./views/Clientes.vue";
import Celulares from "./views/Celulares.vue";
import Login from "./views/Login.vue";

Vue.config.productionTip = false;

Vue.filter("moneda", function(valor) {
  // eslint-disable-next-line no-undef
  return accounting.formatMoney(valor);
});
// Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuelidate);

// Principal
const routes = [
  { path: "/celulares/:pagenow?", name: "celulares", component: Celulares },
  { path: "/preventa", component: Preventa },
  { path: "/cliente", component: Clientes },
  { path: "/login", component: Login },
  { path: "/", component: BienvenidoCajero },
  { path: "*", component: BienvenidoCajero },
];
const router = new VueRouter({
  routes,
  mode: "history",
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
