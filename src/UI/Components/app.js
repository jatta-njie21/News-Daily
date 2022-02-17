const route = [
    {path: '/home', component : home},
]

const router = new VueRouter({
    routes
})

const app = new Vue({
    router
}).$mount('#app')