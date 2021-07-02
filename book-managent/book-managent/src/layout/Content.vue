<template>
  <el-container>
    <el-container>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>


export default {
  name: "Content",

}
</script>

<style scoped>
.el-main {
  text-align: left;
}
</style>
