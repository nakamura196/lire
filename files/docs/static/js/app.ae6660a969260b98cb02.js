webpackJsonp([0],{"1/oy":function(t,e){},"3LKl":function(t,e){},"9M+g":function(t,e){},"AN/a":function(t,e){},GfHa:function(t,e){},Id91:function(t,e){},Jmt5:function(t,e){},NHnr:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=a("7+uW"),n={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("b-navbar",{attrs:{toggleable:"md",type:"dark",variant:"info"}},[e("b-navbar-brand",{attrs:{href:"#"}},[this._v("LireSolr Demo")])],1),this._v(" "),e("router-view"),this._v(" "),this._m(0)],1)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("footer",{staticClass:"bd-footer text-muted my-5"},[e("div",{staticClass:"container"},[this._v("\n    Demo application created by Satoru Nakamura with "),e("a",{attrs:{href:"https://jp.vuejs.org/index.html"}},[this._v("Vue.js")]),this._v(" and "),e("a",{attrs:{href:"http://www.lire-project.net/"}},[this._v("Lire")]),this._v(".\n      ")])])}]};var i=a("VU/8")({name:"App"},n,!1,function(t){a("3LKl")},null,null).exports,o=a("/ocq"),s=a("e6fC");a("Jmt5"),a("9M+g");r.a.use(s.a);var u={name:"HelloWorld",data:function(){return{msg:"Welcome to Your Vue.js App",items:[],keyword:"",message:"",imgurl:"",id:"",number:40,accuracy:.9,feature:"ph",features:[{text:"PHOG",value:"ph"},{text:"ColorLayout",value:"cl"},{text:"JCD",value:"jc"},{text:"Edge Histgram",value:"eh"}]}},methods:{getAnswer:function(t){this.id=t;var e=this,a={ms:"false",fl:"*",field:this.feature,rows:this.number,accuracy:this.accuracy,candidates:"1000"};""!=this.imgurl&&(a.url=this.imgurl),""!=this.id&&(a.id=this.id),axios.get("http://104.154.80.89/solr/lire/lireq",{params:a}).then(function(t){var a=t.data.response;a.docs?e.items=a.docs:e.items=a}).catch(function(t){e.message="Error!"+t}).finally(function(){})},onSubmit:function(t){t.preventDefault()},onReset:function(t){var e=this;t.preventDefault(),this.email="",this.name="",this.food=null,this.checked=[],this.show=!1,this.$nextTick(function(){e.show=!0})},goCuration:function(t){var e=t.split("#"),a="http://codh.rois.ac.jp/software/iiif-curation-viewer/demo/?curation="+e[0]+"&pos="+e[1];window.open(a,"icv")}}},c={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("b-container",{staticClass:"my-5"},[a("b-form",{on:{submit:t.onSubmit,reset:t.onReset}},[a("b-form-group",{attrs:{id:"exampleInputGroup2",label:"Image URL:","label-for":"exampleInput2"}},[a("b-form-input",{attrs:{id:"exampleInput2",type:"text",placeholder:"http://..."},model:{value:t.imgurl,callback:function(e){t.imgurl=e},expression:"imgurl"}})],1),t._v(" "),a("b-row",[a("b-col",{attrs:{sm:"4"}},[a("b-form-group",{attrs:{id:"exampleInputGroup3",label:"Search feature:","label-for":"exampleInput3"}},[a("b-form-select",{attrs:{id:"exampleInput3",options:t.features},model:{value:t.feature,callback:function(e){t.feature=e},expression:"feature"}})],1)],1),t._v(" "),a("b-col",{attrs:{sm:"4"}},[a("b-form-group",{attrs:{id:"exampleInputGroup1",label:"# Results:","label-for":"exampleInput1"}},[a("b-form-input",{attrs:{id:"exampleInput1",type:"number"},model:{value:t.number,callback:function(e){t.number=e},expression:"number"}})],1)],1),t._v(" "),a("b-col",{attrs:{sm:"4"}},[a("b-form-group",{attrs:{id:"exampleInputGroup1",label:"Accuracy:","label-for":"exampleInput1"}},[a("b-form-input",{attrs:{id:"exampleInput1",type:"text"},model:{value:t.accuracy,callback:function(e){t.accuracy=e},expression:"accuracy"}})],1)],1)],1),t._v(" "),a("b-button",{attrs:{type:"button",variant:"primary"},on:{click:function(e){t.getAnswer()}}},[t._v("Search")])],1),t._v(" "),a("b-row",{staticClass:"my-5"},t._l(t.items,function(e){return a("b-col",{staticClass:"mb-4",attrs:{sm:"3"}},[a("b-card",{attrs:{"img-src":e.imgurl,"img-alt":"image","img-top":""}},[a("p",{staticClass:"card-text"},[a("b-button",{attrs:{type:"button",variant:"primary"},on:{click:function(a){t.getAnswer(e.id)}}},[t._v("Search")]),t._v(" "),a("b-button",{attrs:{type:"button",variant:"primary"},on:{click:function(a){t.goCuration(e.id)}}},[t._v("View")])],1)])],1)}),1)],1)},staticRenderFns:[]};var l=a("VU/8")(u,c,!1,function(t){a("AN/a")},"data-v-3ddfdcb8",null).exports;r.a.use(o.a);var p=new o.a({routes:[{path:"/",name:"HelloWorld",component:l}]});r.a.config.productionTip=!1,new r.a({el:"#app",router:p,components:{App:i},template:"<App/>"})},zj2Q:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.ae6660a969260b98cb02.js.map