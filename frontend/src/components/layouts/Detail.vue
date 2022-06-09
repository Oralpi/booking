<template>
  <div class="detail">
    <Spinner v-if="spinner" />
    <div class="detail-content1" v-for="(detail, index) in details" :key="index">
      <div class="detail-content1-substance">
        <div class="content1-substance-address">
          주소: {{ detail.address }}
        </div>
        <div class="content1-substance-url">
          홈페이지: {{ detail.url }}
        </div>
        <div class="content1-substance-phone">
          연락처: {{ detail.phone }}
        </div>
        <div class="content1-substance-checkIn">
          체크인: {{ detail.checkIn }}
        </div>
        <div class="content1-substance-checkOut">
          체크아웃: {{ detail.checkOut }}
        </div>
        <div class="content1-substance-information">
          호텔 정보: {{ detail.information }}
        </div>
        <div class="content1-substance-instructions">
          호텔 설명: {{ detail.instructions }}
        </div>
      </div>
    <div class="detail-content2">
      <div class="detail-content2-images" v-for="(image, index) in images" :key="index">
        <img class="content2-images-image" v-bind:src="image" alt="사진" />
      </div>
    </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import Spinner from '../layouts/Spinner.vue'
export default {
  name: 'Detail',
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
      let path = "http://" + window.location.hostname + ":5000/detail";
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
<style>
@import url('../../css/detail.css');
</style>