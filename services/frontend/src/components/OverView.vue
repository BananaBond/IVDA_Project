<template>
  <div style="height: 80vh">
    <div id='firstOverView' style="height: inherit">
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
// import csv from '/Users/shivangi/Downloads/generated_dataset/depressed.csv';
import depressed from '../../../../data-preprocess/data/overview/depressed.json';
import non_depressed from '../../../../data-preprocess/data/overview/non-depressed.json';
import times from '../../../../data-preprocess/data/overview/time.json';
import avg from '../../../../data-preprocess/data/overview/overall-avg.json';

export default {
  name: "OverView",
  data: () => ({
  }),
  mounted() {
    this.drawOverView()
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
    getActivityLevels(times){
      var activity_level_list = []
      times.forEach(time => {
        console.log(time)
        if (time == "00:00" || time == "01:00" || time == "02:00" ||time == "03:00" ||time == "04:00" ||time == "05:00" ||time == "6:00" || time == "23:00") {
          activity_level_list.push(Math.floor(Math.random() * (10 - 0 + 1)) + 0);
        }
        else{
          activity_level_list.push(Math.floor(Math.random() * (1000 - 15 + 1)) + 15);
        }
      });
      return activity_level_list
    },
    processData(allRows) {
        console.log(allRows);

        var control = []
        var condition = []

        for (var i=1; i<=32; i++){
            control[i] = {
              x: times["time"],
              y: []
            }
          }

        for (var j=1; j<=23; j++){
          condition[j] = {
            x: times["time"],
            y: []
          }
        }

        for (var num=0; num<allRows.length; num++) {
          var row = allRows[num];
          for (var control_number=1; control_number<=32; control_number++){
            control[control_number].x.push( row['time'])
            control[control_number].y.push( row['control_'+control_number])
          }
          for (var cond_number=1; control_number<=23; cond_number++){
            condition[cond_number].x.push( row['time'])
            condition[cond_number].y.push( row['condition_'+cond_number])
          }
        }

        var people_data = [condition + control]

        Plotly.newPlot('firstOverview', people_data,
          {title: 'Plotting CSV data from AJAX call'});

      },
    drawOverView() {
        var control = []
        var condition = []

      // var mydata = Plotly.d3.csv("/Users/shivangi/Downloads/generated_dataset/depressed.csv", function(data){
          // console.log(allRows);
      
      var depressed_length = depressed["files"].length
        
      for (var cond_number=0; cond_number<depressed_length; cond_number++){
        var index = parseInt(depressed["files"][cond_number]["file"].split("_")[1])
        console.log(index)
        condition[index-1] = {
          x: times["time"],
          y: depressed["files"][cond_number]["activity_level"],
          mode: 'lines',
          type: 'scatter',
          hovertemplate: '%{x}' + ', %{y:.0f}',
          line: {
            color: 'rgb(102, 178, 255)',
            width: 1
          },
          name: "condition " + index,
          showlegend: false
        }
      }

      var non_depressed_length = non_depressed["files"].length

      for (var control_number=0; control_number<non_depressed_length; control_number++){
        var ind = parseInt(non_depressed["files"][control_number]["file"].split("_")[1])
        console.log(ind)
        control[ind-1] = {
          x: times["time"],
          y: non_depressed["files"][control_number]["activity_level"],
          mode: 'lines',
          type: 'scatter',
          hovertemplate: '%{x}' + ', %{y:.0f}',
          hoverinfo: "control "+ ind,
          line: {
            color: 'rgb(204, 153, 255)',
            width: 1
          },
          name: "control " + ind,
          showlegend: false
        }
      }
      
      var data = []
      data = data.concat(control)
      data = data.concat(condition)

      data.push({
        x: times["time"],
        y: avg["depressed"]["activity_level"],
        mode: 'lines',
        type: 'scatter',
        hovertemplate: '%{x}' + ', %{y:.0f}',
        line: {
          color: 'rgb(0, 102, 204)',
          width: 3
        },
        name: "control average",
        showlegend: false
      })

      data.push({
        x: times["time"],
        y: avg["non-depressed"]["activity_level"],
        mode: 'lines',
        type: 'scatter',
        hovertemplate: '%{x}' + ', %{y:.0f}',
        line: {
          color: 'rgb(76, 0, 153)',
          width: 3
        },
        name: "control average",
        showlegend: false
      })

      console.log('data length', data)


      var layout = {
          title: {
            text:'',
            font: {
            family: 'Helvetica',
            size: 18
            },
          xref: 'paper',
          x: 0.05,
      },
      xaxis: {
          title: {
          text: 'Time (hours)',
          font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
          }},
          tickvals:['00:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00','07:00:00','08:00:00'
          ,'09:00:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:00:00','16:00:00','17:00:00','18:00:00'
          ,'19:00:00','20:00:00','21:00:00','22:00:00','23:00:00'],
          ticktext: ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00'
          ,'09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00'
          ,'19:00','20:00','21:00','22:00','23:00']
      },
      yaxis: {
          title: {
          text: 'Activity level',
          font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
          }
          }
      }
      };

      Plotly.newPlot('firstOverView', data, layout );
      
      
    }

      // var people_data = [condition + control]

      // return people_data
          }
      // );
      
      
             
  }

</script>

<style scoped>

</style>