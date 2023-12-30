import React, { useState, useEffect } from "react";
import axios from "axios";
import * as d3 from "d3";

const PieChartComponent = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/fetch-data/"); // Replace with your actual JSON data URL
        setData(response.data);
        console.log(response.data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching data:", error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const createPieChart = () => {
    const width = 400;
    const height = 400;
    const radius = Math.min(width, height) / 2;

    const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

    const svg = d3
      .select("#pie-chart-container")
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", `translate(${width / 2},${height / 2})`);

    const pie = d3.pie().value((d) => 1);

    const arc = d3.arc().innerRadius(0).outerRadius(radius);

    const arcs = svg.selectAll("arc").data(pie(data)).enter().append("g");

    arcs
      .append("path")
      .attr("d", arc)
      .attr("fill", (d, i) => colorScale(i));

    arcs
      .append("text")
      .attr("transform", (d) => `translate(${arc.centroid(d)})`)
      .attr("text-anchor", "middle")
      .text((d) => d.data.region);
  };

  useEffect(() => {
    if (!loading) {
      createPieChart();
    }
  }, [loading]);

  return (
    <div>
      {loading && <p>Loading...</p>}
      {!loading && (
        <div>
          <p>Data fetched successfully!</p>
          <div id="pie-chart-container" />
        </div>
      )}
    </div>
  );
};

export default PieChartComponent;
