<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="12">
          <v-card>
            Parameters go here
          </v-card>
        </v-col>

        <v-col cols="12" md="8">
          <v-card>
            Overview
          </v-card>
          <OverView/>
        </v-col>

        <!-- <v-col cols="12" md="8">
          <v-card-title cols="12" md="8">
            <v-spacer />
            <div class="text-center">
              <h3 class="headline Black--text text--accent-2">Overview</h3>
               <div>Some description about the headline</div>
            </div>
            <v-spacer />
            <v-card-actions>
              <v-spacer />
              <v-btn color="lightblue">Depressed</v-btn>
              <v-spacer />
              <v-spacer />
              <v-btn color="lightblue">Non-Depressed</v-btn>
              <v-spacer />
            </v-card-actions>
          </v-card-title>
          <OverView/>
        </v-col>-->



        <v-col cols="12" md="4">
          <v-card>
            Details Align
          </v-card>
          <DetailsAlign/>
        </v-col>

        <v-col cols="12" md="12">
          <v-card>
            BoxPlot goes here
          </v-card>
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