<template>
  <div>
    <div>
      <h3>{{courseDetailList.course}}</h3>
      <p>{{courseDetailList.career_improvement}}</p>
      <p>{{courseDetailList.course_slogon}}</p>
      <p>{{courseDetailList.prerequisite}}</p>
      <p>{{courseDetailList.what_to_study_brief}}</p>
      <p>{{courseDetailList.why_study}}</p>
      <h4>推荐课程</h4>
      <ul v-for="item in courseDetailList.recommend_courses">
        <li><span @click="clickHandler(item.id)">{{item.name}}</span></li>
      </ul>
      <h4>讲师</h4>
      <ul v-for="item in courseDetailList.teacher">
        <li>{{item.name}}</li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "CourseDetail",
    data() {
      return {
        courseDetailList: []
      }
    },
    mounted: function () {
      var courseId = this.$route.params.id;
      this.initCourseDetail(courseId);
    },
    methods: {
      initCourseDetail: function (courseId) {
        this.$axios.request({
          url: this.$store.state.apiDict.course + courseId + "/",
          method: "GET"
        }).then(res => {
          if(res.data.code===1000){
            this.courseDetailList = res.data.data;
          }else{
            alert(res.data.error);
          }
        }).catch(res => {
          alert(res);
        })
      },
      clickHandler: function (courseId) {
        this.initCourseDetail(courseId);
        this.$router.push({name: "courseDetail", params: {id: courseId}});
      }
    },
  }
</script>

<style scoped>

</style>
