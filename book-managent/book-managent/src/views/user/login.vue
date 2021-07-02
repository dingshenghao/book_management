<template>
  <div>
    <div class="form-data">
      <div id="header">
        <span id="title">Book-Management</span>
        <a href="/register" id="login">注册 ></a>
      </div>
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model.number="ruleForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm">登录</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from "@/layout/Footer";
import {Login} from "@/api/requests";

export default {
  name: "login",
  components: {
    Footer
  },
  data() {
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('用户名不能为空'));
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      }
    };
    return {
      ruleForm: {
        password: '',
        username: ''
      },
      rules: {
        password: [
          {validator: validatePass, trigger: 'blur', required: true}
        ],
        username: [
          {validator: checkName, trigger: 'blur', required: true}
        ]
      }
    };
  },
  methods: {
    submitForm() {
      const loading = this.openLoading();
      Login(this.ruleForm).then((res) => {
        if (res.status == 200) {
          setTimeout(()=>{
            loading.close()
            this.$message({
              type: 'success',
              message: res.message
            })
            localStorage.setItem('username', res.data.username);
            localStorage.setItem('user', JSON.stringify(res.data))
            this.$router.push('/hots')
          }, 700)
        } else {
          this.$message({
            type: 'error',
            message: res.message
          })
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  },
  mounted() {
    document.querySelector('body').setAttribute('style', 'background-color:#2d3a4b')
  }
  ,
  beforeDestroy() {
    document.querySelector('body').removeAttribute('style')
  }
}
</script>

<style scoped>

.form-data {
  width: 480px;
  margin: 210px auto;
}

#header {
  margin-bottom: 15px;
}

#title {
  font-size: 26px;
  color: #DCDCDC;
  margin-left: 120px;
}

#login {
  color: #BEBEBE;
  font-size: 10px;
  margin-left: 80px;
  margin-top: 2px;
}

a {
  text-decoration: none;
}
</style>
