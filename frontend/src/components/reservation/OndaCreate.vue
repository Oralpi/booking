<template>
  <div class="create">
    <div class="create-content1">
      <div class="create-content1-substance1">
        입실날짜: <input>
      </div>
      <div class="create-content1-substance2">
        퇴실날짜: <input>
      </div>
      <div class="create-content1-substance3">
        입실자 이름: <input>
      </div>
      <div class="create-content1-substance4">
        성인 수: <input>
      </div>
      <div class="create-content1-substance5">
        아동, 유아 나이: <input>
      </div>
      <div class="create-content1-substance6">
        예약자 이름: <input>
      </div>
      <div class="create-content1-substance7">
        예약자 이메일: <input>
      </div>
      <div class="create-content1-substance8">
        예약자 전화번호: <input>
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
@import url('../../css/ondaCreate.css');
</style>