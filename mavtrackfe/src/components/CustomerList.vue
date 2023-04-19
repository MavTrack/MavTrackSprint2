<template>
  <div class="container-fluid">
    <!--Welcome Title -->
    <div class="row align-items-center justify-content-center">
      <div class="col col-12 align-items-center justify-content-center">
        <blockquote>
          Welcome {{ validUserName }}!
          <footer>
            <small>
              <em>MavTrack</em>
            </small>
          </footer>
        </blockquote>
      </div>
      <div class="col-12 col-md-10 col-lg-10 col-12 align-items-center justify-content-center">
        <div class="alert alert-success" v-if="showMsg === 'new'" :value="true">
          New customer has been added.
        </div>
        <div class="alert alert-success" v-if="showMsg === 'update'" :value="true">
          Customer information has been updated.
        </div>
        <div class="alert alert-success" v-if="showMsg === 'deleted'" :value="true">
          Selected customer has been deleted.
        </div>
      </div>
    </div>
    <!-- Data table -->
    <div class="row align-items-center justify-content-center">
      <div class="d-md-none" id="collapsable-card" style="width: 80%">
        <button type="button"
                class="btn btn-primary"
                @click="addNewCustomer"
                style="background-color: white;
                border-color: white"
        >
          <svg xmlns="http://www.w3.org/2000/svg"
               width="50"
               height="50"
               fill="#0275d8"
               class="bi bi-plus-circle-fill"
               viewBox="0 0 16 16"
          >
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
          </svg>
        </button>
        <div class="card" v-for="customer in customers" v-bind:key="customer">
          <div class="card-header" :id="'heading' + customer.pk">
            <button class="btn btn-link collapsed"
                    data-bs-toggle="collapse"
                    :data-bs-target="'#collapse' + customer.pk"
                    aria-expanded="true"
                    :aria-controls="'collapse' + customer.pk"
            >
              <h6 style="color: #0275d8; float: left">{{ customer.name }}</h6>
            </button>
          </div>
          <div :id="'collapse' + customer.pk"
               class="collapse"
               :aria-labelledby="'heading' + customer.pk"
               data-bs-parent="#collapsable-card"
          >
            <div class="card-body">
              <p><b>Customer #:</b> {{ customer.cust_number }}</p>
              <p><b>Address:</b>
                <br/> {{ customer.address }},
                <br/> {{ customer.city }},
                <br/> {{ customer.state }}
                {{ customer.zipcode }}
              </p>
              <p><b>Email:</b> {{ customer.email }}</p>
              <p><b>Phone:</b> {{ customer.cell_phone }}</p>
              <div class="btn-group">
                <button @click="updateCustomer(customer)"
                        style="background-color: transparent;
                        padding: 0;"
                >
                  <svg xmlns="http://www.w3.org/2000/svg"
                       width="20"
                       height="20"
                       fill="currentColor"
                       class="bi bi-pencil"
                       viewBox="0 0 16 16">
                    <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
                  </svg>
                </button>
                <button @click="deleteCustomer(customer)"
                        style="background-color: transparent;
                        padding: 0;"
                >
                  <svg @click="deleteCustomer"
                       xmlns="http://www.w3.org/2000/svg"
                       width="20"
                       height="20"
                       fill="currentColor"
                       class="bi bi-trash-fill"
                       viewBox="0 0 16 16">
                    <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col col-12 col-md-10 d-none d-xl-block d-lg-block d-md-block">
        <table class="table table-hover" style="overflow-y: auto" :headers="headers">
          <thead>
          <tr>
            <th scope="col">Customer #</th>
            <th scope="col">Name</th>
            <th scope="col">Address</th>
            <th scope="col">City</th>
            <th scope="col">State</th>
            <th scope="col">Zip Code</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
            <th scope="col">Update</th>
            <th scope="col">Delete</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="customer in customers" v-bind:key="customer">
            <!-- Should be customer.cust_number but not working -->
            <th scope="row">{{ customer.cust_number }}</th>
            <td>{{ customer.name }}</td>
            <td>{{ customer.address }}</td>
            <td>{{ customer.city }}</td>
            <td>{{ customer.state }}</td>
            <td>{{ customer.zipcode }}</td>
            <td>{{ customer.email }}</td>
            <td>{{ customer.cell_phone }}</td>
            <td @click="updateCustomer(customer)">
              <button style="background-color: transparent; padding: 0;">
                <svg xmlns="http://www.w3.org/2000/svg"
                     width="16"
                     height="16"
                     fill="currentColor"
                     class="bi bi-pencil"
                     viewBox="0 0 16 16"
                >
                  <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
                </svg>
              </button>
            </td>
            <td @click="deleteCustomer(customer)">
              <button style="background-color: transparent; padding: 0;">
                <svg @click="deleteCustomer"
                     xmlns="http://www.w3.org/2000/svg"
                     width="16"
                     height="16"
                     fill="currentColor"
                     class="bi bi-trash-fill"
                     viewBox="0 0 16 16"
                >
                  <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                </svg>
              </button>
            </td>
          </tr>
          </tbody>
        </table>
        <button type="button" class="btn btn-primary" @click="addNewCustomer">Add New Customer</button>
      </div>
    </div>
  </div>
