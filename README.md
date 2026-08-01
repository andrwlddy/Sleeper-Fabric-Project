# Sleeper-Fabric-Project
Project connecting to Sleeper API, ingesting data into Fabric, and learning more about Fabric
# Fantasy Football Analytics Platform

## Project Overview

This project is an end-to-end analytics engineering project built with Microsoft Fabric. Data is collected from the Sleeper Fantasy Football API, transformed into a star schema using Python and Delta Lake, and visualized through interactive Power BI reports.

The project is being developed incrementally as I continue learning Microsoft Fabric and modern analytics engineering best practices.

---

# Project Workflow

## Step 1 – Data Source Discovery

### Objective

Identify a publicly available data source that provides rich, real-world data suitable for analytics.

### Completed

* Evaluated multiple API options.
* Selected the Sleeper Fantasy Football API.
* Identified available endpoints.
* Planned the overall data model.

### Technologies & Skills

* REST APIs
* JSON
* Data Modeling
* Solution Design

---

## Step 2 – Data Ingestion (Bronze Layer)

### Objective

Extract raw data from the Sleeper API and store it in Microsoft Fabric without modification.

### Completed

* Built Python notebooks to call API endpoints.
* Retrieved league data for multiple seasons.
* Retrieved player metadata.
* Retrieved owner information.
* Retrieved roster information.
* Retrieved matchup information.
* Retrieved draft information.
* Stored raw JSON files in the Fabric Lakehouse.

### Technologies & Skills

* Python
* Requests Library
* JSON
* Microsoft Fabric Notebooks
* Lakehouse
* OneLake
* Data Ingestion

---

## Step 3 – Data Transformation (Silver Layer)

### Objective

Convert raw JSON files into structured Delta tables optimized for analytics.

### Completed

* Combined multiple seasons into unified tables.
* Flattened nested JSON structures.
* Cleaned inconsistent data.
* Created reusable business columns.
* Created composite keys.
* Added season identifiers.
* Calculated matchup results.
* Calculated point differential.
* Built reusable week keys.
* Saved transformed data as Delta tables.

### Technologies & Skills

* Python
* Pandas
* Delta Lake
* Data Cleaning
* Data Transformation
* Analytics Engineering

---

## Step 4 – Data Modeling

### Objective

Design a star schema to support efficient reporting and analytics.

### Completed

Created Fact Tables

* Fact_Matchups
* Fact_Player_Performance

Created Dimension Tables

* Dim_Player
* Dim_Owner
* Dim_Roster
* Dim_Calendar

Additional work

* Built one-to-many relationships.
* Created reusable calendar dimension.
* Built hierarchies.
* Created semantic model.
* Implemented star schema design.

### Technologies & Skills

* Star Schema Design
* Semantic Modeling
* Data Relationships
* Dimensional Modeling
* Microsoft Fabric
* Power BI

---

## Step 5 – Analytics & Reporting

### Objective

Develop dashboards that provide meaningful insights into league and player performance.

### Completed

Created visualizations including:

* Weekly point differential trends
* Highest scoring player performances
* Highest scoring player seasons
* Team performance comparisons
* Historical scoring analysis
* Interactive filtering
* DAX measures
* Report navigation

### Technologies & Skills

* Power BI
* DAX
* Data Visualization
* Dashboard Design
* Business Intelligence

---

## Step 6 – Source Control & Documentation

### Objective

Document the project and track development over time.

### Completed

* Created GitHub repository.
* Documented project architecture.
* Maintained project README.
* Version controlled notebooks and project files.

### Technologies & Skills

* Git
* GitHub
* Documentation
* Version Control

---


