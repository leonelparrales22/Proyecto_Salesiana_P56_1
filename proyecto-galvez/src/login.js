import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import Celulares from "./components/Celulares.vue";



Vue.config.productionTip = false;

Vue.use(VueRouter);
const routes = [
  { path: "/login", component: Celulares },
];
const router = new VueRouter({
  routes,
  mode: "history",
});
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#login");
