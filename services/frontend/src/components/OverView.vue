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
        y: [3, 8, 9, 10, 13, 15, 13, 17, 2, 4, 17, 4, 5, 6, 7, 10, 5, 6, 7, 17, 2, 3, 4, 2],
        mode: 'lines+markers',
        type: 'scatter'
      };
      var trace2 = {
        x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        y: [13, 7, 12, 5, 2, 4, 5, 6, 12, 6, 7, 6, 7, 5, 4, 10, 4, 5, 12, 11, 16, 5, 11, 9],
        mode: 'lines+markers',
        type: 'scatter'
      };
      var trace3 = {
        x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        y: [12, 9, 13, 17, 5, 6, 7, 2, 4, 17, 17, 4, 5, 6, 7, 10, 2, 3, 4, 15, 12, 4, 5, 6],
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