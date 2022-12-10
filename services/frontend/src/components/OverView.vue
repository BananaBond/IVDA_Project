<template>
  <div style="height: 70vh">
    <div id='firstOverView' style="height: inherit">
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
// import depressed from '../../../../data-preprocess/data/overview/depressed.json';
// import non_depressed from '../../../../data-preprocess/data/overview/non-depressed.json';
import depressed from '../../../../data-preprocess/data/overview/shifted/depressed.json';
import non_depressed from '../../../../data-preprocess/data/overview/shifted/non-depressed.json';
// import times from '../../../../data-preprocess/data/overview/time.json';
import times from '../../../../data-preprocess/data/overview/shifted/shifted_time.json';
// import avg from '../../../../data-preprocess/data/overview/overall-avg.json';


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


      //UNCOMMENT FOR NORMAL GRAPH
        
      // for (var cond_number=0; cond_number<depressed_length; cond_number++){
      //   var index = parseInt(depressed["files"][cond_number]["file"].split("_")[1])
      //   console.log(index)
      //   condition[index-1] = {
      //     x: times["time"],
      //     y: depressed["files"][cond_number]["activity_level"],
      //     mode: 'lines',
      //     type: 'scatter',
      //     hovertemplate: '%{x}' + ', %{y:.0f}',
      //     line: {
      //       color: 'rgba(211,59,44, 0.6)',
      //       width: 1
      //     },
      //     name: "condition " + index,
      //     showlegend: false
      //   }
      // }

      for (var cond_number=0; cond_number<depressed_length; cond_number++){
        var index = parseInt(depressed["files"][cond_number]["file"].split("_")[1])
        if (index == 1  || index == 11 || index == 15 || index == 18 || index == 19 || index == 21 || index == 5 || 
        index == 6 || index == 7 || index == 8){
          condition[index-1] = {
            x: times["time"],
            y: depressed["files"][cond_number]["activity_level"],
            mode: 'lines',
            type: 'scatter',
            hovertemplate: '%{x}' + ', %{y:.0f}',
            line: {
              color: 'rgba(129, 183, 78,0.8)',
              width: 2
            },
            name: "condition " + index,
            showlegend: false
          }
        }
        else if (index == 2){
          condition[index-1] = {
            x: times["time"],
            y: depressed["files"][cond_number]["activity_level"],
            mode: 'lines',
            type: 'scatter',
            hovertemplate: '%{x}' + ', %{y:.0f}',
            line: {
              color: 'rgb(0,100,0, 0.8)',
              width: 4
            },
            name: "condition " + index,
            showlegend: false
          }
        }
        else{
          condition[index-1] = {
            x: times["time"],
            y: depressed["files"][cond_number]["activity_level"],
            mode: 'lines',
            type: 'scatter',
            hovertemplate: '%{x}' + ', %{y:.0f}',
            line: {
              color: 'rgba(169,169,169,0.5)',
              width: 1
            },
            name: "condition " + index,
            showlegend: false
          }
        }
    }

      var non_depressed_length = non_depressed["files"].length

      //UNCOMMENT FOR NORMAL GRAPH
      // for (var control_number=0; control_number<non_depressed_length; control_number++){
      //   var ind = parseInt(non_depressed["files"][control_number]["file"].split("_")[1])
      //   console.log(ind)
      //   control[ind-1] = {
      //     x: times["time"],
      //     y: non_depressed["files"][control_number]["activity_level"],
      //     mode: 'lines',
      //     type: 'scatter',
      //     hovertemplate: '%{x}' + ', %{y:.0f}',
      //     hoverinfo: "control "+ ind,
      //     line: {
      //       color: 'rgba(37,98,166, 0.6)',
      //       width: 1
      //     },
      //     name: "control " + ind,
      //     showlegend: false
      //   }
      // }
      
      for (var control_number=0; control_number<non_depressed_length; control_number++){
        var ind = parseInt(non_depressed["files"][control_number]["file"].split("_")[1])
        console.log(ind)
        if (index == 0  || index == 2 || index == 11){
          control[ind-1] = {
            x: times["time"],
            y: non_depressed["files"][control_number]["activity_level"],
            mode: 'lines',
            type: 'scatter',
            hovertemplate: '%{x}' + ', %{y:.0f}',
            hoverinfo: "control "+ ind,
            line: {
              color: 'rgba(129, 183, 78, 0.8)',
              width: 2
            },
            name: "control " + ind,
            showlegend: false
          }
        }
        else{
          control[ind-1] = {
            x: times["time"],
            y: non_depressed["files"][control_number]["activity_level"],
            mode: 'lines',
            type: 'scatter',
            hovertemplate: '%{x}' + ', %{y:.0f}',
            hoverinfo: "control "+ ind,
            line: {
              color: 'rgba(169,169,169,0.5)',
              width: 1
            },
            name: "control " + ind,
            showlegend: false
          }
        }
      }
      
      var data = []
      data = data.concat(control)
      data = data.concat(condition)

      //UNCOMMENT FOR AVERAGE
      // import avg from '../../../../data-preprocess/data/overview/overall-avg.json';
      // data.push({
      //   x: times["time"],
      //   y: avg["depressed"]["activity_level"],
      //   mode: 'lines',
      //   type: 'scatter',
      //   hovertemplate: '%{x}' + ', %{y:.0f}',
      //   line: {
      //     color: 'rgb(211,59,44)',
      //     width: 3
      //   },
      //   name: "control average",
      //   showlegend: false
      // })

      // data.push({
      //   x: times["time"],
      //   y: avg["non-depressed"]["activity_level"],
      //   mode: 'lines',
      //   type: 'scatter',
      //   hovertemplate: '%{x}' + ', %{y:.0f}',
      //   line: {
      //     color: 'rgb(37,98,166)',
      //     width: 3
      //   },
      //   name: "control average",
      //   showlegend: false
      // })

      console.log('data length', data)


      var layout = {
        margin: {
          r: 20,
          t: 20,
          pad: 5
        },
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
          // tickvals:['00:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00','07:00:00','08:00:00'
          // ,'09:00:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:00:00','16:00:00','17:00:00','18:00:00'
          // ,'19:00:00','20:00:00','21:00:00','22:00:00','23:00:00'],
          tickvals:['22:00:00','23:00:00', '00:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00','07:00:00','08:00:00'
          ,'09:00:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:00:00','16:00:00','17:00:00','18:00:00'
          ,'19:00:00','20:00:00','21:00:00'],
          // ticktext: ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00'
          // ,'09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00'
          // ,'19:00','20:00','21:00','22:00','23:00']
          ticktext: ['22:00','23:00','00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00'
          ,'09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00'
          ,'19:00','20:00','21:00']
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
      // shapes: [
      //   {
      //     x0: '22:00:00',
      //     x1: '22:00:00',
      //     y0: 0,
      //     y1: 700,
      //     type: 'line',
      //     line: {
      //       color: 'rgb(37,98,166)',
      //       dash: 'dot'
      //     },
      //     showlegend: false
      //   }
      // ]
      };

      Plotly.newPlot('firstOverView', data, layout );


      var myPlot = document.getElementById('firstOverView')

      myPlot.on('plotly_click', function(data){
        console.log(data)
        console.log('clicked')
        console.log(data.points[0].data.line.color)

        // var pn='',
        //     tn='',
        //     colors=[];
        if (data.points[0].data.line.color != 'rgb(129, 183, 78)')
        {
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
          var update_ = {'line': {color: 'rgba(169,169,169,0.5)', width: 1}}
          for (let i = 0; i < 55; i++) {
            if (i != 34){
              Plotly.restyle('firstOverView', update_,i);
            }
          }
          var update = {'line':{color: 'rgb(129, 183, 78)', width: 3}};
          Plotly.restyle('firstOverView', update,tn);
        }
        else{
          console.log('hi')
          console.log(data.points[0].x)
          var tn_ = data.points[0].x;
          var update__ = {'mode': "markers"}
          Plotly.restyle('firstOverView', update__,tn_);
        }
      });



      // myPlot.on('plotly_click', function(data){
      //   console.log(data)
      //   var pn='';
      //   var tn='';
      //   var colors=[];
      //   var line_colors = [];
      //   for(var i=0; i < data.points.length; i++){
      //     pn = data.points[i].pointNumber;
      //     tn = data.points[i].curveNumber;
      //     colors = data.points[i].data.marker.color;
      //     line_colors = data.points[i].data.line.color;
      //   }
      //   colors[tn] = '#ffffff';
      //   var update = {'line':{color: line_colors, size:16}};
      //   Plotly.restyle('myDiv', update,[pn]);
      // });
      
      
    }

      // var people_data = [condition + control]

      // return people_data
          }
      // );
      
      
             
  }

</script>

<style scoped>

</style>