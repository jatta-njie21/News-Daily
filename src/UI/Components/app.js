import Home from './home.js'

const routes = {
    '/': Home,
}

const router = new VueRouter({
    routes
})

const app = new Vue({
    router
}).$mount('#app')