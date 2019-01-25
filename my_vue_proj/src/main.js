// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios"
import store from './store/store'

Vue.prototype.$axios = axios;

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});

// 拦截器
router.beforeEach(function(to, from, next){
  if(to.meta.requiredAuth){
    if(store.state.token){
      next();
    }else{
      next({
        path: "/login",
        query: {backUrl: to.fullPath}
      })
    }
  }else{
    next();
  }
});
