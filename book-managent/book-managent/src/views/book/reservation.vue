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
          label="操作">
        <template slot-scope="scope">
          <el-button v-if="scope.row.book_status == 0" type="primary" plain
                     @click="reservationBorrowBook(scope.$index)">预约借书
          </el-button>
          <el-button v-else type="warning" plain @click="unReservationBorrowBook(scope.$index)">取消预约</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import {GetBorrow, GetReservation, UnReservation} from "@/api/requests";

export default {
  name: "reservation",
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
      GetBorrow(JSON.parse(localStorage.getItem('user')).id).then((res) => {
        this.books = res.data
      })
    },
    reservationBorrowBook(index) {
      this.data.book_id = this.books[index].id
      GetReservation(this.data).then((res)=>{
        if (res.status == 200) {
          this.$notify({
            type: 'success',
            message: '预约成功'
          })
        }
        this.books[index].book_status = 1
      })
    },
    unReservationBorrowBook(index) {
      this.data.book_id = this.books[index].id
      UnReservation(this.books[index].id, this.data).then((res)=>{
        if (res.status == 204) {
          this.$notify({
            type: 'success',
            message: res.message
          })
          this.books[index].book_status = 0
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
