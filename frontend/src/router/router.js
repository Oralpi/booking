import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: '/',
    component: () => import('../components/first/First.vue')
  },
  {
    path: '/firstHotelStory',
    component: () => import('../components/first/FirstHotelStory.vue')
  },
  {
    path: '/firstOnda',
    component: () => import('../components/first/FirstOnda.vue')
  },
  {
    path: '/search',
    component: () => import('../components/search/Search.vue')
  },
  {
    path: '/onda',
    component: () => import('../components/onda/Onda.vue')
  },
  {
    path: '/detail',
    component: () => import('../components/layouts/Detail.vue')
  },
  {
    path: '/ondaDetail',
    component: () => import('../components/onda/OndaDetail.vue')
  },
  {
    path: '/hotelCreate',
    component: () => import('../components/reservation/HotelCreate.vue')
  },
  {
    path: '/hotelCancel',
    component: () => import('../components/reservation/HotelCancel.vue')
  },
  {
    path: '/hotelReference',
    component: () => import('../components/reservation/HotelReference.vue')
  },
  {
    path: '/hotelBatchService',
    component: () => import('../components/batchService/HotelBatchService.vue')
  },
  {
    path: '/ondaBatchService',
    component: () => import('../components/batchService/OndaBatchService.vue')
  },
  {
    path: '/ondaCreate',
    component: () => import('../components/reservation/OndaCreate.vue')
  },
  {
    path: '/ondaCancel',
    component: () => import('../components/reservation/OndaCancel.vue')
  },
  {
    path: '/ondaReference',
    component: () => import('../components/reservation/OndaReference.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;