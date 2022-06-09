<template>
    <div class="flex-div-row header-container">
        <div class="flex-div-row header-box">
            <ul class="menubar menubar-list-box">
                <li class="menu-logo"><img src="../../assets/img/onepick.png" alt="로고"></li>
                <div class="menu-list">
                    <router-link class="menu-items" to="/">숙박 업체 조회</router-link>
                    <router-link class="menu-items" to="/search">객실 정보 조회</router-link>
                    <router-link class="menu-items" to="/search">상품 정보 조회</router-link>
                    <router-link class="menu-items" to="/hotelBatchService">호텔스토리 배치 서비스</router-link>
                    <router-link class="menu-items" to="/ondaBatchService">온다 배치 서비스</router-link>
                    <router-link to="hotelCreate">호텔 예약 생성</router-link>
                    <router-link to="hotelReference">호텔 예약 조회</router-link>
                    <router-link to="hotelCancel">호텔 예약 취소</router-link>
                    <router-link to="ondaCreate">온다 예약 생성</router-link>
                    <router-link to="ondaReference">온다 예약 조회</router-link>
                    <router-link to="ondaCancel">온다 예약 취소</router-link>
                </div>
            </ul>
        </div>
    </div>
</template>
<script>
export default {
    name: "Header",
}
</script>
<style>
@import url('../../css/header.css');
</style>