</template>
<script>
import router from '../router';
import {APIService} from '../http/APIService';

const apiService = new APIService();

export default {
  name: "CustomerList",
  data: () => ({
    customers: [],
    validUserName: "Guest",
    customerSize: 0,
    showMsg: '',
    isMobile: false,
    headers: [
      {text: 'Customer Number', sortable: false, align: 'left',},
      {text: 'Name', sortable: false, align: 'left',},
      {text: 'Address', sortable: false, align: 'left',},
      {text: 'City', sortable: false, align: 'left',},
      {text: 'State', sortable: false, align: 'left',},
      {text: 'ZipCode', sortable: false, align: 'left',},
      {text: 'Email', sortable: false, align: 'left',},
      {text: 'Phone', sortable: false, align: 'left',},
      {text: 'Update', sortable: false, align: 'left',},
      {text: 'Delete', sortable: false, align: 'left',}
    ],
  }),
  mounted() {
    this.getCustomers();
    this.showMessages();
  },
  methods: {
    onResize() {
      if (window.innerWidth > 600)
        this.isMobile = false;
      else
        this.isMobile = true;
    },
    showMessages() {
      console.log(this.$route.params.msg)
      if (this.$route.params.msg) {
        this.showMsg = this.$route.params.msg;
      }
    },
    getCustomers() {
      apiService.getCustomerList().then(response => {
        this.customers = response.data.data;
        this.customerSize = this.customers.length;
        if (localStorage.getItem("isAuthenticates")
            && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
          this.validUserName = JSON.parse(localStorage.getItem("log_user"));
        }
      }).catch(error => {
        if (error.response.status === 401) {
          localStorage.removeItem('isAuthenticates');
          localStorage.removeItem('log_user');
          localStorage.removeItem('token');
          router.push("/auth");
        }
      });
    },
    addNewCustomer() {
      if (localStorage.getItem("isAuthenticates")
          && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
        router.push('/customer-create');
      } else {
        router.push("/auth");
      }
    },
    updateCustomer(customer) {
      router.push('/customer-create/' + customer.pk);
    },
    deleteCustomer(customer) {
      if (confirm("Do you really want to delete?")) {
        apiService.deleteCustomer(customer.pk).then(response => {
          if (response.status === 204) {
            router.push('/customer-list/deleted/')
            this.getCustomers()
          }
        }).catch(error => {
          if (error.response.status === 401) {
            localStorage.removeItem('isAuthenticates');
            localStorage.removeItem('log_user');
            localStorage.removeItem('token');
            router.push("/auth");
          }
        });
      }
    }
  }
};
</script>
<style>
button {
  padding: 1rem;
  border: 0;
  cursor: pointer;
}
</style>