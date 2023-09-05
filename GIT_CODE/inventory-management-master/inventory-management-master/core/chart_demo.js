var xValues = ["Allocated", "Not-Allocated" ];
var yValues = [100,200];
var barColors = [
  "#b91d47",
  "#00aba9"
];

new Chart("myChart", {
  type: "pie",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "Analytics of inventory managment"
    }
  }
});