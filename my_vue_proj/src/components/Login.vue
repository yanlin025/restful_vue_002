<template>
  <div>
    <p><input type="text" placeholder="请输入用户名" v-model="username"/></p>
    <p><input type="password" placeholder="请输入密码" v-model="password"/></p>
    <p><input @click="loginHandler" type="submit" value="登录"/></p>
  </div>
</template>

<script>
  export default {
    name: "Login",
    data(){
      return {
        username: "",
        password: "",
      }
    },
    methods: {
      loginHandler: function () {
        this.$axios.request({
          url: "http://127.0.0.1:8000/api/v1/login/",
          method: "POST",
          data: {
            user: this.username,
            pwd: this.password
          },
          headers: {
            "Content-Type": "application/json"
          }
        }).then(res=>{
          if(res.data.code===1000){
            this.$store.commit("saveToken", {username: this.username, token: res.data.token});
            var url = this.$route.query.backUrl;
            if(url){
              this.$router.push({path: url});
            }else{
              this.$router.push({name: "index"});
            }
          }else{
            alert(res.data.error);
          }
        }).catch(res=>{
          alert(res);
        })
      }
    }
  }
</script>

<style scoped>

</style>
