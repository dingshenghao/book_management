<template>
  <div style="margin-left: 220px; width: 80%; margin-top: 50px">
    <el-table
        v-if="books.length > 0"
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
          prop="username"
          align="center"
          label="用户名"
          width="180">
      </el-table-column>
      <el-table-column
          prop="email"
          align="center"
          label="邮箱">
      </el-table-column>
      <el-table-column
          prop="name"
          align="center"
          label="书名">
      </el-table-column>
      <el-table-column
          prop="status"
          align="center"
          label="状态">
        <template slot-scope="scope">
          <el-button @click="agreeBorrow(scope.$index)"  type="info" plain>同意预约</el-button>
        </template>
      </el-table-column>
    </el-table>
    <h3 v-else>暂时没有用户申请预约图书</h3>
  </div>
</template>

<script>
import {AgreeReservation, ReservationList} from "@/api/requests";

export default {
  name: "edit",
  data() {
    return {
      books: [],
      data: {
        borrow_id: ''
      }
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
    load(){
      ReservationList().then((res)=>{
        this.books = res.data
      })
    },
    agreeBorrow(index){
      this.data.borrow_id = this.books[index].id
      AgreeReservation(this.data).then((res)=>{
        if (res.status == 200){
          this.$notify({
            type: 'success',
            message: res.message
          })
          this.books.splice(index, 1);
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
