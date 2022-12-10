<template>
  <div style="height: 40vh" margin="0 auto" width="1000px">
    <div id='thirdBoxPlot' cols="12" md="12" style="height: inherit" margin="0">
    </div>
  </div>
</template>

<script>
import Plotly, { inherits } from 'plotly.js/dist/plotly';
import activity_level from '../../../../data-preprocess/data/boxplot/condition_3.json';
// import times from '../../../../data-preprocess/time.json';

export default {
  name: "BoxPlot",
  data: () => ({
    person: 'condition1',
    times: {},
    activity_levels: {},
  }),
  mounted() {
    this.drawScatterPlot()
  },
  methods: {
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
    drawScatterPlot() {
      var data = []
      console.log(Object.keys(activity_level["boxplot_data"]))
      Object.keys(activity_level["boxplot_data"]).forEach(time => {
        // var time_str = time.split(':')[1]
          var new_trace = {
              x: "00:00",
              y: activity_level["boxplot_data"][time],
              type: 'box',
              name: time.key,
              marker: {
                  color: 'rgb(129, 183, 78)'
              },
              showlegend:false
          }
          data.push(new_trace)
          new_trace = {}
      })

      // var y_list = []

      // for(var ff=0; ff<1440; ff++){
      //   if (ff%60 == 0){}
      //     y_list.push(depressed["files"][1]["activity_level"][ff])
      // }

      // var bp_times = ['00:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00','07:00:00','08:00:00'
      //     ,'09:00:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:00:00','16:00:00','17:00:00','18:00:00'
      //     ,'19:00:00','20:00:00','21:00:00','22:00:00','23:00:00']
      // bp_times.forEach(time => {
      //     var new_trace = {
      //         y: y_list,
      //         type: 'box',
      //         name: time,
      //         marker: {
      //             color: 'rgb(107,174,214)'
      //         }
      //     }
      //     data.push(new_trace)
      //     new_trace = {}
      // })
      

      // Plotly.newPlot('myScatterPlot', data);
      // var config = {responsive: true, displayModeBar: false}
      var layout = {
        margin: {
          r: 40,
          t: 15,
          pad: 5
        },
        autosize: true,
        width: inherits,
        height: 500,
        title: {
          // text:'condition_19',
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
          },
        },
          tickvals:['trace 0','trace 1','trace 2','trace 3','trace 4','trace 5','trace 6','trace 7','trace 8'
          ,'trace 9','trace 10','trace 11','trace 12','trace 13','trace 14','trace 15','trace 16','trace 17','trace 18'
          ,'trace 19','trace 20','trace 21','trace 22','trace 23'],
          ticktext: ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00'
          ,'09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00'
          ,'19:00','20:00','21:00','22:00','23:00']
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

      var box_plot = document.getElementById('firstOverView')

      box_plot.on('plotly_click', function(data){
        console.log(data)
        console.log('clicked')
        console.log(data.points[0].data.line.color)

        // var pn='',
        //     tn='',
        //     colors=[];
        var tn;
        // for(var i=0; i < data.points.length; i++){
        //   pn = data.points[i].pointNumber;
        //   tn = data.points[i].curveNumber;
        //   colors = data.points[i].data.line.color;
        // }
        // colors[pn] = '#C54C82';
        // data.points[0].data.line.color = rgb(0,0,0);
        tn = data.points[0].curveNumber;
        console.log(tn)
        // tn = data.points[0].data.name;
        var update = {'line':{color: '#000000'}};
        Plotly.restyle('thirdBoxPlot', update,tn);
      });
    }
  }
}
</script>

<style scoped>

</style>