<template>
  <div style="height: 60vh">
    <div id='secondDetailsAlign' style="height: inherit">
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "DetailsAlign",
  data: () => ({
  }),
  mounted() {
    this.drawDetailsAlign()
  },
  methods: {
    drawDetailsAlign() {
      var trace1 = {
        x: [1, 2, 3, 4],
        y: [10, 15, 13, 17],
        mode: 'markers',
        type: 'scatter'
      };
      var trace2 = {
        x: [2, 3, 4, 5],
        y: [16, 5, 11, 9],
        mode: 'lines',
        type: 'scatter'
      };
      var data = [trace1, trace2];
      Plotly.newPlot('secondDetailsAlign', data);
    }
  }
}
</script>


<style scoped>

</style>