<template>
  <div id="welcome">
    <div class="search-container">
      <div class="search">
        <el-input v-model="input" placeholder="请输入搜索内容" class="input"></el-input>
        <el-button icon="el-icon-search" circle @click="getData"></el-button>
      </div>
    </div>

    <!-- 词云图 -->
    <div id="word-cloud" class="col-left1" v-loading="loading" element-loading-text="稍等一会会，大约5分钟"></div>

    <!-- 热点词词频图 -->
    <div id="word-time" class="col-left2" v-loading="loading" element-loading-text="稍等一会会，大约5分钟"></div>

    <!-- 热点事件时间曲线图 -->
    <div id="time-trend" class="col-left3" v-loading="loading" element-loading-text="稍等一会会，大约5分钟"></div>

    <!-- 发展流程图 -->
    <div
      id="event-process"
      class="col-left4"
      v-loading="loading"
      element-loading-text="稍等一会会，大约5分钟"
    >
      <h3>热点新闻时间流程</h3>
      <div
        style="margin-left:10%;width:80%"
        v-for="eventData in eventProcessData"
        :key="eventData.index"
      >
        <div v-for="(item,key) in eventData" :key="key">
          <el-card style="border-top:1px solid rgb(123, 195, 212)">
            <span slot="header">
              <i class="el-icon-date"/>
              {{ key }}
            </span>
            <div v-for="event in item" :key="event.index" class="event-content-style">
              <i class="el-icon-arrow-right"/>
              {{ event }}
            </div>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import echarts from "echarts";
import search from "@/api/search";

export default {
  name: "Welcome",
  data() {
    return {
      input: "",
      loading: false,
      activeNames: ["1"],
      list: "",
      wordDataTest: "",
      wordCloudData: [{ name: "还没有数据", value: 1 }],

      wordTimeData1: ["无数据"],
      wordTimeData2: [0],
      timeTrendData1: ["无数据"],
      timeTrendData2: [0],

      eventProcessData: [
        {
          无数据: ["无数据", "无数据"]
        }
      ]
    };
  },
  mounted() {
    this.initWordCloud();
    this.initWordTime();
    this.initTimeTrend();
  },
  methods: {
    getData() {
      this.loading = true;
      search(this.input).then(response => {
        //词云图
        var array = [];
        for (var i = 0; i < response.data[0][0].length; i++) {
          var jsonObj = {};
          jsonObj.name = response.data[0][0][i];
          jsonObj.value = response.data[0][1][i];
          array[i] = jsonObj;
        }
        this.wordCloudData = array;
        this.initWordCloud();
        //词频表
        this.wordTimeData1 = response.data[0][0];
        this.wordTimeData2 = response.data[0][1];
        this.initWordTime();
        //时间趋势图
        this.timeTrendData1 = response.data[1][0];
        this.timeTrendData2 = response.data[1][1];
        this.initTimeTrend();

        this.eventProcessData = response.data[2];
        this.loading = false;
      });
    },

    initWordCloud() {
      this.chart1 = echarts.init(document.getElementById("word-cloud"));
      this.chart1.setOption({
        title: { text: "相关关键词词云图" },
        series: [
          {
            type: "wordCloud",
            gridSize: 2,
            sizeRange: [40, 160],
            rotationRange: [-90, 90],
            shape: "pentagon",
            textStyle: {
              normal: {
                color: function() {
                  return (
                    "rgb(" +
                    [
                      Math.round(Math.random() * 255),
                      Math.round(Math.random() * 255),
                      Math.round(Math.random() * 255)
                    ].join(",") +
                    ")"
                  );
                }
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: "#333"
              }
            },
            data: this.wordCloudData
          }
        ]
      });
    },

    initWordTime() {
      this.chart2 = echarts.init(document.getElementById("word-time"));
      this.chart2.setOption({
        title: { text: "相关热点词词频图" },
        color: '#d48265',
        xAxis: {
          type: "category",
          data: this.wordTimeData1
        },
        yAxis: {
          type: "value"
        },
        series: [
          {
            data: this.wordTimeData2,
            type: "bar"
          }
        ]
      });
    },

    initTimeTrend() {
      this.chart3 = echarts.init(document.getElementById("time-trend"));
      this.chart3.setOption({
        title: { text: "事件热点时间趋势图" },
        color: '#61a0a8',
        xAxis: {
          type: "category",
          data: this.timeTrendData1
        },
        yAxis: {
          type: "value"
        },
        series: [
          {
            data: this.timeTrendData2,
            type: "bar"
          }
        ]
      });
    }
  }
};
</script>

<style lang="scss" scoped type="text/css">
#welcome {
  left: 0;
  top: 0;
  width: 100%;
  height: auto;
}
.search-container {
  height: 60px;
  display: flex;
}
.search {
  margin: 0;
  margin: auto;
  text-align: center;
}
.input {
  width: 400px;
}

.col-left1 {
  width: 100%;
  height: 800px;
  border-bottom: 1px solid rgb(59, 140, 158);
}
.col-left2 {
  width: 100%;
  height: 800px;
  float: left;
  border-bottom: 1px solid rgb(59, 85, 158);
}
.col-left3 {
  width: 100%;
  height: 800px;
  float: left;
  border-bottom: 1px solid rgb(59, 140, 158);
}
.col-left4 {
  width: 100%;
  height: auto;
  float: left;
}

.event-content-style {
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 20px;
}
</style>
