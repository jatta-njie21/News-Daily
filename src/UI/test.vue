<template>
    <div>
        <h1>Testing testing 1 2</h1>
        <child/>
    </div>
</template>

<script>
    import child from './child.vue';

    export default {
      components: {
        ChildComponent
      }
    }
</script>