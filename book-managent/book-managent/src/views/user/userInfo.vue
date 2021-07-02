<template>
  <div id="userInfo">
    <div>
      <el-form :model="ruleForm" status-icon ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="ruleForm.username" :value="ruleForm.username" type="test"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="ruleForm.email" :value="ruleForm.email" type="email"></el-input>
        </el-form-item>
        <el-form-item label="个人简介">
          <el-input
              type="textarea"
              :rows="2"
              placeholder="请输入内容"
              :value="ruleForm.desc"
              v-model="ruleForm.desc">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm">修改</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div>
      <span id="userIcon">上传头像</span>
      <el-upload
          id="icon"
          class="avatar-uploader"
          action="#"
          :http-request="uploadIcon"
          :show-file-list="true"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload">
        <img v-if="imageUrl" :src="imageUrl" class="avatar">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
    </div>
  </div>
</template>

<script>
import {EditUser, UploadIcon} from "@/api/requests";

export default {
  name: "userInfo",
  data() {
    return {
      ruleForm: {
        email: '',
        username: '',
        desc: '',
      },
      imageUrl: ''
    };
  },
  mounted() {
    let user = JSON.parse(localStorage.getItem('user'))
    this.ruleForm.email = user.email;
    this.ruleForm.username = user.username
    this.ruleForm.desc = user.desc
  },
  methods: {
    submitForm() {
      var user = JSON.parse(localStorage.getItem('user'))
      EditUser(this.ruleForm, user.id).then((res) => {
        if (res.status == 200) {
          const loading = this.openLoading()
          setTimeout(()=>{
            loading.close()
            user.username = this.ruleForm.username;
            user.email = this.ruleForm.email;
            user.desc = this.ruleForm.desc;
            localStorage.setItem('user', JSON.stringify(user))
            this.$router.go(0)
            this.$notify({
              type: 'success',
              message: res.message
            })
          }, 500)
        } else {
          this.$notify({
            type: 'error',
            message: res.message
          })
        }
      })
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
      this.$notify({
        type: 'success',
        message: '头像上传成功'
      })
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    },
    uploadIcon(params) {
      const formData = new FormData();
      formData.append('img', params.file)
      let id = JSON.parse(localStorage.getItem('user')).id
      UploadIcon(id, formData).then((res) => {
        const loading = this.openLoading();
        if (res.status == 200) {
          this.$message({
            type: 'success',
            message: res.message
          })
          var user = JSON.parse(localStorage.getItem('user'));
          user.img = res.data;
          localStorage.setItem("user", JSON.stringify(user));
          setTimeout(() => {
            loading.close();
            this.$router.go(0)
          }, 1000);
        } else {
          this.$message({
            type: 'error',
            message: res.message
          })
        }
      })
    }

  }
}
</script>

<style scoped>
#userInfo {
  width: 500px;
  margin-left: 300px;
  margin-top: 100px;
}

#userIcon {
  float: right;
  margin-right: -100px;
  margin-top: -260px;
}

#icon {
  width: 180px;
  border: 1px dashed #DCDCDC;
  float: right;
  margin-right: -300px;
  margin-top: -260px;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}

.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
