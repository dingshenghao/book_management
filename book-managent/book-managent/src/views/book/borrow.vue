<template>
  <div style="margin-left: 220px; width: 80%; margin-top: 50px">
    <el-table
        border
        :data="books"
        stripe
        style="width: 100%">
      <el-table-column
          prop="name"
          align="center"
          label="书名"
          width="180">
      </el-table-column>
      <el-table-column
          prop="img"
          align="center"
          label="图书封面"
          width="180">
        <template slot-scope="scope">
          <el-popover
              placement="right"
              width="200"
              trigger="click">
            <img :src="scope.row.img" alt="">
            <i :index="scope.row.img" slot="reference" class="el-icon-view" style="color: #00B2EE; font-size: 20px"></i>
          </el-popover>
        </template>
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
          prop="product"
          align="center"
          label="出版社">
      </el-table-column>
      <el-table-column
          prop="ISBN"
          align="center"
          label="图书ISBN号">
      </el-table-column>
      <el-table-column
          align="center"
          label="操作"
      >
        <template slot-scope="scope">
          <el-button type="primary" @click="borrowBook(scope.$index)" plain>借书</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {BorrowBook, GetBorrow} from "@/api/requests";

export default {
  name: "borrow",
  data() {
    return {
      books: [],
      categories: [],
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
      GetBorrow(JSON.parse(localStorage.getItem('user')).id).then((res) => {
        this.books = res.data
      })
    },
    borrowBook(index) {
      this.data.book_id = this.books[index].id;
      BorrowBook(this.data).then((res) => {
        console.log(res)
        if (res.status == 200) {
          this.$notify({
            type: "success",
            message: res.message
          })
          this.books.splice(index, 1);
        } else {
          this.$notify({
            type: "error",
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
