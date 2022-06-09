import { createApp } from 'vue';
import App from './App.vue';
import routes from './router/router';
import VueSession from 'vue-session';
// import BootstrapVue3 from 'bootstrap-vue-3';
// import { PaginationNavPlugin } from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css';
// import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';

// import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

const app = createApp(App);

app.use(routes);
app.use(VueSession);
// app.use(BootstrapVue3);
// app.use(PaginationNavPlugin);
// app.use(BootstrapVue);
// app.use(BootstrapVueIcons);
app.mount('#app');