import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Course from '@/components/Course'
import News from '@/components/News'
import CourseDetail from '@/components/CourseDetail'
import NewsDetail from '@/components/NewsDetail'
import Login from '@/components/Login'

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/news',
      name: 'news',
      component: News,
      meta: {
        requiredAuth: true
      }
    },
    {
      path: '/courseDetail/:id',
      name: 'courseDetail',
      component: CourseDetail
    },
    {
      path: '/newsDetail/:id',
      name: 'newsDetail',
      component: NewsDetail,
      meta: {
        requiredAuth: true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
  ]
})
