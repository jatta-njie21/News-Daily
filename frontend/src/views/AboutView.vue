<template>
  <div class="about">
    <h1>This is an about page</h1>
    <GetAuthors/>
  </div>
</template>

<script>
// @ is an alias to /src
import GetAuthors from '@/components/GetAuthors.vue'

export default {
  components: {
    GetAuthors,
  },
}
</script>