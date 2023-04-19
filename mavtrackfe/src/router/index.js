import {createRouter, createWebHashHistory} from 'vue-router'
import Home from '@/views/Home.vue'
import Auth from '@/components/Auth.vue'
import Register from '@/components/Register'
import TrainingPlans from '@/components/TrainingPlans'
import TrainingPreferences from "@/components/TrainingPreferences";
import TrainingSchedules from '@/components/TrainingSchedules'
import ForgotPassword from "@/components/ForgotPassword";
import ResetPassword from "@/components/ResetPassword";
import ResetPasswordForm from '@/components/ResetPasswordForm';
import CustomerList from '@/components/CustomerList'
import CustomerCreate from '@/components/CustomerCreate'

const routes = [
    // Home Page
    {
        path: '/',
        name: 'home',
        component: Home
    },

    // About Page
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },

    // login
    {
        path: '/auth',
        name: 'Auth',
        component: Auth
    },

    // Register User
    {
        path: '/register',
        name: 'Register',
        component: Register
    },

    // Training Plan
    {
        path: '/training-plans/',
        name: 'TrainingPlans',
        component: TrainingPlans
    },
    {
        path: '/training-plans/:msg',
        name: 'TrainingPlansUpdatedList',
        component: CustomerList
    },

    // Training Preferences
    {
        path: '/training-preferences/',
        name: 'TrainingPreferencesCreate',
        component: TrainingPreferences
    },
    {
        path: '/training-preferences/:id',
        name: 'TrainingPreferencesUpdate',
        component: TrainingPreferences
    },

    // Training Schedule
    {
        path: '/training-schedules/',
        name: 'TrainingSchedules',
        component: TrainingSchedules
    },

    // Forgot Password
    {
        path: '/forgot-password/',
        name: 'ForgotPassword',
        component: ForgotPassword
    },
    // Reset Password
    {
        path: '/reset-password/:uidb64/:token/',
        name: 'ResetPassword',
        component: ResetPassword,
        props: true,
    },
    // Reset Password Form
    {
        path: '/reset-password-form/',
        name: 'ResetPasswordForm',
        component: ResetPasswordForm,
        props: true,
    },


    // Customer Feature
    {
        path: '/customer-list',
        name: 'CustomerList',
        component: CustomerList
    },
    {
        path: '/customer-list/:msg',
        name: 'CustomerUpdatedList',
        component: CustomerList
    },
    {
        path: '/customer-create',
        name: 'CustomerCreate',
        component: CustomerCreate
    },
    {
        path: '/customer-create/:pk',
        name: 'CustomerUpdate',
        component: CustomerCreate
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
