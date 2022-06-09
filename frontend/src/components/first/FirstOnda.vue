<template>
  <div class="onda">
    <Spinner v-if="spinner" />
    <router-link to="/" class="back">뒤로 가기</router-link>
    <div class="onda-content1">
      <div class="onda-content1-search">
        <input id="search-word" class="content1-search-input" type="text" placeholder="어디로 향하시나요?">
        <button class="content1-search-button" @click="search()">검색</button>
      </div>
      <div class="onda-content1-result">온다 검색된 숙소: {{ result }}개</div>
    </div>
    <div class="onda-content2" v-for="(detail, index) in details" :key="index">
      <div class="onda-content2-images">
        <img class="content2-images-image" :src="detail.image" alt="사진">
      </div>
      <div class="onda-content2-substance1">
        <div class="content2-substance1-content1" @click="detail_params(detail.id)">{{ detail.name }}</div>
        <div class="content2-substance1-content2">{{ detail.address }}</div>
      </div>
      <div class="onda-content2-substance2">
        <div class="content2-substance2-mark">{{ Math.ceil(detail.rating / 10) }}점</div>
      </div>
    </div>
    <v-pagination v-model="pageNum" :pages="totalPage" :range-size="1" active-color="#DCEDFF" @update:modelValue="movePage" />
  </div>
</template>

<script>
import axios from 'axios'
import VPagination from "@hennge/vue3-pagination";
import "@hennge/vue3-pagination/dist/vue3-pagination.css";
import Spinner from '../layouts/Spinner.vue'
export default {
  name: 'Onda',
  components: {
    Spinner,
    VPagination
  },
  data() {
    return {
      details: [],
      size: 0,
      lens: 0,
      current: 0,
      spinner: true,
      result: 0,
      totalPage: 0,
      startIdx: 0,
      endIdx: 0,
      limit: 10,
      pageNum: 1,
      pageList: [],
      pageLength: 0,
      words: '',
      page: 0
    }
  },
  created() {
    this.onda();
    this.searchData(this.pageNum);
  },
  methods: {
    onda() {
      let path = "http://" + window.location.hostname + ":5000/onda";
      let frm = new FormData();

      frm.append("start", "0");
      axios.post(path, frm).then((response) => {
        this.details = response.data.hotelStory;
        // this.size = this.details.length;
        this.lens = response.data.lens;
        this.current = response.data.currentLength;
        this.pageList = response.data.pageList;
        this.pageLength = response.data.pagelens;
        this.spinner = false;
        this.totalPage = Math.ceil(response.data.lengths / 10);
        
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
      let path = "http://" + window.location.hostname + ":5000/onda";
      let frm = new FormData();
      let startIdx = (pageNum - 1) * this.limit;
      console.log(startIdx)

      frm.append("start", startIdx.toString());
      frm.append("search_word", this.words);
      axios.post(path, frm).then((response) => {
        this.details = response.data.onda;
        console.log(this.details)
        this.totalPage = Math.ceil(response.data.lengths / 10);
        this.result = response.data.lengths;
        this.spinner = false;

      }).catch((error) => {
        console.log(error);
      });
    },
    apiData(word) {
      console.log("?")
      let path = "http://" + window.location.hostname + ":5000/onda";
      let frm = new FormData();

      frm.append("start", "0");
      frm.append("search_word", word);
      axios.post(path, frm).then((response) => {
        this.details = response.data.onda;
        this.totalPage = Math.ceil(response.data.lengths / 10);
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
      this.$router.push({path: "/ondaDetail"});
      this.$session.set("id", id);
    },
    movePage(page) {
      this.pageNum = page;
      console.log(this.pageNum)
      this.searchData(this.pageNum)
    }
  }
};
</script>

<style scoped>
@import url('../../css/firstOnda.css');
</style>