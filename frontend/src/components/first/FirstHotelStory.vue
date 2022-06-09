<template>
  <div class="search">
    <Spinner v-if="spinner" />
    <router-link to="/" class="back">뒤로 가기</router-link>
    <div class="search-content1">
      <div class="search-content1-search">
        <input id="search-word" class="content1-search-input" type="text" placeholder="어디로 향하시나요?">
        <button class="content1-search-button" @click="search()">검색</button>
      </div>
      <div class="search-content1-result">호텔스토리 검색된 숙소: {{ result }}개</div>
    </div>
    <div class="search-content2" v-for="(detail, io) in details" :key="io">
      <div class="search-content2-images">
        <img class="content2-images-image" :src="detail.image" alt="사진" />
      </div>
      <div class="search-content2-substance1">
        <div @click="detail_params(detail.id)" class="content2-substance1-content1">{{ detail.name }}</div>
        <div class="content2-substance1-content2">{{ detail.addr }}</div>
        <div class="content2-substance1-content3">{{ detail.desc }}</div>
      </div>
      <div class="search-content2-substance2">
        <div class="content2-substance2-mark">{{ detail.rating * 5 }}점</div>
      </div>
    </div>
    <v-pagination v-model="pageNum" :pages="totalPage" :range-size="1" active-color="#DCEDFF" @update:modelValue="movePage" />
  </div>
</template>

<script>
import axios from 'axios'
import Spinner from '../layouts/Spinner.vue'
import VPagination from "@hennge/vue3-pagination";
import "@hennge/vue3-pagination/dist/vue3-pagination.css";
export default {
  name: 'Search',
  components: {
    Spinner,
    VPagination
  },
  data() {
    return {
      details: [],
      result: 0,
      totalPage: 0,
      startIdx: 0,
      endIdx: 0,
      pageNum: 1,
      limit: 10,
      size: 0,
      current: 0,
      spinner: true,
      lens: 0,
      pageList: [],
      pageLength: 0,
      pageCurrent: 0,
      words: '',
      page: 0
    }
  },
  created() {
    this.hotelStory();
    this.searchData(this.pageNum);
  },
  methods: {
    hotelStory() {
      let path = "http://" + window.location.hostname + ":5000/hotel-story";
      let frm = new FormData();

      frm.append("start", "0");
      axios.post(path, frm).then((response) => {        
        this.details = response.data.hotelStory;
        console.log(this.details);
        this.size = this.details.length;
        this.lens = response.data.lens;
        this.current = response.data.currentLength;
        this.pageList = response.data.pageList;
        this.pageLength = response.data.pagelens;
        this.totalPage = Math.ceil(this.lens / 10);
        this.spinner = false;

        for(let i = 0; i < this.lens; i++) {
          this.result = i + 1;
        }
      }).catch((error) => {
        console.log(error);
      });
    },
    search() {
      this.words = document.getElementById("search-word").value;
      this.searchData(this.pageNum);
    },
    searchData(pageNum) {
      let path = "http://" + window.location.hostname + ":5000/hotel-story";
      let frm = new FormData();
      let startIdx = (pageNum - 1) * this.limit;

      frm.append("start", startIdx.toString());
      frm.append("search_word", this.words);
      axios.post(path, frm).then((response) => {
        this.details = response.data.hotelStory;
        this.totalPage = Math.ceil(response.data.length / 10);
        this.result = response.data.length;
        this.spinner = false;
      
      }).catch((error) => {
        console.log(error);
      });
    },
    apiData(word) {
      let path = "http://" + window.location.hostname + ":5000/hotel-story";
      let frm = new FormData();

      frm.append("start", "0");
      frm.append("search_word", word);
      axios.post(path, frm).then((response) => {
        this.details = response.data.hotelStory;
        this.totalPage = Math.ceil(this.details.length / 10);
        this.current = response.data.currentLength;
        this.spinner = false;

        for(let i = 0; i < this.current; i++) {
          this.result = i + 1;
        }
      }).catch((error) => {
        console.log(error);
      });
    },
    detail_params(id) {
      this.$router.push({path: "/detail"});
      this.$session.set("id", id);
    },
    movePage(page) {
      this.pageNum = page;
      this.searchData(this.pageNum)
    }
  }
};
</script>

<style scoped>
@import url('../../css/firstHotelStory.css');
</style>