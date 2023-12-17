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
              text: '',
              id: ''
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
                if(this.id){
                    data = {
                        "date": this.date,
                        "time": this.time,
                        "category": this.category,
                        "text": this.text,
                        "id": this.id
                    }
                    
                }
                console.log(data);

                this.$http.post("/api/add-appointment/", data)
                    .then(response => {
                        
                    })
                    .catch(err => {
                        console.log(err);
                        
                    })
                this.removeAll();
                
            },
            deleteNote(){
                this.id = this.$refs['instance'].dataset.id;
                this.$http.post("/api/delete-appointment/" + this.id + "/")
                    .then(response => {
                        
                    })
                    .catch(err => {
                        console.log(err);
                        
                })
                const chooseModal = document.getElementById("chooseModal");
                chooseModal.classList.remove("visible");
            },
            removeAll(){
                this.time = '';
                this.category = 'Личное';
                this.text = '';
                this.id = '';
            },
            getNote(id_note){
                
                this.$http.post("/api/get-appointment-details/" + id_note + "/", data)
                    .then(response => {
                        console.log(response.data);
                    })
                    .catch(err => {
                        console.log(err);
                        
                    })

            },
            changeNote(){
                console.log("DASDAS")
                const chooseModal = document.getElementById("chooseModal");
                const createnoteModal = document.getElementById("createnoteModal");
                chooseModal.classList.remove("visible");
                createnoteModal.classList.add("visible");
                this.date = this.$refs['instance'].dataset.date;
                this.id = this.$refs['instance'].dataset.id;
                this.text = this.$refs['instance'].dataset.text;
                this.category =  this.$refs['instance'].dataset.category;
                this.time = this.$refs['instance'].dataset.time;

            }

        }
    })
}