<template>
  <div>
      <div v-for="item in newsList">
        <div class="box">
          <p><img :src="item.head_img" alt="xxx"/></p>
          <h3><router-link :to="{name: 'newsDetail', params:{id: item.id}}">{{item.title}}</router-link></h3>
          <p>{{item.brief}}</p>
          <p>{{item.source}}</p>
          <p>{{item.date}}</p>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    name: "News",
    data(){
      return {
        newsList: [],
      }
    },
    mounted: function(){
      this.initNews();
    },
    methods: {
      initNews: function () {
        this.$axios.request({
          url: this.$store.state.apiDict.news,
          method: "GET",
          params: {token: this.$store.state.token}
        }).then(res=>{
          if(res.data.code===1000){
            this.newsList = res.data.data;
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
.box {
  width: 700px;
  padding: 10px;
}
</style>
