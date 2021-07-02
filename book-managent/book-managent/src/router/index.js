import Vue from 'vue'
import VueRouter from 'vue-router'
import index from '../views/index'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'index',
        component: index,
        children: [
            {
                path: '/search',
                name: 'search',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/search.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/hots',
                name: 'hots',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/hosts.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/newBook',
                name: 'newBook',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/newBook.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/history',
                name: 'history',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/history.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/borrow',
                name: 'borrow',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/borrow.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/back',
                name: 'back',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/back.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/reservation',
                name: 'reservation',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/reservation.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/readers',
                name: 'readers',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/admin/readers.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/bookManagement',
                name: 'bookManagement',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/admin/bookManagement.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/borrow-book',
                name: 'borrow-book',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/borrow.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/back-book',
                name: 'back-book',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/book/back.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/userInfo',
                name: 'userInfo',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/user/userInfo.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/addBook',
                name: 'addBook',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/admin/addBook.vue')
                },
                meta: {auth: true}
            },
            {
                path: '/edit',
                name: 'edit',
                component: function () {
                    return import(/* webpackChunkName: "about" */ '../views/admin/edit.vue')
                },
                meta: {auth: true}
            },
        ]
    },
    {
        path: '/register',
        name: 'register',
        component: function () {
            return import(/* webpackChunkName: "about" */ '../views/user/register.vue')
        },
        meta: {auth: false}
    },
    {
        path: '/login',
        name: 'login',
        component: function () {
            return import(/* webpackChunkName: "about" */ '../views/user/login.vue')
        },
        meta: {auth: false}
    }

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
