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
      var Depressed = {
        x: ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69"],
        y: [1, 5, 3, 7, 4, 1, 5, 4, 5],
        type: 'bar'
      };
      var Non_Depressed = {
        x: ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69"],
        y: [6, 5, 1, 5, 6, 1, 2, 5, 6],
        type: 'bar'
      };
      var data = [Depressed, Non_Depressed];
      Plotly.newPlot('secondDetailsAlign', data);

    }
  }
}
</script>


<style scoped>

</style>