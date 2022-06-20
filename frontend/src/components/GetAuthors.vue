<template>

<div class="relative overflow-x-auto shadow-md sm:rounded-lg">
<table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
<thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
<tr>
<th scope="col" class="px-6 py-3">
Name
</th>
<th scope="col" class="px-6 py-3">
Surname
</th>
<th scope="col" class="px-6 py-3">
Number
</th>
<th scope="col" class="px-6 py-3">
Email
</th>
<th scope="col" class="px-6 py-3">
<span class="sr-only">Edit</span>
</th>
</tr>
</thead>
<tbody>
<tr v-for="authors of result.allAuthors" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
<th scope="row" class="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap">
{{authors.firstName}}
</th>
<td class="px-6 py-4">
{{authors.lastName }}
</td>
<td class="px-6 py-4">
{{authors.phoneNumber}}
</td>
<td class="px-6 py-4">
${{authors.email}}
</td>
<td class="px-6 py-4 text-right">
<a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
</td>
</tr>
</tbody>
</table>
</div>

</template>

<script>
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'

export default {
  setup () {
    const { result } = useQuery(gql`
      query getAllAuthors {
        allAuthors {
          firstName
          lastName
          phoneNumber
          email
        }
      }
    `)

    return {
      result,
    }
  },
}
</script>