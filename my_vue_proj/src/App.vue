<template>
  <div id="app">
    <Headers/>
    <router-view/>
  </div>
</template>

<script>
  import Headers from "@/components/common/Headers"
  export default {
    name: 'App',
    components: {Headers},
  }
</script>

<style>
</style>
