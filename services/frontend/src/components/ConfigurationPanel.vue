<link rel="stylesheet" type="text/css" href="css/styles.css" />
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js"></script>
<script src="js/script.js"></script>

<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="8" style=" border-collapse :collapse;border-width:0px;background-color: rgb(207, 223, 239);padding-bottom: 0%;padding-top:0%;">
          <v-container fluid> 
          <v-row>
          <v-col cols="12" md="10" style=" border-collapse :collapse;border-width:0px;padding-left: 15%;padding-bottom: 0%;">
          <v-card-title cols="12" md="10" style="padding-top:0px;padding-bottom:0%;">
            <v-spacer />
            <div class="text-center">
              <h3 class="headline black--text text--accent-2"><b>OVERVIEW</b></h3>
               <!--<div>Some description about the headline</div>-->
            </div>
            <v-spacer />
          </v-card-title>
          </v-col>
          <v-col cols="12" md="2" style=" border-collapse :collapse;border-width:0px;padding-left: 6%;padding-bottom: 0%;">
          <v-card-actions cols="12" md="2">
          <label for="toggle_button" style="">
              <input type="checkbox" id="toggle_button">
              <span> Average</span>
          </label>
          </v-card-actions>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="12" style=" border-collapse :collapse;border-width:0px;padding-top: 0%;padding-bottom: 0%;">
            <v-spacer />
            <div>
              <div class="text-center">
              Select start time (t0) for pattern recognition
            </div>
            </div>
            <v-spacer />
        </v-col>
        </v-row>
        </v-container>
          <OverView/>
        </v-col>

        <v-col cols="12" md="4" style=" border-collapse :collapse;border-width:0px; background-color: rgb(204, 202, 240);">
          <v-card-title cols="12" md="4" style="padding-top:0px;padding-bottom:2%;">
            <v-spacer />
            <div class="text-center">
              <h3 class="headline black--text text--accent-2"><b>DETAILS EXPLORATION</b></h3>
              <!--<div>Some description about the headline</div>-->
            </div>
            <v-spacer />
          </v-card-title>

          Display Attributes:
          <select name="attributes">
            <option value="0"> Age</option>
            <option value="1"> Gender</option>
            <!--<option value="2"> Depression Type</option>
            <option value="3"> Education Years</option>
            <option value="4"> Marital Status</option>
            <option value="5"> Work Status</option>-->
          </select>

          <DetailsAlign/>
        </v-col>
      </v-row>

      <v-row>

        <v-col cols="12" md="12" style=" border-collapse :collapse;border-width:0px;">
          <v-card-title cols="12" md="12">
            <v-spacer />
            <div class="text-center">
              <h3 class="headline black--text text--accent-2">Activity level distribution for <b>CONDITION 3</b></h3>
            </div>
            <v-spacer />
          </v-card-title>
          <BoxPlot/>
        </v-col>

      </v-row>
    </v-container>
  </div>
</template>

<script>
import OverView from './OverView';
import DetailsAlign from './DetailsAlign';
import BoxPlot from './BoxPlot';
export default {
  components: {OverView, DetailsAlign, BoxPlot},
  data: () => ({
    OverView:0,
    DetailsAlign:0,
    BoxPlot:0
  }),

}
</script>