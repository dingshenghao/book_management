<template>
  <div class="container">
    <Header/>
    <Left/>
    <Content>
      <router-view/>
    </Content>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "@/layout/Header";
import Footer from "@/layout/Footer";
import Left from "@/layout/Left";
import Content from "@/layout/Content";
export default {
  name: "index",
  data(){
    return{
      username: ''
    }
  },
  components:{
    Header,
    Footer,
    Left,
    Content
  },
  mounted() {
    this.load()
  },
  methods: {
    load(){
      this.username = localStorage.getItem('username');
      if (!this.username){
        this.$message({
          type: 'error',
          message: '你还没有登录！请前去登录'
        })
      }
    }
  }
}
</script>

<style scoped>
.container{
  height: 100%;
}

</style>
