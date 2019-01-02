<template>
  <b-container class="my-5">

  <b-form @submit="onSubmit" @reset="onReset">

<b-form-group id="exampleInputGroup2"
                    label="Image URL:"
                    label-for="exampleInput2">
        <b-form-input id="exampleInput2"
                      type="text"
                      v-model="imgurl"
                      placeholder="http://...">
        </b-form-input>
      </b-form-group>

    <b-row>
        <b-col sm="4">
        <b-form-group id="exampleInputGroup3"
                    label="Search feature:"
                    label-for="exampleInput3">
        <b-form-select id="exampleInput3"
                      :options="features"
                      v-model="feature">
        </b-form-select>
      </b-form-group>
        </b-col>
        <b-col sm="4">
        <b-form-group id="exampleInputGroup1"
                    label="# Results:"
                    label-for="exampleInput1">
        <b-form-input id="exampleInput1"
                      type="number"
                      v-model="number">
        </b-form-input>
      </b-form-group>
        </b-col>

        <b-col sm="4">
        <b-form-group id="exampleInputGroup1"
                    label="Accuracy:"
                    label-for="exampleInput1">
        <b-form-input id="exampleInput1"
                      type="text"
                      v-model="accuracy">
        </b-form-input>
      </b-form-group>
      
        </b-col>
    </b-row>

      <b-button type="button" variant="primary" v-on:click="getAnswer();">Search</b-button>
    </b-form>

  <b-row class="my-5">
    <b-col sm="3" v-for="item in items" class="mb-4">

      <b-card v-bind:img-src="item.imgurl"
                img-alt="image"
                img-top>
            <p class="card-text">
              <b-button type="button" variant="primary" v-on:click="getAnswer(item.id);">Search</b-button>
                 <b-button type="button" variant="primary" v-on:click="goCuration(item.id);">View</b-button>
            </p>
        </b-card>

      </b-col>
  </b-row>


  </b-container>
</template>

<script>
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      items: [],
      keyword: '',
      message: '',
      imgurl: "",
      id: "",
      number: 40,
      accuracy: 0.9,
      feature: "ph",
      features: [
        { text: 'PHOG', value: "ph" },
        { text: 'ColorLayout', value: "cl" },
        { text: 'JCD', value: "jc" },
        { text: 'Edge Histgram', value: "eh" },
      ]
    }
  },
  methods: {
      getAnswer: function(id){
        this.id = id
      
        var vm = this;

        var params = {
          ms:"false",
          fl: "*",
          field: this.feature,
          rows: this.number,
          accuracy: this.accuracy,
          candidates: "1000"
          };
          if(this.imgurl != ""){
            params.url = this.imgurl
          }
          if(this.id != ""){
            params.id = this.id
          }

        axios.get('http://104.154.80.89/solr/lire/lireq', {params})
          .then(function(response){
            var tmp = response.data.response

            if(tmp.docs){
              vm.items = tmp.docs;
            } else {
              vm.items = tmp;
            }    
          })
          .catch(function(error){
            vm.message = 'Error!' + error;
          })
          .finally(function(){
            //vm.message = '';
          })

      },
      onSubmit (evt) {
      evt.preventDefault();
      //alert(JSON.stringify(this.form));
    },
    onReset (evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.email = '';
      this.name = '';
      this.food = null;
      this.checked = [];
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.$nextTick(() => { this.show = true });
    },
    goCuration: function(id){
        
        var tmp = id.split("#")
        var curation_uri = tmp[0]
        var pos = tmp[1]
        var url = "http://codh.rois.ac.jp/software/iiif-curation-viewer/demo/?curation="+curation_uri+"&pos="+pos
        window.open(url,'icv');
      
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
