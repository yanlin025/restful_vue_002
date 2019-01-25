<template>
  <div>
    <div>
      <h3>{{newsDetailList.title}}</h3>
      <p>{{newsDetailList.content}}</p>
      <p>{{dateFormat(newsDetailList.pub_date)}}</p>
      <p>{{dateFormat(newsDetailList.offline_date)}}</p>
      <p>{{newsDetailList.status}}</p>
      <p>
        <span @click="collect">收藏({{newsDetailList.collect_num}})</span>
        <span>阅读({{newsDetailList.view_num}})</span>
        <span @click="agree">点赞({{newsDetailList.agree_num}})</span>
        <span>评论({{newsDetailList.comment_num}})</span>
      </p>
      <div class="comm">
        <textarea v-model="commentContent"/>
        <input @click="commentHandler" type="submit" value="评论"/>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "NewsDetail",
    data() {
      return {
        newsDetailList: [],
        commentContent: ""
      }
    },
    mounted: function () {
      var newsId = this.$route.params.id;
      this.initNewsDetail(newsId);
    },
    methods: {
      initNewsDetail: function (newsId) {
        this.$axios.request({
          url: this.$store.state.apiDict.news + newsId + "/",
          method: "GET",
          params: {token: this.$store.state.token}
        }).then(res => {
          if (res.data.code === 1000) {
            this.newsDetailList = res.data.data;
          } else {
            alert(res.data.error);
          }
        }).catch(res => {
          alert(res);
        })
      },
      //时间格式化函数，此处仅针对yyyy-MM-dd hh:mm:ss 的格式进行格式化
      dateFormat: function (time) {
        var date = new Date(time);
        var year = date.getFullYear();
        /* 在日期格式中，月份是从0开始的，因此要加0
         * 使用三元表达式在小于10的前面加0，以达到格式统一  如 09:11:05
         * */
        var month = date.getMonth() + 1 < 10 ? "0" + (date.getMonth() + 1) : date.getMonth() + 1;
        var day = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
        var hours = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
        var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
        var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
        // 拼接
        return year + "-" + month + "-" + day + " " + hours + ":" + minutes + ":" + seconds;
      },
      //  收藏
      collect: function () {
        // 检查用户是否登录，如果登录，检查用户是否已经收藏过，如果收藏过就取消收藏，如果没有就收藏
        // 如果没有登录 就跳转到登录页面，登录成功后返回这里
        if (this.$store.state.token) {
          this.$axios.request({
            url: this.$store.state.apiDict.collect,
            method: "POST",
            data: {"id": this.$route.params.id, "token": this.$store.state.token},
            headers: {
              "Content-Type": "application/json"
            }
          }).then(res => {
            if (res.data.code === 1000) {
              this.initNewsDetail(this.$route.params.id);
              alert("收藏成功");
            } else if (res.data.code === 1001) {
              this.initNewsDetail(this.$route.params.id);
              alert("取消收藏成功");
            }
          }).catch(res => {
            alert(res);
          })
        } else {
          this.$router.push({name: "login", query: {backUrl: this.$route.fullPath}});
        }
      },
      //  点赞
      agree: function () {
        // 检查用户是否登录，如果登录，检查用户是否已经点赞过，如果点赞过就取消点赞，如果没有就点赞
        if (this.$store.state.token) {
          this.$axios.request({
            url: this.$store.state.apiDict.agree,
            method: "POST",
            data: {"id": this.$route.params.id, "token": this.$store.state.token},
            headers: {
              "Content-Type": "application/json"
            }
          }).then(res => {
            if (res.data.code === 1000) {
              this.initNewsDetail(this.$route.params.id);
              alert("点赞成功");
            } else if (res.data.code === 1001) {
              this.initNewsDetail(this.$route.params.id);
              alert("取消点赞成功");
            }
          }).catch(res => {
            alert(res);
          })
        } else {
          this.$router.push({name: "login", query: {backUrl: this.$route.fullPath}});
        }
      },
    //  评论
      commentHandler: function () {
        if(this.$store.state.token){
          if(this.commentContent){
            this.$axios.request({
              url: this.$store.state.apiDict.comment,
              method: "POST",
              data: {
                token: this.$store.state.token,
                id: this.$route.params.id,
                commentContent: this.commentContent
              },
              headers: {
                "Content-Type": "application/json"
              }
            }).then(res=>{
              if(res.data.code===1000){
                alert("评论成功");
              }else{
                alert(res.data.error);
              }
            }).catch(res=>{
              alert(res);
            })
          }else{
            alert("评论不能为空");
          }
        }else{
          this.$router.push({name: "login", query: {backUrl: this.$route.fullPath}});
        }
      }
    },
  }
</script>

<style scoped>

</style>
