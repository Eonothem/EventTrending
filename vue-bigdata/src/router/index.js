import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Welcome from '@/views/Welcome'
import testChart from '@/views/test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/test',
      name: 'test',
      component: testChart
    }
  ]
})
