<template>
    <div>
      <div v-for="item in courseList">
        <div class="box">
          <p><img :src="item.course_img" alt="xxx"/></p>
          <h3><router-link :to="{name: 'courseDetail', params:{id: item.id}}">{{item.name}}</router-link></h3>
          <p>{{item.course_type}}</p>
          <p>{{item.brief}}</p>
          <p>{{item.level}}</p>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "Course",
      data(){
          return {
            courseList: []
          }
      },
      mounted: function () {
        this.initCourse();
      },
      methods: {
          initCourse:function () {
          //  向后端发送请求 获取数据 初始化页面
            this.$axios.request({
              url:this.$store.state.apiDict.course,
              method: "GET"
            }).then(res=>{
              if(res.data.code===1000){
                this.courseList = res.data.data;
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
    width: 300px;
    padding: 10px;
  }
</style>
