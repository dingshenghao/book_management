<template>
  <div>
    <div class="form-data">
      <div id="header">
        <span id="title">Book-Management</span>
        <a href="/login" id="login">登录 ></a>
      </div>
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="ruleForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="password2">
          <el-input type="password" v-model="ruleForm.password2" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item
            prop="email"
            label="邮箱"
            :rules="[
                      { required: true, message: '请输入邮箱地址', trigger: 'blur' },
                      { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
                    ]"
        >
          <el-input v-model="ruleForm.email"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm">注册</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
    <Footer></Footer>
  </div>

</template>

<script>
import Footer from "@/layout/Footer";
import {Register} from "@/api/requests";

export default {
  name: "register",
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
      } else {
        if (this.ruleForm.password !== '') {
          this.$refs.ruleForm.validateField('password2');
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        password: '',
        password2: '',
        username: '',
        email: ''
      },
      rules: {
        password: [
          {validator: validatePass, trigger: 'blur', required: true}
        ],
        password2: [
          {validator: validatePass2, trigger: 'blur', required: true}
        ],
        username: [
          {validator: checkName, trigger: 'blur', required: true}
        ]
      }
    };
  },
  methods: {
    submitForm() {
      const loading = this.openLoading()
      setTimeout(() => {
        loading.close()
        Register(this.ruleForm).then((res) => {
          if (res.status == 200) {
            this.$message({
              type: 'success',
              message: res.message
            })
            this.$router.push('/login')
          } else (
              this.$message({
                type: 'error',
                'message': res.message
              })
          )
        })
      }, 700)
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  },
  mounted() {
    document.querySelector('body').setAttribute('style', 'background-color:#2d3a4b')
  },
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
