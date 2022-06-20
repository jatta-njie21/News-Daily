import { createApp, provide, h } from 'vue'
import App from './App.vue'
import router from './router'
import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'
import { apolloClient } from "@/apollo-config";

import './index.css'

// HTTP connection to the API
// const httpLink = createHttpLink({
//     // You should use an absolute URL here
//     uri: 'http://127.0.0.1:8000/graphql',
//   })

// // Cache implementation
// const cache = new InMemoryCache()

// // Create the apollo client
// const apolloClient = new ApolloClient({
//   link: httpLink,
//   cache,
// })

const app = createApp({
  setup () {
    provide(DefaultApolloClient, apolloClient)
  },

  render: () => h(App),
})

createApp(App).use(router).mount('#app')
