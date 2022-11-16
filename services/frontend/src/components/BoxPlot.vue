<template>
  <div style="height: 40vh">
    <div id='thirdBoxPlot' style="height: inherit">
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "BoxPlot",
  data: () => ({
    person: 'condition1',
    times: {},
    activity_levels: {},
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    createTimeData(){
      var arr = [];
      for (let i=0; i < 10; i++) {
          arr.push(`0${i}:00`);
      }
      for (let i=10; i < 24; i++) {
          arr.push(`${i}:00`);
      }
      return arr
    },
  //   async fetchDaysinStudy(person){
    fetchDaysinStudy(){
      //need to refactor code to fetch number of days from score table for specific condition person
      return 15
    },
  //   async get_activity_levels_for_time(person, time) {
    get_activity_levels_for_time(time) {
      // split_string = whole_string.split(/(\d+)/)
      // console.log(split_string)
      // console.log(time)
      if (time == "00:00" || time == "01:00" || time == "02:00" ||time == "03:00" ||time == "04:00" ||time == "05:00" ||time == "6:00" || time == "23:00") {
          return Math.floor(Math.random() * (10 - 0 + 1)) + 0;
      }
      else{
          return Math.floor(Math.random() * (1000 - 15 + 1)) + 15;
      }
      // var reqUrl = 'http://127.0.0.1:5000/condition_19'
      // console.log("ReqURL " + reqUrl)
      // // await response and data
      // const response_ = await fetch(reqUrl)
      // // console.log(response)
      // const responseData = await response_.json()
      // // transform data to usable by lineplot
      // // console.log(responseData)
      // responseData.forEach(output => {
      //     if (output.timestamp.includes(`T${time}`)){
      //         return output.activity_level
              
      //     }
      // })
    },
  // async createTimeData(person, times){
    createActivityData(times_array){
      var master_dict = {};
      console.log(times_array);
      // var newarray = Object.keys(times_array);
      // console.log(typeof(newarray));
      // console.log(JSON.parse(JSON.stringify(newarray)))
      // console.log(newarray);
      // console.log(length)
      times_array.forEach(time => {
          master_dict[time] = []
          // days_in_study = fetchDaysinStudy(person)
          var days_in_study = this.fetchDaysinStudy()
          for (let day_number = 1; day_number <= days_in_study; day_number++) {
              // activity_level = this.get_activity_levels_for_time(person, time)
              var activity_level = this.get_activity_levels_for_time(time)
              master_dict[time].push(activity_level)
          }
          
      });
      return master_dict
    },
    async fetchData() {
      // req URL to retrieve companies from backend
      // var reqUrl = 'http://127.0.0.1:5000/companies'
      // console.log("ReqURL " + reqUrl)
      // await response and data
      // const response = await fetch(reqUrl)
      // const responseData = await response.json();
      // transform data to usable by scatterplot
      // responseData.forEach((company) => {
      //   this.ScatterPlotData.x.push(company.employees)
      //   this.ScatterPlotData.y.push(company.founding_year)
      // })
      // after the data is loaded, draw the plot
      this.times = this.createTimeData()
      

      // this.activity_levels= this.createActivityData(this.person, this.times)
      this.activity_levels = this.createActivityData(this.times)

      console.log(this.times)
      console.log('activity levels', this.activity_levels)
      this.drawScatterPlot()
    },


    drawScatterPlot() {
      var data = []
      this.times.forEach(time => {
          var new_trace = {
              y: this.activity_levels[time],
              type: 'box',
              name: time,
              marker: {
                  color: 'rgb(107,174,214)'
              }
          }
          data.push(new_trace)
          new_trace = {}
      })

      // Plotly.newPlot('myScatterPlot', data);
      // var config = {responsive: true, displayModeBar: false}
      var layout = {
          title: {
          text:'condition_19',
          font: {
          family: 'Helvetica',
          size: 24
          },
          xref: 'paper',
          x: 0.05,
      },
      xaxis: {
          title: {
          text: 'Time (hours)',
          font: {
              family: 'Helvetica',
              size: 18,
              color: '#7f7f7f'
          }
          },
      },
      yaxis: {
          title: {
          text: 'Activity level',
          font: {
              family: 'Helvetica',
              size: 18,
              color: '#7f7f7f'
          }
          }
      }
      };

          Plotly.newPlot('thirdBoxPlot', data, layout);
      }
  }
}
</script>

<style scoped>

</style>