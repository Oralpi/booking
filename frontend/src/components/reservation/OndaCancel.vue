<template>
  <div class="cancel">
    <table class="cancel-content1" border="1">
      <th>입실날짜</th>
      <th>퇴실날짜</th>
      <th>입실자 이름</th>
      <th>성인 수</th>
      <th>아동, 유아 나이</th>
      <th>예약자 이름</th>
      <th>예약자 이메일</th>
      <th>예약자 전화번호</th>
      <tr>
        <td>가</td>
        <td>나</td>
        <td>다</td>
        <td>라</td>
        <td>마</td>
        <td>바</td>
        <td>사</td>
        <td>아</td>
      </tr>
    </table>
    <div class="cancel-content2">
      <div class="cancel-content2-substance1">
        취소 사유: <input>
      </div>
      <div class="cancel-content2-substance2">
        총 결제 금액: <input>
      </div>
      <div class="cancel-content2-substance3">
        환불 금액: <input>
      </div>
    </div>
    <div class="cancel-content3">
      <button class="cancel-content3-substance">뒤로 가기</button>
      <button class="cancel-content3-substance" type="button" @click="cancel();">취소</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cancel',
  methods: {
    cancel() {
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
@import url('../../css/ondaCancel.css');
</style>