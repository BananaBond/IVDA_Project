<link rel="stylesheet" type="text/css" href="css/styles.css" />
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js"></script>
<script src="js/script.js"></script>

<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="8" style=" border-collapse :collapse;border-width:0px">
          <v-card-title cols="12" md="8">
            <v-spacer />
            <div class="text-center">
              <h3 class="headline black--text text--accent-2">Overview of Activity Level</h3>
               <!--<div>Some description about the headline</div>-->
            </div>
            <v-spacer />
          </v-card-title>
          <v-card-actions cols="12" md="8">
            <select name="Select" class="selected">
              <option value="details" selected="selected" data-skip="1">Please select here</option>
              <option value="details" data-icon="xx.png" data-html-text="details">Overview</option>
              <option value="average" data-icon="xx.png" data-html-text="average">Average</option>
              </select>
          </v-card-actions>
          <OverView/>
        </v-col>

        <v-col cols="12" md="4" style=" border-collapse :collapse;border-width:0px">
          <v-card-title cols="12" md="4">
            <v-spacer />
            <div class="text-center">
              <h3 class="headline black--text text--accent-2">Detail Exploration</h3>
              <!--<div>Some description about the headline</div>-->
            </div>
            <v-spacer />
          </v-card-title>
          <select name="Select" class="selected">
            <option value="Depressed" selected="selected" data-skip="1">Please select here</option>
            <option value="Depressed" data-icon="xx.png" data-html-text="details">Depressed</option>
            <option value="Non-Depressed" data-icon="xx.png" data-html-text="average">Non-Depressed</option>
          </select>
          <DetailsAlign/>
        </v-col>

        <v-col cols="12" md="12" style=" border-collapse :collapse;border-width:0px">
          <v-card-title cols="12" md="4">
            <v-spacer />
            <div class="text-center">
              <h3 class="headline black--text text--accent-2">Individual Activity Level</h3>
              <!--<div>Some description about the headline</div>-->
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
  }),
}
</script>