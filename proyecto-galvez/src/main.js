import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import BienvenidoCajero from "./components/BienvenidoCajero.vue";
import Preventa from "./components/Preventa.vue";
import Clientes from "./components/Clientes.vue";
import Celulares from "./components/Celulares.vue";

Vue.config.productionTip = false;

Vue.filter("moneda", function(valor) {
  // eslint-disable-next-line no-undef
  return accounting.formatMoney(valor);
});

Vue.use(VueRouter);
const routes = [
  { path: "/celulares/:pagenow?", name: "celulares", component: Celulares },
  { path: "/preventa", component: Preventa },
  { path: "/cliente", component: Clientes },
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
