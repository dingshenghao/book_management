<template>
  <div style="margin-left:260px; margin-top: 50px; width: 400px">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm" >
      <el-form-item label="图书名称" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>
      <el-form-item label="图书类别" prop="category_id">
        <el-select v-model="ruleForm.category_id" placeholder="请选择图书类别">
          <el-option v-for="(item,index) in categories" :key="index" :label="item.name" :value="item.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="出版社" prop="product">
        <el-input v-model="ruleForm.product"></el-input>
      </el-form-item>
      <el-form-item label="负责人" prop="principal">
        <el-input v-model="ruleForm.principal"></el-input>
      </el-form-item>
      <el-form-item label="图书索引" prop="book_index">
        <el-input type="text" v-model="ruleForm.book_index"></el-input>
      </el-form-item>
      <el-form-item label="ISBN" prop="ISBN">
        <el-input type="text" v-model="ruleForm.ISBN"></el-input>
      </el-form-item>
      <el-form-item label="图书封面" prop="img">
        <el-upload
            class="upload-demo"
            drag
            action="#"
            :file-list="fileList"
            :on-change="handleAddChange"
            :auto-upload="false"
            multiple>
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">立即发布</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {AddBook, GetCategory} from "@/api/requests";

export default {
  name: "addBook",
  data() {
    return {
      categories: [],
      ruleForm: {
        name: '',
        category_id: '',
        product: '',
        principal: '',
        book_index: '',
        ISBN: '',
      },
      rules: {
        name: [
          {required: true, message: '请输入活动名称', trigger: 'blur'},
        ],
        category_id: [
          {required: true, message: '请选择图书分类', trigger: 'change'}
        ],
        product: [
          {required: true, message: '请输入出版社', trigger: 'blur'}
        ],
        principal: [
          {required: true, message: '请输入负责人', trigger: 'blur'}
        ],
        book_index: [
          {required: true, message: '请输入图书索引', trigger: 'blur'}
        ],
        ISBN: [
          {required: true, message: '请输入图书ISBN号', trigger: 'blur'}
        ],
        img: [
          {required: true, message: '请选择图书封面', trigger: 'blur'}
        ]
      },
      fileList : [],
    };
  },
  mounted() {
    const loading = this.openLoading()
    setTimeout(() => {
      loading.close()
      this.load()
    }, 500)
  },
  methods: {
    load() {
      GetCategory().then((res) => {
        this.categories = res.data
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    // 上传change事件
    handleAddChange(file, fileList) {
      // 图片大小限制
      const isLt20M = file.size / 1024 / 1024 < 20;
      if (!isLt20M) {
        this.$message.error("上传图片大小不能超过 20MB!");
        fileList.splice(-1, 1);
      } else {
        this.fileList = fileList;

      }
    },
    submitForm() {
      let formData = new FormData();
      for (const key in this.ruleForm) {
        formData.append(key, this.ruleForm[key]);
      }
      this.fileList.map(item => {
        formData.append("file", (item.raw));
      });
      AddBook(formData).then((res) => {
        console.log(res)
        if (res.status == 200){
          this.$message({
            type: 'success',
            message: res.message
          })
          this.$router.go(0);
        } else {
          this.$message({
            type: 'error',
            message: res.message
          })
        }
      })
    },
  }
}

</script>

<style scoped>
.el-select {
  width: 300px;
  height: 40px;
}
</style>
