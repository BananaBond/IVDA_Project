<template>
  <div style="height: 70vh">
    <div id='secondDetailsAlign' style="height: inherit">
    </div>
  </div>
</template>

<script>
import Plotly, {inherits} from 'plotly.js/dist/plotly';
//import all_age from '../../../../data-preprocess/data/detailgraph/all_age.json';
//import all_gender from '../../../../data-preprocess/data/detailgraph/all_gender.json';
//import after_afftype from '../../../../data-preprocess/data/detailgraph/all_afftype_condition_3.json';
//import after_edu from '../../../../data-preprocess/data/detailgraph/all_edu_condition_3.json';
//import after_marriage from '../../../../data-preprocess/data/detailgraph/all_marriage_condition_3.json';
//import after_work from '../../../../data-preprocess/data/detailgraph/all_work_condition_3.json';
import after_age from '../../../../data-preprocess/data/detailgraph/all_age_condition_3.json';
//import after_gender from '../../../../data-preprocess/data/detailgraph/all_gender_condition_3.json';


export default {
  name: "DetailsAlign",
  data: () => ({
    PlotData_AgeCondition: {x: [], y: []},
    PlotData_AgeControl: {x: [], y: []},
    PlotData_GenderCondition: {x: [], y: []},
    PlotData_GenderControl: {x: [], y: []},
    PlotData_YequalX: {x: [], y: []},
    PlotData_Afftype1: {x: [], y: []},
    PlotData_Afftype2: {x: [], y: []},
    PlotData_Afftype3: {x: [], y: []},
    PlotData_Afftype_3: {x: [], y: []},
    PlotData_Edu_6_10: {x: [], y: []},
    PlotData_Edu_11_15: {x: [], y: []},
    PlotData_Edu_3: {x: [], y: []},
    PlotData_Marriage_Y: {x: [], y: []},
    PlotData_Marriage_N: {x: [], y: []},
    PlotData_Marriage_3: {x: [], y: []},
    PlotData_Work_Y: {x: [], y: []},
    PlotData_Work_N: {x: [], y: []},
    PlotData_Work_3: {x: [], y: []},
    PlotData_AfterAgeCondition: {x: [], y: []},
    PlotData_AfterAgeControl: {x: [], y: []},
    PlotData_AfterAge_3: {x: [], y: []},
    PlotData_AfterGenderCondition: {x: [], y: []},
    PlotData_AfterGenderControl: {x: [], y: []},
    PlotData_AfterGender_3: {x: [], y: []},

    //arrData: ['Age', 'Gender']
  }),
  update: function (){

  },
  mounted() {
    //this.getAgeData()
    //this.getGenderData()
    //this.getAfftypeData()
    //this.getEduData()
    //this.getMarriageData()
    //this.getWorkData()
    this.getAfterAgeData()
    //this.getAfterGenderData()
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
          color: 'rgb(211,59,44)',
        }
      };

      var trace2 = {
        x: this.PlotData_AgeControl.x,
        y: this.PlotData_AgeControl.y,
        type: 'bar',
        name: 'Non-Depressed',
        marker: {
          color: 'rgb(37,98,166)'
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
        legend: {
          "orientation": "h",
          x: 0,
          y: 1.2,
          traceorder: 'normal',
          font: {
            family: 'sans-serif',
            size: 12,
            color: '#000'
          },
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
            text: 'The Number of People',
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

        getAfterAgeData() {

          var ageGroup_length = after_age["age_group"].length
          console.log(ageGroup_length)

          for (var ageGroup_number = 0; ageGroup_number < ageGroup_length; ageGroup_number++) {
            if (after_age["age_group"][ageGroup_number]["type"] === "depress") {
              this.PlotData_AgeCondition.x.push(after_age["age_group"][ageGroup_number]["age"])
              this.PlotData_AgeCondition.y.push(after_age["age_group"][ageGroup_number]["number"])
            } else {
              this.PlotData_AgeControl.x.push(after_age["age_group"][ageGroup_number]["age"])
              this.PlotData_AgeControl.y.push(after_age["age_group"][ageGroup_number]["number"])
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
              color: 'rgb(211,59,44)',
            }
          };

          var trace2 = {
            x: this.PlotData_AgeControl.x,
            y: this.PlotData_AgeControl.y,
            type: 'bar',
            name: 'Non-Depressed',
            marker: {
              color: 'rgb(37,98,166)'
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
            legend: {
              "orientation": "h",
              x: 0,
              y: 1.2,
              traceorder: 'normal',
              font: {
                family: 'sans-serif',
                size: 12,
                color: '#000'
              },
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
                text: 'The Number of People',
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
        },

    /*
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
          color: 'rgb(102, 178,   255)',
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
        margin: {
          r: 40,
          t: 20,
          pad: 5
        },
        barmode:'group',

        height: inherits,
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
    },*/

/*
    getAfftypeData() {
      var afftypeGroup_length = after_afftype["afftype"].length
      console.log(afftypeGroup_length)

      for (var afftypeGroup_number = 0; afftypeGroup_number < afftypeGroup_length; afftypeGroup_number++) {
        //this.PlotData_Afftype.id.push(after_afftype["afftype"][afftypeGroup_number]["number"])
        if (after_afftype["afftype"][afftypeGroup_number]["number"] === 'condition_3') {
          this.PlotData_Afftype_3.x.push(after_afftype["afftype"][afftypeGroup_number]["madrs1"])
          this.PlotData_Afftype_3.y.push(after_afftype["afftype"][afftypeGroup_number]["madrs2"])
        } else if (after_afftype["afftype"][afftypeGroup_number]["afftype"] === 1.0) {
          this.PlotData_Afftype1.x.push(after_afftype["afftype"][afftypeGroup_number]["madrs1"])
          this.PlotData_Afftype1.y.push(after_afftype["afftype"][afftypeGroup_number]["madrs2"])
        } else if (after_afftype["afftype"][afftypeGroup_number]["afftype"] === 2.0){
          this.PlotData_Afftype2.x.push(after_afftype["afftype"][afftypeGroup_number]["madrs1"])
          this.PlotData_Afftype2.y.push(after_afftype["afftype"][afftypeGroup_number]["madrs2"])
        } else if (after_afftype["afftype"][afftypeGroup_number]["afftype"] === 3.0){
          this.PlotData_Afftype3.x.push(after_afftype["afftype"][afftypeGroup_number]["madrs1"])
          this.PlotData_Afftype3.y.push(after_afftype["afftype"][afftypeGroup_number]["madrs2"])
        }
        console.log(this.PlotData_Afftype2.x)

      }

      for (var i = 10; i < 31; i += 1) {
        this.PlotData_YequalX.x.push(i);
        this.PlotData_YequalX.y.push(i);
      }

      //console.log(this.PlotData_Afftype.type)
      this.drawAfftypeDetailsAlign()
    },

    drawAfftypeDetailsAlign() {
      var trace5 = {
        x: this.PlotData_Afftype1.x,
        y: this.PlotData_Afftype1.y,
        //mode: 'markers',
        mode: 'markers',
        type: 'scatter',
        name: 'Bipolar II',
        //width: 0.2,
        //orientation: 'h',
        //text: this.PlotData_GenderCondition.y.map(String),
        //textposition: 'auto',
        marker: {
          color: 'rgba(37,90,166, 0.6)',
          size: 15,
        }
      };
      var trace6 = {
        x: this.PlotData_Afftype2.x,
        y: this.PlotData_Afftype2.y,
        //mode: 'markers',
        mode: 'markers',
        type: 'scatter',
        name: 'Unipolar Depressive',
        //width: 0.2,
        //orientation: 'h',
        //text: this.PlotData_GenderCondition.y.map(String),
        //textposition: 'auto',
        marker: {
          color: 'rgb(239,137,51)',
          size: 15,
        },
        showlegend: true,
      };
      var trace7 = {
        x: this.PlotData_Afftype3.x,
        y: this.PlotData_Afftype3.y,
        //mode: 'markers',
        mode: 'markers',
        type: 'scatter',
        name: 'Bipolar I',
        //width: 0.2,
        //orientation: 'h',
        //text: this.PlotData_GenderCondition.y.map(String),
        //textposition: 'auto',
        marker: {
          color: 'rgb(23, 60, 159)',
          size: 15,
        },
        showlegend: true,
      };

      var trace8 = {
        x: this.PlotData_Afftype_3.x,
        y: this.PlotData_Afftype_3.y,
        //mode: 'markers',
        mode: 'markers',
        type: 'scatter',
        name: 'Selected',
        //width: 0.2,
        //orientation: 'h',
        //text: this.PlotData_GenderCondition.y.map(String),
        //textposition: 'auto',
        marker: {
          color: 'rgb(239,137,51)',
          size: 15,
          line: {
            color: 'rgb(129, 183, 78)',
            width: 3
          },
        },
        showlegend: true,
      };

      var trace9 = {
        x: this.PlotData_YequalX.x,
        y: this.PlotData_YequalX.y,
        mode: 'lines',
        //name: 'Before MADRS = After MADRS',
        line: {
          dash: 'dot',
          width: 1
        },
        showlegend: false,
      };


      var layout = {
        barmode:'group',

        height: inherits,
        width: 500,
        legend: {
          "orientation": "h",
          x: 0,
          y: 1.2,
          traceorder: 'normal',
          font: {
            family: 'sans-serif',
            size: 12,
            color: '#000'
          },

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
          //tickmode: "array",
          //tickvals: [1, 2],
          //ticktext: ['Female', 'Male'],
          tickangle: -45,
          tickSize: 15,
          title: {
            text: 'MADRS before the Measurement',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          },
        },
        yaxis: {
          title: {
            text: 'MADRS after the Measurement',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          }
        }

      }
      var data = [trace5, trace6, trace7, trace8, trace9];
      Plotly.newPlot('secondDetailsAlign', data, layout)
    },*/


///////////////////////////////
    /*
    getEduData() {
  var eduGroup_length = after_edu["edu"].length
  console.log(eduGroup_length)

  for (var eduGroup_number = 0; eduGroup_number < eduGroup_length; eduGroup_number++) {
    //this.PlotData_Afftype.id.push(after_afftype["afftype"][afftypeGroup_number]["number"])
    if (after_edu["edu"][eduGroup_number]["number"] === 'condition_3') {
      this.PlotData_Edu_3.x.push(after_edu["edu"][eduGroup_number]["madrs1"])
      this.PlotData_Edu_3.y.push(after_edu["edu"][eduGroup_number]["madrs2"])
    } else if (after_edu["edu"][eduGroup_number]["edu"] === "6-10") {
      this.PlotData_Edu_6_10.x.push(after_edu["edu"][eduGroup_number]["madrs1"])
      this.PlotData_Edu_6_10.y.push(after_edu["edu"][eduGroup_number]["madrs2"])
    } else if (after_edu["edu"][eduGroup_number]["edu"] === "11-15"){
      this.PlotData_Edu_11_15.x.push(after_edu["edu"][eduGroup_number]["madrs1"])
      this.PlotData_Edu_11_15.y.push(after_edu["edu"][eduGroup_number]["madrs2"])
    }
    console.log(this.PlotData_Edu_3.x)

  }

  for (var i = 10; i < 31; i += 1) {
    this.PlotData_YequalX.x.push(i);
    this.PlotData_YequalX.y.push(i);
  }

  this.drawEduDetailsAlign()
},

    drawEduDetailsAlign() {
  var trace5 = {
    x: this.PlotData_Edu_6_10.x,
    y: this.PlotData_Edu_6_10.y,
    //mode: 'markers',
    mode: 'markers',
    type: 'scatter',
    name: '6-10',
    //width: 0.2,
    //orientation: 'h',
    //text: this.PlotData_GenderCondition.y.map(String),
    //textposition: 'auto',
    marker: {
      color: 'rgba(37,90,166, 0.6)',
      size: 15,
    }
  };
  var trace6 = {
    x: this.PlotData_Edu_11_15.x,
    y: this.PlotData_Edu_11_15.y,
    //mode: 'markers',
    mode: 'markers',
    type: 'scatter',
    name: '11-15',
    //width: 0.2,
    //orientation: 'h',
    //text: this.PlotData_GenderCondition.y.map(String),
    //textposition: 'auto',
    marker: {
      color: 'rgb(239,137,51)',
      size: 15,
    },
    showlegend: true,
  };

  var trace8 = {
    x: this.PlotData_Edu_3.x,
    y: this.PlotData_Edu_3.y,
    //mode: 'markers',
    mode: 'markers',
    type: 'scatter',
    name: 'Selected',
    //width: 0.2,
    //orientation: 'h',
    //text: this.PlotData_GenderCondition.y.map(String),
    //textposition: 'auto',
    marker: {
      color: 'rgb(37,90,166, 0.6)',
      size: 15,
      line: {
        color: 'rgb(129, 183, 78)',
        width: 3
      },
    },
    showlegend: true,
  };

  var trace9 = {
    x: this.PlotData_YequalX.x,
    y: this.PlotData_YequalX.y,
    mode: 'lines',
    //name: 'Before MADRS = After MADRS',
    line: {
      dash: 'dot',
      width: 1
    },
    showlegend: false,
  };


  var layout = {
    barmode:'group',

    height: inherits,
    width: 500,
    legend: {
      "orientation": "h",
      x: 0,
      y: 1.2,
      traceorder: 'normal',
      font: {
        family: 'sans-serif',
        size: 12,
        color: '#000'
      },

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
      //tickmode: "array",
      //tickvals: [1, 2],
      //ticktext: ['Female', 'Male'],
      tickangle: -45,
      tickSize: 15,
      title: {
        text: 'MADRS before the Measurement',
        font: {
          family: 'Helvetica',
          size: 16,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
      title: {
        text: 'MADRS after the Measurement',
        font: {
          family: 'Helvetica',
          size: 16,
          color: '#7f7f7f'
        }
      }
    }

  }
  var data = [trace5, trace6, trace8, trace9];
  Plotly.newPlot('secondDetailsAlign', data, layout)
},*/

//////////////////////////////////////
/*
    getMarriageData() {
      var marriageGroup_length = after_marriage["marriage"].length
      console.log(marriageGroup_length)

      for (var marriageGroup_number = 0; marriageGroup_number < marriageGroup_length; marriageGroup_number++) {
        //this.PlotData_Afftype.id.push(after_afftype["afftype"][afftypeGroup_number]["number"])
        if (after_marriage["marriage"][marriageGroup_number]["number"] === 'condition_3') {
          this.PlotData_Marriage_3.x.push(after_marriage["marriage"][marriageGroup_number]["madrs1"])
          this.PlotData_Marriage_3.y.push(after_marriage["marriage"][marriageGroup_number]["madrs2"])
        } else if (after_marriage["marriage"][marriageGroup_number]["marriage"] === 1.0) {
          this.PlotData_Marriage_Y.x.push(after_marriage["marriage"][marriageGroup_number]["madrs1"])
          this.PlotData_Marriage_Y.y.push(after_marriage["marriage"][marriageGroup_number]["madrs2"])
        } else if (after_marriage["marriage"][marriageGroup_number]["marriage"] === 2.0){
          this.PlotData_Marriage_N.x.push(after_marriage["marriage"][marriageGroup_number]["madrs1"])
          this.PlotData_Marriage_N.y.push(after_marriage["marriage"][marriageGroup_number]["madrs2"])
        }
        console.log(this.PlotData_Marriage_3.x)

      }

      for (var i = 10; i < 31; i += 1) {
        this.PlotData_YequalX.x.push(i);
        this.PlotData_YequalX.y.push(i);
      }
      this.drawMarriageDetailsAlign()
    },

    drawMarriageDetailsAlign() {
      var trace5 = {
        x: this.PlotData_Marriage_Y.x,
        y: this.PlotData_Marriage_Y.y,
        mode: 'markers',
        type: 'scatter',
        name: 'Married or Cohabiting',
        marker: {
          color: 'rgba(37,90,166, 0.6)',
          size: 15,
        }
      };
      var trace6 = {
        x: this.PlotData_Marriage_N.x,
        y: this.PlotData_Marriage_N.y,
        mode: 'markers',
        type: 'scatter',
        name: 'Single',
        marker: {
          color: 'rgb(239,137,51)',
          size: 15,
        },
        showlegend: true,
      };

      var trace8 = {
        x: this.PlotData_Marriage_3.x,
        y: this.PlotData_Marriage_3.y,
        mode: 'markers',
        type: 'scatter',
        name: 'Selected',
        marker: {
          color: 'rgb(239,137,51)',
          size: 15,
          line: {
            color: 'rgb(129, 183, 78)',
            width: 3
          },
        },
        showlegend: true,
      };

      var trace9 = {
        x: this.PlotData_YequalX.x,
        y: this.PlotData_YequalX.y,
        mode: 'lines',
        line: {
          dash: 'dot',
          width: 1
        },
        showlegend: false,
      };


      var layout = {
        barmode:'group',

        height: inherits,
        width: 500,
        legend: {
          "orientation": "h",
          x: 0,
          y: 1.2,
          traceorder: 'normal',
          font: {
            family: 'sans-serif',
            size: 12,
            color: '#000'
          },

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
          tickangle: -45,
          tickSize: 15,
          title: {
            text: 'MADRS before the Measurement',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          },
        },
        yaxis: {
          title: {
            text: 'MADRS after the Measurement',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          }
        }

      }
      var data = [trace5, trace6, trace8, trace9];
      Plotly.newPlot('secondDetailsAlign', data, layout)
    },*/
    ////////////////////////////////

    /*
    getWorkData() {
      var workGroup_length = after_work["work"].length
      console.log(workGroup_length)

      for (var workGroup_number = 0; workGroup_number < workGroup_length; workGroup_number++) {
        //this.PlotData_Afftype.id.push(after_afftype["afftype"][afftypeGroup_number]["number"])
        if (after_work["work"][workGroup_number]["number"] === 'condition_3') {
          this.PlotData_Work_3.x.push(after_work["work"][workGroup_number]["madrs1"])
          this.PlotData_Work_3.y.push(after_work["work"][workGroup_number]["madrs2"])
        } else if (after_work["work"][workGroup_number]["work"] === 1.0) {
          this.PlotData_Work_Y.x.push(after_work["work"][workGroup_number]["madrs1"])
          this.PlotData_Work_Y.y.push(after_work["work"][workGroup_number]["madrs2"])
        } else if (after_work["work"][workGroup_number]["work"] === 2.0){
          this.PlotData_Work_N.x.push(after_work["work"][workGroup_number]["madrs1"])
          this.PlotData_Work_N.y.push(after_work["work"][workGroup_number]["madrs2"])
        }
        console.log(this.PlotData_Work_3.x)

      }

      for (var i = 10; i < 31; i += 1) {
        this.PlotData_YequalX.x.push(i);
        this.PlotData_YequalX.y.push(i);
      }
      this.drawWorkDetailsAlign()
    },

    drawWorkDetailsAlign() {
      var trace5 = {
        x: this.PlotData_Work_Y.x,
        y: this.PlotData_Work_Y.y,
        mode: 'markers',
        type: 'scatter',
        name: 'Working or Studying',
        marker: {
          color: 'rgba(37,90,166, 0.6)',
          size: 15,
        }
      };
      var trace6 = {
        x: this.PlotData_Work_N.x,
        y: this.PlotData_Work_N.y,
        mode: 'markers',
        type: 'scatter',
        name: 'Unemployed/Sick Leave/Pension',
        marker: {
          color: 'rgb(239,137,51)',
          size: 15,
        },
        showlegend: true,
      };

      var trace8 = {
        x: this.PlotData_Work_3.x,
        y: this.PlotData_Work_3.y,
        mode: 'markers',
        type: 'scatter',
        name: 'Selected',
        marker: {
          color: 'rgb(239,137,51)',
          size: 15,
          line: {
            color: 'rgb(129, 183, 78)',
            width: 3
          },
        },
        showlegend: true,
      };

      var trace9 = {
        x: this.PlotData_YequalX.x,
        y: this.PlotData_YequalX.y,
        mode: 'lines',
        line: {
          dash: 'dot',
          width: 1
        },
        showlegend: false,
      };


      var layout = {
        barmode:'group',

        height: inherits,
        width: 500,
        legend: {
          "orientation": "h",
          x: 0,
          y: 1.2,
          traceorder: 'normal',
          font: {
            family: 'sans-serif',
            size: 12,
            color: '#000'
          },

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
          tickangle: -45,
          tickSize: 15,
          title: {
            text: 'MADRS before the Measurement',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          },
        },
        yaxis: {
          title: {
            text: 'MADRS after the Measurement',
            font: {
              family: 'Helvetica',
              size: 16,
              color: '#7f7f7f'
            }
          }
        }

      }
      var data = [trace5, trace6, trace8, trace9];
      Plotly.newPlot('secondDetailsAlign', data, layout)
    },
    */

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
