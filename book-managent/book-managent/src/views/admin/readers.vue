<template>
  <div>
    <el-table
        border
        :data="tableData"
        style="width: 80%; margin-left: 220px;margin-top: 50px">
      <el-table-column
          label="注册时间"
          align="center"
          prop="date">
      </el-table-column>
      <el-table-column
          label="用户名"
          align="center"
          prop="username">
      </el-table-column>
      <el-table-column
          label="邮箱"
          align="center"
          prop="email">
      </el-table-column>
      <el-table-column
          label="操作"
          align="center">
        <template slot-scope="scope">
          <el-button size="mini" type="primary" icon="el-icon-edit" circle
                     @click="handleEdit(scope.$index)"></el-button>
          &nbsp;&nbsp;
          <el-button slot="reference" size="mini"
                     @click="handleDelete(scope.$index)" type="danger" icon="el-icon-delete" circle>
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div id="addUser">
      <el-button type="primary" @click="dialogFormAddUser = true">新增用户</el-button>
    </div>
    <div>
      <el-dialog title="用户修改" :visible.sync="dialogFormEditUser">
        <el-form :model="form">
          <el-form-item label="用户名" label-width="100px">
            <el-input v-model="form.username" :value="form.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="邮箱" label-width="100px">
            <el-input type="email" v-model="form.email" :value="form.email" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormEditUser = false">取 消</el-button>
          <el-button type="primary" @click="commit">确 定</el-button>
        </div>
      </el-dialog>

      <el-dialog title="新增用户" :visible.sync="dialogFormAddUser">
        <el-form :model="addForm" status-icon :rules="rules">
          <el-form-item label="用户名" label-width="100px" prop="username">
            <el-input v-model="addForm.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="email"
                        label-width="100px"
                        label="邮箱"
                        :rules="[
                      { required: true, message: '请输入邮箱地址', trigger: 'blur' },
                      { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
                    ]"
          >
            <el-input type="email" v-model="addForm.email" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" label-width="100px" prop="password">
            <el-input type="password" v-model="addForm.password" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" label-width="100px" prop="password2">
            <el-input type="password" v-model="addForm.password2" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormAddUser = false">取 消</el-button>
          <el-button type="primary" @click="commit">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import {DeleteUser, EditUser, GetUser, Register} from "@/api/requests";

export default {
  name: "readers",
  data() {
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('用户名不能为空'));
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.addForm.password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      dialogFormEditUser: false,
      dialogFormAddUser: false,
      tableData: [],
      index: '',
      form: {
        email: '',
        username: '',
      },
      addForm: {
        email: '',
        username: '',
        password: '',
        password2: '',
      },
      rules: {
        password: [
          {validator: validatePass, trigger: 'blur', required: true}
        ],
        password2: [
          {validator: validatePass2, trigger: 'blur', required: true}
        ],
        username: [
          {validator: checkName, trigger: 'blur', required: true}
        ]
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
    load() {
      GetUser().then((res) => {
        this.tableData = res.data
      })
    },
    handleEdit: function (index) {
      this.index = index;
      this.dialogFormEditUser = true
      this.form.username = this.tableData[index].username
      this.form.email = this.tableData[index].email
    },
    handleDelete(index) {
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        DeleteUser(this.tableData[index].id).then((res) => {
          if (res.status == 200) {
            this.$message({
              type: 'success',
              message: res.message
            })
            this.tableData.splice(index, 1);
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    commit() {
      if (this.dialogFormEditUser === true) {
        EditUser(this.form, this.tableData[this.index].id).then((res) => {
          if (res.status == 200) {
            this.dialogFormEditUser = false;
            this.dialogFormAddUser = false;
            this.$message({
              type: 'success',
              message: res.message
            })
            this.tableData[this.index].username = this.form.username;
            this.tableData[this.index].email = this.form.email
            this.index = '';
          } else {
            this.$message({
              type: 'error',
              message: res.message
            })
          }
        })
      } else {
        Register(this.addForm).then((res) => {
          if (res.status == 200) {
            this.$message({
              type: 'success',
              message: '添加成功!'
            })
            this.dialogFormAddUser = false;
            this.dialogFormEditUser = false;
            this.load()
          } else {
            this.$message({
              type: 'error',
              message: res.message
            })
          }
        })
      }
    }
  },
}
</script>

<style scoped>
.el-table {
  text-align: center;
}

#addUser {
  float: right;
  margin-right: 60px;
  margin-top: 20px;
}
</style>
