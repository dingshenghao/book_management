import service from "@/utils/request";

// 登录
export function Login(data) {
    return service({
        url: 'login/',
        method: 'post',
        data: data
    })
}

// 注册
export function Register(data) {
    return service({
        url: 'register/',
        method: 'post',
        data: data
    })
}


// 删除用户
export function deleteUser(id) {
    return service({
        url: 'deleteUser/' + id + '/',
        method: 'delete'
    })
}

// 修改用户信息
export function EditUser(data, id) {
    return service({
        url: 'editUser/' + id + '/',
        method: 'put',
        data: data
    })
}

// 上传头像
export function UploadIcon(id, data) {
    return service({
        url: 'uploadIcon/' + id + '/',
        method: 'put',
        data: data
    })
}

// 查看读者
export function GetUser() {
    return service({
        url: 'getUsers/',
        method: 'get'
    })
}

// 删除读者
export function DeleteUser(id) {
    return service({
        url: 'deleteUser/' + id +'/',
        method: 'delete'
    })
}

// 添加用户
export function addUser(data) {
    return service({
        url: 'addUser/',
        method: 'post',
        data: data
    })
}

// 获取分类
export function GetCategory(){
    return service({
        url: 'category/',
        method: 'get'
    })
}
// 发布图书
export function AddBook(data){
    return service({
        url: 'addBook/',
        method: 'post',
        data: data
    })
}
// 获取图书
export function GetBooks(){
    return service({
        url: 'books/',
        method: 'get'
    })
}
// 修改图书
export function EditBook(id, data){
    return service({
        url: 'editBook/' + id + '/',
        method: 'put',
        data: data
    })
}
// 删除图书
export function DeleteBook(id){
    return service({
        url: 'deleteBook/' + id + '/',
        method: 'delete'
    })
}

// 借书
export function BorrowBook(data){
    return service({
        url: 'borrowBook/',
        method: 'post',
        data: data
    })
}
// 获取借书列表
export function GetBorrow(id){
    return service({
        url: 'getBorrow/?id=' + id,
        method: 'get'
    })
}
export function BackBook(data){
    return service({
        url: 'backBook/',
        method: 'put',
        data: data
    })
}
// 获取还书列表
export function GetBorrow1(id){
    return service({
        url: 'getBorrow1/?id=' + id,
        method: 'get'
    })
}
// 预约借书
export function GetReservation(data){
    return service({
        url: 'reservation/',
        method: 'post',
        data: data
    })
}
// 取消预约
export function UnReservation(id,data){
    return service({
        url: 'unReservation/' + id + '/',
        method: 'delete',
        data: data
    })
}

// 借阅历史
export function GetHistory(id){
    return service({
        url: 'history/' + id + '/',
        method: 'get'
    })
}

// 同意预约
export function AgreeReservation(data){
    return service({
        url: 'agreeReservation/',
        method: 'put',
        data: data
    })
}
// 获取预约列表
export function ReservationList(){
    return service({
        url: "getReservations/",
        method: 'get'
    })
}

// 获取某一分类下的图书
export function getBookByCategory(id){
    return service({
        url: 'getBookByCategory/' + id + '/',
        method: 'get'
    })
}

// 图书搜索
export function SearchBook(data){
    return service({
        'url': 'searchBook/',
        method: 'post',
        data: data
    })
}
