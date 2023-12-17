import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

Vue.use(VueAxios, axios);
Vue.options.delimiters = ['[[', ']]'];
