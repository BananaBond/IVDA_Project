<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <h2>Low ESS: Depression Exploration</h2>
    </v-app-bar>
    <v-main>
      <ConfigurationPanel/>
    </v-main>
  </v-app>
</template>

<style>
/* disable scrolling */
html {
  scrollbar-width: none; /* For Firefox */
  -ms-overflow-style: none; /* For Internet Explorer and Edge */
}
html::-webkit-scrollbar {
  width: 0px; /* For Chrome, Safari, and Opera */
}
</style>


<script>
import ConfigurationPanel from './components/ConfigurationPanel';
export default {
  name: 'App',
  components: {
    ConfigurationPanel,
  },
  data: () => ({
    //
  }),
};
</script>