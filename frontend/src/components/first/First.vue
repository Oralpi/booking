<template>
    <div class="first">
        <div class="first-page">
            <router-link class="ota-list" to="/firstHotelStory">호텔스토리</router-link>
            <router-link class="ota-list" to="/firstOnda">온다</router-link>
        </div>
        <div class="none-select">
            --아무것도 선택하지 않았습니다--
        </div>
    </div>
</template>

<script>
export default {
    name: 'First',
}
</script>

<style scoped>
@import url('../../css/first.css');
</style>