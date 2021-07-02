<template>

  <div id="container">
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

</template>

<script>
import {GetBooks} from "@/api/requests";

export default {
  name: "hosts",
  data() {
    return {
      books: []
    }
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      const loading = this.openLoading()
      setTimeout(()=>{
        loading.close()
        GetBooks().then((res) => {

          this.books = res.data
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
