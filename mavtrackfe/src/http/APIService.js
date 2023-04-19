/* eslint-disable */
import axios from 'axios';

// const API_URL = 'https://maverickstudent1.pythonanywhere.com';
const API_URL = 'http://127.0.0.1:8000';

export class APIService {
    constructor() {
    }

    // Login User
    authenticateLogin(credentials) {
        const url = `${API_URL}/auth/`;
        return axios.post(url, credentials);
    }

    // Register User
    registerUser(credentials) {
        const url = `${API_URL}/register/`;
        credentials.customusername = credentials.username
        return axios.post(url, credentials);
    }

    // Get Fun facts
    getFunFactList() {
        return axios.get(`${API_URL}/fun-facts/`);
    }

    // Get Daily Hints
    getDailyHintList() {
        return axios.get(`${API_URL}/daily-hints/`);
    }

    // Get Daily Hints
    getPromptsEncouragementList() {
        return axios.get(`${API_URL}/prompts-encouragement/`);
    }

    // Get Recommended Exercises
    getRecommendedExerciseList() {
        return axios.get(`${API_URL}/recommended-exercises/`);
    }

    // Get Categories
    getTrainingCategoryList() {
        const url = `${API_URL}/training-categories/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Get Goals
    getTrainingGoalList() {
        const url = `${API_URL}/training-goals/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Get level
    getTrainingLevelList() {
        const url = `${API_URL}/training-levels/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Get Daily Tasks
    getDailyTaskList() {
        const url = `${API_URL}/daily-tasks-list/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Create Daily Task
    createDailyTask(tasks) {
        const url = `${API_URL}/daily-tasks-create/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        console.log("Output Daily Tasks", tasks)
        return axios.post(url, tasks, config);
    }

    // Get Training Preferences List
    getTrainingPreferenceList() {
        const url = `${API_URL}/training-preferences-list/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Create Training Preferences
    createTrainingPreference(preferences) {
        const url = `${API_URL}/training-preferences-create/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        console.log("Output Preference", preferences)
        return axios.post(url, preferences, config);

        // const url = `${API_URL}/training-preferences/`;
        // let jwtToken = localStorage.getItem('token');
        // console.log(":::jwtToken:::::" + jwtToken);
        // const config = {Authorization: `jwt ${jwtToken}`};
        // console.log("Output Data: ", preferences)
        // return axios.post(url, preferences, config);
    }

    getTrainingPreference(param_pk) {
        const url = `${API_URL}/training-preferences/${param_pk}`;
        let jwtToken = localStorage.getItem('token');
        console.log(":::jwtToken:::::" + jwtToken);
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.get(url, {headers: {Authorization: `jwt ${jwtToken}`}});
    }

    updatePlan(preference) {
        const url = `${API_URL}/training-preferences/${preference.pk}`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.put(url, preference, {headers: headers});
    }

    deletePlan(preference_Pk) {
        const url = `${API_URL}/training-preferences/${preference_Pk}`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.delete(url, {headers: headers});
    }

    // Get Training Schedule
    getTrainingScheduleList() {
        const url = `${API_URL}/training-schedules/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        return axios.get(url, config);
    }

    // Create Training Schedule
    createTrainingSchedule(schedules) {
        const url = `${API_URL}/training-schedules/`;
        const token = localStorage.getItem('token');
        const config = {
            headers: {
                Authorization: `JWT ${token}`,
            },
        };
        console.log("Output Schedule", schedules)
        return axios.post(url, schedules, config);
    }

    // Forgot Password
    forgotPassword(email) {
        const url = `${API_URL}/forgot-password/`;
        const data = {email};
        const response = axios.post(url, data);
        return response.data;
    }

    // Reset Password
    resetPassword(data) {
        const url = `${API_URL}/reset-password/`;
        const response = axios.post(url, data);
        return response.data;
    }

    // Customers
    getCustomer(param_pk) {
        const url = `${API_URL}/api/customers/${param_pk}`;
        let jwtToken = localStorage.getItem('token');
        console.log(":::jwtToken:::::" + jwtToken);
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.get(url, {headers: {Authorization: `jwt ${jwtToken}`}});
    }

    getCustomerList() {
        const url = `${API_URL}/api/customers/`;
        let jwtToken = localStorage.getItem('token');
        console.log(":::jwtToken:::::" + jwtToken);
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.get(url, {headers: headers});
    }

    addNewCustomer(customer) {
        const url = `${API_URL}/api/customers/`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.post(url, customer, {headers: headers});
    }

    updateCustomer(customer) {
        const url = `${API_URL}/api/customers/${customer.pk}`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.put(url, customer, {headers: headers});
    }

    deleteCustomer(customer_Pk) {
        const url = `${API_URL}/api/customers/${customer_Pk}`;
        let jwtToken = localStorage.getItem('token');
        const headers = {Authorization: `jwt ${jwtToken}`};
        return axios.delete(url, {headers: headers});
    }
}

