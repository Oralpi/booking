<template>
  <div class="create">
    <div class="create-content1">
      <div class="create-content1-substance1">
        성인수: <input>
      </div>
      <div class="create-content1-substance2">
        소아수: <input>
      </div>
      <div class="create-content1-substance3">
        예약자 성: <input>
      </div>
      <div class="create-content1-substance4">
        예약자 이름: <input>
      </div>
      <div class="create-content1-substance5">
        예약자 이메일: <input>
      </div>
      <div class="create-content1-substance6">
        예약자 연락처: <input>
      </div>
      <div class="create-content1-substance7">
        투숙자 성: <input>
      </div>
      <div class="create-content1-substance8">
        투숙자 이름: <input>
      </div>
      <div class="create-content1-substance9">
        투숙자 이메일: <input>
      </div>
      <div class="create-content1-substance10">
        투숙자 연락처: <input>
      </div>
    </div>
    <div class="create-content2">
      <button class="create-content2-substance">뒤로 가기</button>
      <button class="create-content2-substance" type="button" @click="button_event();">예약</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Create',
  methods: {
    button_event() {
      if(confirm("정말 예약하시겠습니까?") === true) {
        document.form.submit();
      } else {
        return;
      }
    }
  }
};
</script>

<style>
@import url('../../css/hotelCreate.css');
</style>