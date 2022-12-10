<template>
  <div style="height: 60vh">
    <div id='secondDetailsAlign' style="height: inherit">
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
//import all_age from '/Users/qiguo/Documents/01 UZH/03 2022 Fall/03 Interactive-Visual Data Analysis/05 Project/IVDA_Project/ivda_03_git/generated_dataset/all_age.json';
import all_gender from '/Users/qiguo/Documents/01 UZH/03 2022 Fall/03 Interactive-Visual Data Analysis/05 Project/IVDA_Project/ivda_03_git/generated_dataset/all_gender.json';
//import times from '/Users/qiguo/Documents/01 UZH/03 2022 Fall/03 Interactive-Visual Data Analysis/05 Project/IVDA_Project/ivda_03_git/generated_dataset/time.json';
//import avg from '/Users/qiguo/Documents/01 UZH/03 2022 Fall/03 Interactive-Visual Data Analysis/05 Project/IVDA_Project/ivda_03_git/generated_dataset/overall-avg.json';


export default {
  name: "DetailsAlign",
  data: () => ({
    //PlotData_AgeCondition: {x: [], y: []},
    //PlotData_AgeControl: {x: [], y: []},
    PlotData_GenderCondition: {x: [], y: []},
    PlotData_GenderControl: {x: [], y: []},
    arrData: ['Age', 'Gender']
  }),
  update: function (){

  },
  mounted() {
    //this.getAgeData()
    this.getGenderData()
  },
  methods: {

    /*
    getAgeData() {

      var ageGroup_length = all_age["age_group"].length
      console.log(ageGroup_length)

      for (var ageGroup_number = 0; ageGroup_number < ageGroup_length; ageGroup_number++) {
        if (all_age["age_group"][ageGroup_number]["type"] === "depress") {
          this.PlotData_AgeCondition.x.push(all_age["age_group"][ageGroup_number]["age"])
          this.PlotData_AgeCondition.y.push(all_age["age_group"][ageGroup_number]["number"])
        } else {
          this.PlotData_AgeControl.x.push(all_age["age_group"][ageGroup_number]["age"])
          this.PlotData_AgeControl.y.push(all_age["age_group"][ageGroup_number]["number"])
        }
      }
      console.log(this.PlotData_AgeCondition)
      console.log(this.PlotData_AgeControl)
      this.drawAgeDetailsAlign()
    },

    drawAgeDetailsAlign() {
      var trace1 = {
        x: this.PlotData_AgeCondition.x,
        y: this.PlotData_AgeCondition.y,
        //mode: 'markers',
        type: 'bar',
        name: 'Depressed',
        marker: {
          color: 'rgb(8,48,107)',
        }
      };

      var trace2 = {
        x: this.PlotData_AgeControl.x,
        y: this.PlotData_AgeControl.y,
        type: 'bar',
        name: 'Non-Depressed',
        marker: {
          color: 'rgb(204, 153, 255)'
        }
      };

      var layout = {
        barmode:'group',
        title: {
          text: '',
          font: {
            family: 'Helvetica',
            size: 18
          },
          xref: 'paper',
          x: 0.05,
        },
        xaxis: {
          tickangle: -45,
          title: {
            text: 'Age Group',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          },
        },
        yaxis: {
          title: {
            text: 'Count',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          }
        }

      }
      var data = [trace1, trace2];
      Plotly.newPlot('secondDetailsAlign', data, layout)
    },*/

    getGenderData() {
      var genderGroup_length = all_gender["gender_group"].length
      console.log(genderGroup_length)

      for (var genderGroup_number = 0; genderGroup_number < genderGroup_length; genderGroup_number++) {
        if (all_gender["gender_group"][genderGroup_number]["type"] === "depress") {
          this.PlotData_GenderCondition.x.push(all_gender["gender_group"][genderGroup_number]["gender"])
          this.PlotData_GenderCondition.y.push(all_gender["gender_group"][genderGroup_number]["number"])
        } else {
          this.PlotData_GenderControl.x.push(all_gender["gender_group"][genderGroup_number]["gender"])
          this.PlotData_GenderControl.y.push(all_gender["gender_group"][genderGroup_number]["number"])
        }
      }
      console.log(this.PlotData_GenderCondition)
      console.log(this.PlotData_GenderControl)
      this.drawGenderDetailsAlign()
    },

    drawGenderDetailsAlign() {
      var trace3 = {
        x: this.PlotData_GenderCondition.x,
        y: this.PlotData_GenderCondition.y,
        //mode: 'markers',
        type: 'bar',
        name: 'Depressed',
        width: 0.2,
        gap: '20%',
        //orientation: 'h',
        text: this.PlotData_GenderCondition.y.map(String),
        textposition: 'auto',
        marker: {
          color: 'rgb(102, 178, 255)',
        }
      };
      var trace4 = {
        x: this.PlotData_GenderControl.x,
        y: this.PlotData_GenderControl.y,
        type: 'bar',
        name: 'Non-Depressed',
        //orientation: 'h',
        width: 0.2,
        gap: '-20%',
        text: this.PlotData_GenderControl.y.map(String),
        textPosition: 'auto',
        marker: {
          color: 'rgb(204, 153, 255)',
        }
      };

      var layout = {
        barmode:'group',

        height: 605,
        width: 500,

        showlegend: true,
        legend: {
          x: 1,
          xanchor: 'right',
          y: 1
        },

        title: {
          text: '',
          font: {
            family: 'Helvetica',
            size: 18
          },
          xref: 'paper',
          x: 0.05,
        },
        xaxis: {
          tickmode: "array",
          tickvals: [1, 2],
          ticktext: ['Female', 'Male'],
          tickangle: -45,
          tickSize: 15,
          title: {
            text: 'Gender',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          },
        },
        yaxis: {
          title: {
            text: 'Count',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          }
        }

      }
      var data = [trace3, trace4];
      Plotly.newPlot('secondDetailsAlign', data, layout)
    }



    /*
    drawDetailsAlign() {
      var trace1 = {
        x: this.PlotData_Condition.x,
        y: this.PlotData_Condition.y,
        //mode: 'markers',
        type: 'bar',
        name: 'Depressed',
        width: 0.3,
        bordercolor: {
          color: 'rgb(102, 178, 255)',
        },
      };
      console.log(trace1)
      var trace2 = {
        x: this.PlotData_Control.x,
        y: this.PlotData_Control.y,
        //mode: 'markers',
        type: 'bar',
        name: 'Non-Depressed',
        width: 0.3,
        bordercolor: {
          color: 'rgb(204, 153, 255)',
        }
      };

      var layout = {
        title: {
          text: '',
          font: {
            family: 'Helvetica',
            size: 18
          },
          xref: 'paper',
          x: 0.05,
        },
        xaxis: {
          title: {
            text: 'Age Group',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          },
        },
        yaxis: {
          title: {
            text: 'Count',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          }
        }

      }
      var data = [trace1, trace2];
      Plotly.newPlot('secondDetailsAlign', data, layout)
    } */
  }
}
</script>


<style scoped>

</style>


<!--
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
      var trace0 = {
        x: ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69"],
        y: [1, 5, 3, 7, 4, 1, 5, 4, 5],
        name: 'Depressed',
        type: 'bar'
      };
      var trace1 = {
        x: ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69"],
        y: [6, 5, 1, 5, 6, 1, 2, 5, 6],
        name: 'Non-Depressed',
        type: 'bar'
      };
      var data = [trace0, trace1];
      Plotly.newPlot('secondDetailsAlign', data);

    }
  }
}
</script>


<style scoped>

</style>
-->
