const routes = [
    {path: '/home', component: home},
    {path: '/contact', component: contact},
    {path: '/authors', component: layout},
]

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes,
})

const app = Vue.createApp({})

app.use(router)

app.mount('#app')