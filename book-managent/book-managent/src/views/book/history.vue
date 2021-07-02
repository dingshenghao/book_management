<template>
  <div style="margin-left: 220px; width: 80%; margin-top: 50px">
    <el-table
        border
        :data="books"
        stripe
        style="width: 100%">
      <el-table-column
          prop="create_time"
          label="日期"
          align="center"
          width="180">
      </el-table-column>
      <el-table-column
          prop="name"
          align="center"
          label="书名"
          width="180">
      </el-table-column>
      <el-table-column
          prop="principal"
          align="center"
          label="负责人">
      </el-table-column>
      <el-table-column
          prop="category"
          align="center"
          label="图书分类">
      </el-table-column>
      <el-table-column
          prop="status"
          align="center"
          label="状态">
        <template slot-scope="scope">
          <el-button v-if="scope.row.book_status == 1" type="success" plain>已还书</el-button>
          <el-button v-else-if="scope.row.book_status == 0" @click="borrowBook(scope.$index)" type="warning" plain>待还书
          </el-button>
          <el-button v-else-if="scope.row.book_status == 2" type="info" plain>预约中</el-button>
        </template>

      </el-table-column>
    </el-table>
  </div>

</template>

<script>
import {BackBook, GetHistory} from "@/api/requests";

export default {
  name: "history",
  data() {
    return {
      books: [],
      data: {
        user_id: '',
        book_id: ''
      }
    }
  },
  mounted() {
    const loading = this.openLoading()
    setTimeout(() => {
      loading.close()
      this.load()
    }, 500)
    this.data.user_id = JSON.parse(localStorage.getItem('user')).id
  },
  methods: {
    load() {
      GetHistory(JSON.parse(localStorage.getItem('user')).id).then((res) => {
        this.books = res.data;
      })
    },
    borrowBook(index) {
      console.log(index)
      this.data.book_id = this.books[index].id

      BackBook(this.data).then((res) => {
        console.log(res)
        if (res.status == 200) {
          this.$notify({
            type: 'success',
            message: res.message
          })
          this.books[index].book_status = 1;
        } else {
          this.$notify({
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

</style>
