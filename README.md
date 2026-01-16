# DJIA Stock Analysis Project

## Overview

This project provides a comprehensive analysis of the Dow Jones Industrial Average (DJIA) stock data using Python and Jupyter Notebook. It includes data loading from a PostgreSQL database, data preprocessing, exploratory data analysis, and various financial metrics calculations such as sector-wise returns, volatility, market capitalization, and valuation ratios.

The analysis covers key aspects of stock market performance, helping investors and analysts understand sector trends, risk-return profiles, and investment opportunities within the DJIA index.

## Features

- **Data Loading**: Connect to PostgreSQL database and load stock price and company information data
- **Data Preprocessing**: Merge datasets, handle date conversions, and clean data
- **Exploratory Data Analysis**:
  - Data information and descriptive statistics
  - Distribution analysis of closing prices and PE ratios
  - Sector distribution analysis
- **Sector Analysis**:
  - Sector overview (companies, volume, market cap)
  - Average returns by sector
  - Volatility analysis by sector
  - Market capitalization distribution
  - Price trends over time for top sectors
- **Valuation Metrics**: PE ratio and dividend yield analysis by sector
- **Risk-Return Analysis**: Scatter plot of return vs. volatility for sectors
- **Investment Summary**: Comprehensive metrics for investment decision-making

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database with DJIA data
- Git

### Setup

1. **Clone the repository**:
   ```bash
   git clone ...
   ```

2. **Activate the virtual environment**:
   ```bash
   ...
   ```

3. **Install dependencies** (if not already in the virtual environment):
   ```bash
   pip install pandas sqlalchemy matplotlib seaborn psycopg2-binary
   ```

4. **Set up the database**:
   - Ensure PostgreSQL is running
   - Create a database named `djia_db`
   - Update the connection string in `Analyst.ipynb` if necessary:
     ```python
     engine = create_engine("postgresql+psycopg2://username:password@localhost:5432/djia_db")
     ```

5. **Load data** (if needed):
   - Use `Get_data.py` to fetch and prepare data
   - Run `python check_data.py` to verify data integrity

## Usage

1. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Open Analyst.ipynb**:
   - Run cells sequentially to execute the analysis
   - Each section is clearly marked with markdown headers

3. **Key Outputs**:
   - Data visualizations (histograms, bar charts, pie charts, scatter plots)
   - Summary tables for sector analysis
   - Investment insights based on quantitative metrics

## Project Structure

```
djia-stock-analysis/
│
├── Analyst.ipynb              # Main Jupyter notebook with analysis

```

## Data Sources

- **Stock Prices**: Historical DJIA stock prices from `djia_stock_raw_long.csv`
- **Company Info**: Company details from `djia_company_info.csv`
- **Database**: PostgreSQL tables `fact_stock_price` and `dim_company`

## Requirements

- **Python Libraries**:
  - pandas
  - sqlalchemy
  - matplotlib
  - seaborn
  - psycopg2-binary
  - jupyter

- **Database**: PostgreSQL

## Analysis Methodology

1. **Data Integration**: Merge stock price and company data
2. **Time Series Processing**: Convert dates and calculate daily returns
3. **Sector Grouping**: Aggregate metrics by industry sector
4. **Statistical Analysis**: Compute means, standard deviations, and distributions
5. **Visualization**: Create plots for data interpretation

## Key Insights

- Identify top-performing sectors by return and market cap
- Analyze risk profiles through volatility measures
- Evaluate valuation metrics across industries
- Visualize sector trends and correlations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data sourced from DJIA historical records
- Analysis inspired by financial data science practices
- Built with Python data science ecosystem

## Contact

For questions or suggestions, please open an issue on GitHub.