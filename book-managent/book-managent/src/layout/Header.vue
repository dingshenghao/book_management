<template>
  <el-container>
    <el-container>
      <el-header>
        <div id="context">
          <span id="text">图书管理系统</span>
          <el-dropdown @command="handleCommand" class="userIcon" v-if="username">
            <el-avatar :src="img"></el-avatar>
            <el-dropdown-menu slot="dropdown" id="dropdown">
              <el-dropdown-item command="/userinfo">个人中心</el-dropdown-item>
              <el-dropdown-item command="/login">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span @click="toLogin" class="userIcon"
                style="font-size: 14px;color: #8c939d;font-weight: 200;margin-top: 20px" v-else>登录</span>
        </div>
      </el-header>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      username: '',
      img: ''
    }
  }, mounted() {
    this.load();
  },
  methods: {
    load() {
      this.username = localStorage.getItem('username')
      let img = JSON.parse(localStorage.getItem('user')).img;
      if (img === ''){
        this.img = 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      } else {
        this.img = img
      }
    },
    handleCommand(command) {
      if (command === '/login') {
        this.$confirm('是否要退出登录？', '退出登录', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '退出登录成功'
          })
          localStorage.clear()
          this.$router.push(command);
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消退出登录'
          })
        })
      } else {
        this.$router.push(command);
      }
    },
    toLogin() {
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>

.el-header {
  color: #333;
  text-align: center;
  background-color: #F5F5F5;
  font-size: 28px;
  font-weight: 700;

  z-index: 100;
  width: 100%;
}

.userIcon {
  margin-top: 10px;
  float: right;
  cursor: pointer;
  color: #409EFF;
  margin-right: 10px;
}

.el-dropdown-menu {
  position: relative;
  margin-right: -20px;
}

#text {
  position: absolute;
  margin-top: 10px;
}

.el-popover {
  background: rebeccapurple !important;
}
</style>
