import Vue from 'vue'
import Vuex from "vuex"
import Cookie from "vue-cookies"

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: Cookie.get("username"),
    token: Cookie.get("token"),
    apiDict: {
      course: "http://127.0.0.1:8000/api/v1/course/",
      news: "http://127.0.0.1:8000/api/v1/news/",
      login: "http://127.0.0.1:8000/api/v1/login/",
      collect: "http://127.0.0.1:8000/api/v1/collect/",
      agree: "http://127.0.0.1:8000/api/v1/agree/",
      comment: "http://127.0.0.1:8000/api/v1/comment/",
    }
  },
  mutations: {
    saveToken (state, userToken) {
      state.username = userToken.username;
      state.token = userToken.token;

      Cookie.set("username", userToken.username, "20min");
      Cookie.set("token", userToken.token, "20min")
    },
    clearToken(state){
      state.username = null;
      state.token = null;
      Cookie.remove("username");
      Cookie.remove("token");
    }
  }
});
