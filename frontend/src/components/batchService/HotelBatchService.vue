<template>
  <div class="hotelBatchService">
    <div class="hotelBatchService-content1">
      <div class="hotelBatchService-content1-substance1">
        <router-link class="content1-substance1-content" to="/">뒤로 가기</router-link>
      </div>
      <div class="hotelBatchService-content1-substance2">
        <button class="content1-substance2-content" type="button" @click="call_in();">전체 불러오기</button>
        <button class="content1-substance2-content" type="button" @click="renewal();">갱신</button>
        <button class="content1-substance2-content" type="button" @click="delete_all();">전체 삭제</button>
      </div>
    </div>
    <div class="hotelBatchService-content2">
      <div class="hotelBatchService-content2-substance">{{ logs }}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HotelBatchService',
  data() {
    return {
      logs: ""
    }
  },
  methods: {
    call_in() {
      if(confirm('정말 전체를 불러오시겠습니까?') === true) {
        this.set_HotelStoryRoomInformation();
        return;
      } else {
        alert('전체 불러오기를 실패하였습니다.');
      }
    },
    renewal() {
      if(confirm('정말 갱신하시겠습니까?') === true) {
        return;
      } else {
        alert('갱신을 실패하였습니다.');
      }
    },
    delete_all() {
      if(confirm('정말 전체 삭제하시겠습니까?') === true) {
        this.delete_HotelStoryRoomInformation();
      } else {
        alert('전체 삭제를 실패하였습니다.');
      }
    },
    set_HotelStoryRoomInformation() {
      let path = "http://" + window.location.hostname + ":5000/set_HotelStoryRoomInfomation";

      axios.post(path).then((response) => {
        this.logs = response.data;
        console.log(this.logs);
      }).catch((error) => {
        console.log(error);
      });
    },
    delete_HotelStoryRoomInformation() {
      let path = "http://" + window.location.hostname + ":5000/delete_HotelStoryRoomInformation";

      axios.post(path).then((response) => {
        this.logs = response.data;
        console.log(this.logs);
      }).catch((error) => {
        console.log(error);
      });
    }
  }
};
</script>

<style>
@import url('../../css/hotelBatchService.css');
</style>