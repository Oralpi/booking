<template>
  <div class="cancel">
    <table class="cancel-content1" border="1">
      <th>성인수</th>
      <th>소아수</th>
      <th>예약자 성</th>
      <th>예약자 이름</th>
      <th>예약자 이메일</th>
      <th>예약자 연락처</th>
      <th>투숙자 성</th>
      <th>투숙자 이름</th>
      <th>투숙자 이메일</th>
      <th>투숙자 연락처</th>
      <tr>
        <td>가</td>
        <td>나</td>
        <td>다</td>
        <td>라</td>
        <td>마</td>
        <td>바</td>
        <td>사</td>
        <td>아</td>
        <td>자</td>
        <td>차</td>
      </tr>
    </table>
    <div class="cancel-content2">
      <div class="cancel-content2-substance1">
        예약번호: <input>
      </div>
      <div class="cancel-content2-substance2">
        취소사유: <input>
      </div>
    </div>
    <div class="cancel-content3">
      <button class="cancel-content3-substance">뒤로 가기</button>
      <button class="cancel-content3-substance" type="button" @click="button_event();">취소</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cancel',
  methods: {
    button_event() {
      if(confirm("정말 취소하시겠습니까?") === true) {
        document.form.submit();
      } else {
        return;
      }
    }
  }
}
</script>

<style>
@import url('../../css/hotelCancel.css');
</style>