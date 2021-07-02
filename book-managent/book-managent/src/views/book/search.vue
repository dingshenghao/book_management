<template>
  <div style="margin-left: 200px;">
    <div style="height: 50px">
      <div style="float: left;">
        <span style="width: 100px">书名：</span>
        <el-input style="width: 280px" v-model="data.name" placeholder="请输入内容"></el-input>
      </div>
      <div style="float: left;margin-left: 10px">
        <span>责任者：</span>
        <el-input style="width: 280px" v-model="data.principal" placeholder="请输入内容"></el-input>
      </div>
      <div style="float: left;margin-left: 10px">
        <span>出版社：</span>
        <el-input style="width: 280px" v-model="data.product" placeholder="请输入内容"></el-input>
      </div>
      <div style=" float: left;margin-left: 20px">
        <el-button @click="searchBook" type="primary" icon="el-icon-search">搜索</el-button>
      </div>
    </div>
    <div style="margin-left: -20px">
      <el-row :gutter="8">
        <el-col :span="8" v-for="(item,index) in books" :key="index">
          <div class="grid-content bg-purple">
            <el-card :body-style="{ padding: '0px' }">
              <img :src="item.img"
                   class="image">
              <div style="padding: 10px;">
                <div>
                  <span class="context">图书题目: {{ item.name }}</span>
                </div>
                <div>
                  <span class="context">负责人: {{ item.principal }}</span>
                </div>
                <div>
                  <span class="context">入馆时间: {{ item.create_time }}</span>
                </div>
              </div>
            </el-card>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import {GetBooks, SearchBook} from "@/api/requests";

export default {
  name: "search",
  data() {
    return {
      data: {
        name: '',
        principal: '',
        product: '',
      },
      books: []
    }
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
      GetBooks().then((res) => {
        this.books = res.data
      })
    },
    searchBook() {
      const loading = this.openLoading()
      setTimeout(() => {
        loading.close()
        SearchBook(this.data).then((res) => {
          if (res.status == 200) {
            this.$notify({
              type: 'success',
              message: res.message
            })
            this.books = res.data
          } else {
            this.$notify({
              type: 'error',
              message: res.message
            })
          }
        })
      }, 500)
    }
  }
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
