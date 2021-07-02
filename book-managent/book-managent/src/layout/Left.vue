<template>
  <el-container>
    <el-aside width="200px">
      <el-row class="tac">
        <el-col :span="24" v-if="role == 0">
          <el-menu
              :default-active='$route.path'
              class="el-menu-vertical-demo"
              background-color="#2d3a4b"
              :default-openeds="open_list"
              text-color="#ffffff"
              :unique-opened=true
              @open="handleOpen"
              v-for="(menu,index) in menus1" :key="index"
          router>
            <el-submenu :index="index.toString()">
              <template slot="title">
                <span>{{ menu.title }}</span>
              </template>
              <el-menu-item-group v-for="(item, index1) in menu.items" :key="index1">
                  <template slot="title">
                    <el-menu-item style="color: #BEBEBE"  :index="menus[index].path[index1]">{{item}}</el-menu-item>
                  </template>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-col>
        <el-col :span="24" v-if="role == 1">
          <el-menu
              :default-active='$route.path'
              class="el-menu-vertical-demo"
              background-color="#2d3a4b"
              :default-openeds="open_list"
              text-color="#ffffff"
              :unique-opened=true
              @open="handleOpen"
              v-for="(menu,index) in menus" :key="index"
              router>
            <el-submenu :index="index.toString()">
              <template slot="title">
                <span>{{ menu.title }}</span>
              </template>
              <el-menu-item-group v-for="(item, index1) in menu.items" :key="index1">
                <template slot="title">
                  <el-menu-item style="color: #BEBEBE"  :index="menus[index].path[index1]">{{item}}</el-menu-item>
                </template>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-col>
      </el-row>

    </el-aside>
  </el-container>
</template>

<script>
export default {
  name: "Left",
  data() {
    return {
      open_list: [],
      role: '',
      menus1: [
        {title: '书目检索', items: ['图书搜索'], path: ['/search']},
        {title: '热门推荐', items: ['图书推荐'], path: ['/hots']},
        {title: '新书通报', items: ['新书通报'], path: ['/newBook']},
        {title: '我的图书', items: ['借阅历史', '借书', '还书', '预约借书'], path: ['/history', '/borrow', '/back', '/reservation']},
      ],
      menus: [
        {title: '书目检索', items: ['图书搜索'], path: ['/search']},
        {title: '热门推荐', items: ['图书推荐'], path: ['/hots']},
        {title: '新书通报', items: ['新书通报'], path: ['/newBook']},
        {title: '我的图书', items: ['借阅历史', '借书', '还书', '预约借书'], path: ['/history', '/borrow', '/back', '/reservation']},
        {title: '读者管理', items: ['查看读者'], path: ['/readers']},
        {title: '图书管理', items: ['查看图书', '发布图书'], path: ['/bookManagement', '/addBook']},
        {title: '借还书管理', items: ['借书', '还书'], path: ['/borrow-book', '/back-book']},
        {title: '预约借书', items: ['预约借书'], path: ['/edit']}
      ],
    }
  },
  mounted() {
    var str = localStorage.getItem('user');
    var user = JSON.parse(str);
    this.role = user.role;
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
      this.open_list = [key];
    },
  }
}
</script>

<style scoped>
.el-aside {
  background-color: #2d3a4b;
  color: #333;
  text-align: center;
  font-size: 28px;
  font-weight: 700;
  margin-top: -60px;
  position: fixed;
  height: 100%;
  padding: 10px;
  z-index: 200;
}

.el-menu {
  border-right: none;
}
.el-col{
  margin-left: -20px;
}
.el-submenu .el-menu-item{
  min-width: 100px;
}
.el-menu-item.is-active {
  color: #3370ff !important;
}
</style>
