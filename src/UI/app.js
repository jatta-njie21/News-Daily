const routes = [
    {path: '/home', component: home}
]

const router = VueRouter.createRouter({
    routes
})

const app = Vue.createApp({})

app.use(router)

app.mount('#app')