# India Weather Dashboard

## The Problem
Weather data for 10 major Indian cities —
scattered across an API, unavailable in one place,
and never in a format a dashboard can consume.

This project fixes that in under 50 lines of code.

## What I Built
A live Python ETL pipeline that hits the Open-Meteo API
for 10 major Indian cities, extracts real-time temperature,
windspeed, and weather conditions, and pipes the output
directly into a Power BI dashboard.

No manual data collection. No static CSVs.
Run the script, refresh the dashboard, done.

## Cities Covered
Hyderabad, Delhi, Bangalore, Chennai, Kolkata,
Mumbai, Pune, Jaipur, Ahmedabad, Lucknow

## Pipeline
Open-Meteo API (live weather data)
       ↓
Python requests → JSON extraction
       ↓
Pandas DataFrame construction
       ↓
India_Weather_Data.csv
       ↓
Power BI Dashboard

## Tech Stack
Python, Pandas, Requests, Open-Meteo API, Power BI

## How to Run
1. Clone the repo
2. Run weather_pipeline.py
3. CSV auto-generates in the same folder
4. Refresh Power BI to update the dashboard

## API
Open-Meteo — free, no API key required
Documentation: https://open-meteo.com/
