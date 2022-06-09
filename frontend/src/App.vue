<template>
  <div class="app">
    <Header />
        <router-view></router-view>
    <Footer />
  </div>
</template>

<script>
import Header from './components/layouts/Header.vue'
import Footer from './components/layouts/Footer.vue'
export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
};
</script>

<style>
</style>