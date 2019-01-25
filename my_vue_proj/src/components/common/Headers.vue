<template>
  <div>
    <li v-for="item in headerList">
      <router-link :to="{name: item.name}" :key="item.id">{{item.title}}</router-link>
    </li>
    <div v-if="this.$store.state.token">
      <a href="#">{{this.$store.state.username}}</a>
      <span @click="logoutHandler">注销</span>
    </div>
    <router-link v-else to="/login">登录</router-link>
  </div>

</template>

<script>
  export default {
    name: "Headers",
    data() {
      return {
        headerList: [
          {id: 1, title: "首页", name: "index"},
          {id: 2, title: "专题课程", name: "course"},
          {id: 3, title: "深科技", name: "news"},
        ]
      }
    },
    methods: {
      logoutHandler: function () {
        this.$store.commit("clearToken");
      }
    }
  }
</script>

<style scoped>

</style>
