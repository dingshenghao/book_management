import request from "axios"

const username = localStorage.getItem('username')

const service = request.create({
    baseURL: 'http://127.0.0.1:8000/',
    timeout: 20000,
    headers: {'username': username}
})


service.interceptors.response.use(
    response => {
        const res = response.data;

        // 判断response状态

        return res;
    },
    error => {
        return Promise.reject(error)
    }
)


export default service


