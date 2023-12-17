import Vue from "vue";


export let VueAddNote;

if (document.getElementById("vue-add-note")) {
    VueAddNote = new Vue({
        el: '#vue-add-note',
        name: 'vue-add-note',
        data: function() {
            return {
              date: '',
              time: '',
              category: "Личное",
              text: ''
            }
        },
        mounted: function() {
            
        },
        methods: {
            getDate(){
                this.date = this.$refs['instance'].dataset.date;
            },
            addNote(){
                let data = {
                    "date": this.date,
                    "time": this.time,
                    "category": this.category,
                    "text": this.text
                }

                this.$http.post("/api/add-appointment/", data)
                    .then(response => {
                        
                    })
                    .catch(err => {
                        console.log(err);
                        
                    })
            }
        }
    })
}