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
import Contenedor from "./views/Contenedor.vue";
import Factura from "./views/Factura.vue";
import Administrador from "./views/Administrador.vue"
import BienvenidoAdministrador from "./components/BienvenidoAdministrador.vue"
import Usuarios from "./views/Usuarios.vue"



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
    { path: "/login", component: Login },
    { path: "/", name: "/", component: Contenedor },
    { path: "*", component: BienvenidoCajero },
    {
        path: "/contenedor",
        component: Contenedor,
        children: [
            { path: "celulares/:pagenow?", name: "celulares", component: Celulares },
            { path: "preventa", component: Preventa },
            { path: "factura", component: Factura },
            //{ path: "factura/:nombre?", name: "facturas", component: Factura },
            { path: "cliente/:pagenow?", name: "clientes", component: Clientes },
            { path: "/", component: BienvenidoCajero },
            { path: "*", component: BienvenidoCajero },
        ],
    },
    {
        path: "/administrador",
        component: Administrador,
        children: [
            { path: "usuarios/:pagenow?", name: "usuarios", component: Usuarios },
            { path: "/", component: BienvenidoAdministrador },
            { path: "*", component: BienvenidoAdministrador },
        ],
    },
];
const router = new VueRouter({
    routes,
    mode: "history",
});

new Vue({
    router,
    render: (h) => h(App),
}).$mount("#app");