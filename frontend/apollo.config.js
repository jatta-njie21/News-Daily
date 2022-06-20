// // apollo.config.js
// module.exports = {
//     client: {
//       // service: {
//       //   name: 'frontend',
//       //   // URL to the GraphQL API
//       //   url: 'http://localhost:8080/graphql',
//       // },
//       // Files processed by the extension
//       includes: [
//         'src/**/*.vue',
//         'src/**/*.js',
//       ],
//     },
//   }
import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'

  // HTTP connection to the API
const httpLink = createHttpLink({
  uri: 'http://127.0.0.1:8000/graphql', // Matches the url that Django is using
})

  // Cache implementation
const cache = new InMemoryCache()

  // Create the apollo client
const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
})