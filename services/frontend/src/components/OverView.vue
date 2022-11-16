<template>
  <div style="height: 60vh">
    <div id='firstOverView' style="height: inherit">
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';

export default {
  name: "OverView",
  data: () => ({
  }),
  mounted() {
    this.drawOverView()
  },
  methods: {
    drawOverView() {
      // plotly code comes later here
      var trace1 = {
        x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        y: [0, 1, 3, 5, 3, 1, 12, 10, 8, 11, 5, 8, 7, 30, 13, 18, 11, 35, 29, 25, 23, 32, 4, 0],
        mode: 'lines+markers',
        type: 'scatter'
      };
      var trace2 = {
        x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        y: [1, 2, 5, 5, 0, 0, 12, 12, 9, 11, 7, 11, 15, 23, 12, 13, 24, 17, 19, 29, 18, 15, 4, 2],
        mode: 'lines+markers',
        type: 'scatter'
      };
      var trace3 = {
        x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        y: [5, 5, 1, 1, 2, 0, 4, 11, 10, 4, 6, 7, 27, 35, 20, 7, 10, 32, 16, 16, 33, 26, 2, 4],
        mode: 'lines+markers',
        type: 'scatter'
      };
      var data = [trace1, trace2, trace3];
      Plotly.newPlot('firstOverView', data);

    }
  }
}
</script>

<style scoped>

</style>