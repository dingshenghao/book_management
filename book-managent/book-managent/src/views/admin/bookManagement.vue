<template>
  <div id="container">
    <el-row :gutter="8">
      <el-col :span="8" v-for="(item, index) in books" :key="index">
        <div class="grid-content bg-purple">
          <el-card :body-style="{ padding: '0px' }">
            <img :src="item.img"
                 class="image">
            <div style="padding: 10px;">
              <div>
                <span class="context">图书题目: {{ item.name }}</span>
              </div>
              <div>
                <span class="context1">负责人: {{ item.principal }}</span>
              </div>
              <div>
                <span class="context2">入馆时间: {{ item.create_time }}</span>
              </div>
            </div>
            <div class="button-box">
              <el-button class="box" type="primary" icon="el-icon-edit" @click="editBook(index)" circle></el-button>
              <el-button class="box" type="danger" icon="el-icon-delete" @click="deleteBook(index)" circle></el-button>
            </div>
          </el-card>
        </div>
      </el-col>
    </el-row>
    <div>
      <el-dialog title="图书修改" :visible.sync="dialogFormEditBook">
        <el-form :model="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="图书名称" prop="name">
            <el-input v-model="ruleForm.name" :value="ruleForm.name"></el-input>
          </el-form-item>
          <el-form-item label="图书类别" prop="category_id">
            <el-select v-model="ruleForm.category_id" placeholder="请选择图书类别">
              <el-option v-for="(item,index) in categories" :key="index" :label="item.name"
                         :value="item.id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="出版社" prop="product">
            <el-input v-model="ruleForm.product" :value="ruleForm.product"></el-input>
          </el-form-item>
          <el-form-item label="负责人" prop="principal">
            <el-input v-model="ruleForm.principal" :value="ruleForm.principal"></el-input>
          </el-form-item>
          <el-form-item label="图书索引" prop="book_index">
            <el-input type="test" v-model="ruleForm.book_index" :value="ruleForm.book_index"></el-input>
          </el-form-item>
          <el-form-item label="ISBN" prop="ISBN">
            <el-input type="test" v-model="ruleForm.ISBN" :value="ruleForm.ISBN"></el-input>
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
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormEditBook = false">取 消</el-button>
          <el-button type="primary" @click="commit">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import {DeleteBook, EditBook, GetBooks, GetCategory} from "@/api/requests";

export default {
  name: "bookManagement",
  data() {
    return {
      books: [],
      categories: [],
      dialogFormEditBook: false,
      ruleForm: {
        name: '',
        category_id: '',
        product: '',
        principal: '',
        book_index: '',
        ISBN: '',
        img: ''
      },
      fileList: [],
      index: ''
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
      GetBooks().then((res) => {
        this.books = res.data
      })
    },
    editBook(index) {
      this.index = index;
      this.dialogFormEditBook = true
      this.ruleForm.name = this.books[index].name
      this.ruleForm.category_id = this.books[index].category_id
      this.ruleForm.product = this.books[index].product
      this.ruleForm.principal = this.books[index].principal
      this.ruleForm.book_index = this.books[index].book_index
      this.ruleForm.ISBN = this.books[index].ISBN
      this.ruleForm.img = this.books[index].img
    },
    deleteBook(index) {
      this.index = index;
      this.$confirm('此操作将永久删除该图书, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(111111111111)
        DeleteBook(this.books[this.index].id).then((res) => {
          if (res.status == 204) {
            this.$message({
              type: 'success',
              message: res.message
            })
            this.books.splice(index, 1);
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
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
    commit() {
      let formData = new FormData();
      for (const key in this.ruleForm) {
        formData.append(key, this.ruleForm[key]);
      }
      if (this.fileList.length != 0) {
        this.fileList.map(item => {
          formData.append("file", (item.raw));
        });
      } else {
        formData.append("file", 'None');
      }
      EditBook(this.books[this.index].id, formData).then((res) => {
        if (res.status == 200) {
          this.dialogFormEditBook = false
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
  },
}
</script>

<style scoped>
.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.grid-content {
  width: 260px;
  margin-left: 60px;
  margin-bottom: 20px;
  margin-top: 30px;
}

#container {
  margin-left: 180px;
}

.el-col-8 {
  width: 32.333%;
}

.el-card {
  width: 340px;
  padding: 0;
}

.image {
  width: 100%;
}

.button-box {
  display: flex;
  width: 86px;
  flex-wrap: wrap;
  float: right;
  margin-right: -40px;
  margin-top: -80px;
}

.box {
  width: 50%;
}

.el-button + .el-button {
  margin-top: 5px;
  margin-left: 1px;
}

.el-select {
  width: 571px;
  height: 40px;
}
</style>
