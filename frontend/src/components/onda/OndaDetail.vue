<template>
  <div class="ondaDetail">
    <Spinner v-if="spinner" />
    <div class="ondaDetail-content1" v-for="(detail, index) in details" :key="index">
      <div class="ondaDetail-content1-substance">
        <div class="content1-substance-email">이메일: {{ detail.email }}</div>
        <div class="content1-substance-phone">연락처: {{ detail.phone }}</div>
        <div class="content1-substance-website">홈페이지: {{ detail.website }}</div>
        <div class="content1-substance-checkin">체크인: {{ detail.checkin }}</div>
        <div class="content1-substance-checkout">체크아웃: {{ detail.checkout }}</div>
        <div class="content1-substance-property">설명: {{ detail.property }}</div>
        <div class="content1-substance-reservation">예약: {{ detail.reservation }}</div>
      </div>
    </div>
    <div class="ondaDetail-content2">
      <div class="ondaDetail-content2-images" v-for="(image, index) in images" :key="index">
        <img class="content2-images-image" v-bind:src="image[0]" alt="사진" />
      </div>
    </div>
  </div>
</template>

<script>
import Spinner from '../layouts/Spinner.vue'
import axios from 'axios'
export default {
  name: 'OndaDetail',
  components: {
    Spinner
  },
  data() {
    return {
      details: [],
      images: [],
      spinner: false
    }
  },
  methods: {
    detail() {
      this.spinner = true;
      let path = "http://" + window.location.hostname + ":5000/onda-detail";
      let frm = new FormData();

      frm.append("id", this.$session.get("id"));
      axios.post(path, frm).then((response) => {
        this.spinner = false;
        this.details = response.data.detail;
        this.images = response.data.image;
      }).catch((error) => {
        console.log(error);
      });
    }
  },
  created() {
    this.detail();
  }
};
</script>

<style scoped>
@import url('../../css/ondaDetail.css');
</style>