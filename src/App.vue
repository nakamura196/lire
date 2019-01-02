<template>
  <div id="app">

<b-navbar toggleable="md" type="dark" variant="info">

  <b-navbar-brand href="#">LireSolr Demo</b-navbar-brand>

  
</b-navbar>
    <router-view/>

<footer class="bd-footer text-muted my-5">
  <div class="container">
    Demo application created by Satoru Nakamura with <a href="https://jp.vuejs.org/index.html">Vue.js</a> and <a href="http://www.lire-project.net/">Lire</a>.
      </div>
      </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
</style>
