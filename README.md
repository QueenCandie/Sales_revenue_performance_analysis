# Sales & Revenue Performance Analysis

## 📊 Project Overview

This project analyzes sales and revenue performance across regions, products, salespeople, customer segments, discounts, and monthly periods.

The project combines:

- Data quality auditing
- Exploratory data analysis
- Financial performance analysis
- Sales target analysis
- Regional performance analysis
- Product performance analysis
- Salesperson performance analysis
- Customer segment analysis
- Discount analysis
- Business performance insights
- Revenue forecasting
- Machine learning model comparison

The objective is to transform raw sales data into actionable business insights that can support revenue planning, performance management, budgeting, and commercial decision-making.

---

## 🎯 Business Objectives

The analysis aims to answer the following questions:

1. What is the overall revenue and gross profit performance?
2. How well is the business performing against its sales targets?
3. Which regions generate the highest revenue?
4. Which products contribute the most revenue and profit?
5. Which salespeople are the strongest performers?
6. Which customer types generate the most revenue?
7. How do discounts relate to revenue and gross margin?
8. What are the major trends in monthly revenue?
9. Can machine learning be used to forecast future revenue?
10. What actions can management take based on the findings?

---

## 🗂️ Dataset

The dataset contains **1,500 sales records** covering an 18-month period from January 2025 to June 2026.

### Dataset Features

| Feature | Description |
|---|---|
| Date | Transaction date |
| Region | Sales region |
| Product | Product category |
| Salesperson | Sales representative |
| Customer_Type | Customer segment |
| Units_Sold | Number of units sold |
| Unit_Price | Price per unit |
| Discount | Discount applied |
| Revenue | Revenue generated |
| Cost | Cost associated with sales |
| Gross_Profit | Revenue minus cost |
| Gross_Margin | Gross profit margin |
| Sales_Target | Target revenue |

---

## 🔍 Data Quality

The dataset was audited before analysis.

### Results

- Rows: **1,500**
- Columns: **13**
- Missing values: **0**
- Duplicate records: **0**

The dataset was therefore suitable for further analysis.

---

# 💰 Overall Business Performance

| KPI | Result |
|---|---:|
| Total Revenue | ₦12.49 Billion |
| Total Cost | ₦8.29 Billion |
| Total Gross Profit | ₦4.20 Billion |
| Gross Margin | 33.6% |
| Total Sales Target | ₦12.80 Billion |
| Target Achievement | 97.6% |

The business generated approximately **₦12.49 billion in revenue** and **₦4.20 billion in gross profit**, achieving **97.6% of the overall sales target**.

---

# 📅 Monthly Performance

Revenue performance varied significantly across the 18-month period.

The strongest revenue period was:

- **January 2025:** approximately ₦972 million

The weakest period was:

- **June 2026:** approximately ₦466 million

The monthly trend indicates considerable revenue volatility, suggesting the need for stronger sales planning, demand monitoring, and performance management.

---

# 🌍 Regional Performance

### Highest Revenue Region

**Kano**

Revenue:

**₦2.74 Billion**

### Lowest Revenue Region

**Abuja**

Revenue:

**₦2.41 Billion**

Although Kano ranked first and Abuja ranked last, the regional revenue gap was relatively moderate, suggesting opportunities for performance improvement across all regions.

---

# 📦 Product Performance

### Top Product

**Product E**

Revenue:

**₦4.59 Billion**

### Lowest Revenue Product

**Product A**

Revenue:

**₦1.12 Billion**

Product E was the strongest revenue contributor, while Product A generated the lowest revenue.

Management should investigate the drivers of Product E's performance and identify opportunities to improve Product A's sales performance.

---

# 👥 Salesperson Performance

### Top Salesperson

**Salesperson 4**

Revenue:

**₦1.72 Billion**

Other strong performers included:

- Salesperson 3
- Salesperson 7
- Salesperson 8
- Salesperson 5

The performance differences can be used to identify effective sales practices and opportunities for knowledge sharing across the sales team.

---

# 🏢 Customer Type Performance

Revenue was distributed across three major customer segments:

- SME
- Corporate
- Retail

### Highest Revenue Customer Segment

**SME**

Revenue:

**₦5.12 Billion**

Corporate customers generated approximately **₦3.71 billion**, while Retail customers generated approximately **₦3.66 billion**.

---

 💸 Discount Analysis

The average discount across the dataset was:

**7.27%**

Revenue and gross margin were analyzed across three discount categories:

| Discount Range | Revenue | Gross Margin |
|---|---:|---:|
| 0–5% | ₦4.60B | 33.84% |
| 5–10% | ₦4.42B | 33.33% |
| 10–15% | ₦3.47B | 33.63% |

The analysis indicates that higher discounts did not automatically translate into higher revenue.

Discount policies should therefore be monitored alongside profitability metrics rather than revenue alone.

---

📈 Performance Drivers

Correlation analysis was used to understand the relationship between revenue and selected business variables.

Correlation with Revenue

| Variable | Correlation |
|---|---:|
| Sales Target | 0.993 |
| Cost | 0.987 |
| Gross Profit | 0.955 |
| Units Sold | 0.702 |
| Unit Price | 0.658 |
| Discount | -0.066 |
| Gross Margin | -0.010 |

Sales Target, Cost, and Gross Profit showed strong positive relationships with Revenue.

Units Sold and Unit Price also showed positive relationships with revenue.

Discount and Gross Margin showed very weak linear relationships with revenue in this dataset.

> Correlation indicates association, not causation.

---

🤖 Revenue Forecasting

Machine learning was used to develop a revenue forecasting model.

Monthly revenue data was transformed into forecasting features including:

- Lagged revenue
- Three-month lag
- Rolling three-month revenue
- Historical revenue patterns

Two models were evaluated:
 1. Linear Regression

- MAE: **₦0.153 Billion**
- RMSE: **₦0.167 Billion**
- MAPE: **28.96%**

2. Random Forest

- MAE: **₦0.149 Billion**
- RMSE: **₦0.164 Billion**
- MAPE: **28.28%**

Selected Model

Random Forest

The Random Forest model achieved the lower MAE, RMSE, and MAPE of the two tested models.

However, the **28.28% MAPE indicates that the current forecasting model has substantial prediction error** and should be treated as a baseline model rather than a highly accurate forecasting system.

---

 📊 Forecasting Results

The model was evaluated on four testing periods.

| Month | Actual Revenue | Forecast |
|---|---:|---:|
| March 2026 | ₦513M | ₦665M |
| April 2026 | ₦627M | ₦781M |
| May 2026 | ₦668M | ₦716M |
| June 2026 | ₦466M | ₦706M |

The model consistently overestimated revenue during the test period, particularly in June 2026.

This suggests that additional forecasting variables and a larger historical dataset could improve predictive performance.

---

# 💡 Key Business Insights

1. Revenue performance is volatile

Monthly revenue fluctuated considerably throughout the analysis period.

This creates challenges for revenue planning and forecasting.

2. Target achievement is close but below plan

Overall target achievement was **97.6%**, indicating that the business is performing close to plan but has room for improvement.

3. Kano is the leading region

Kano generated the highest regional revenue at approximately **₦2.74 billion**.

4. Product E is the strongest product

Product E generated approximately **₦4.59 billion**, making it the largest product revenue contributor.

5. SME customers are important revenue contributors

SME customers generated approximately **₦5.12 billion**, representing the largest customer segment by revenue.

6. Revenue and profitability should be monitored together

Revenue growth should not be evaluated independently of gross profit and gross margin.

7. Forecasting requires improvement

The Random Forest model performed better than Linear Regression but still produced a relatively high MAPE of **28.28%**.

---

# 🚀 Business Recommendations

1. Improve monthly revenue planning

Investigate the causes of significant month-to-month revenue fluctuations and incorporate seasonal patterns into planning.

2. Replicate high-performing practices

Study the strategies used by high-performing regions and salespeople and apply successful practices across weaker-performing teams.

3. Investigate Product A

Analyze pricing, demand, distribution, customer preferences, and sales execution to understand the relatively low performance of Product A.

4. Protect Product E performance

Product E is the largest revenue contributor and should be monitored closely to protect its market performance.

5. Improve target achievement

The business should investigate recurring gaps between actual revenue and sales targets and develop corrective action plans.

6. Monitor discounts carefully

Discounts should be evaluated based on their effect on both revenue and profitability.

7. Improve forecasting

Future forecasting models could incorporate:

- Seasonality
- Region
- Product
- Customer type
- Salesperson performance
- Discount levels
- Unit volume
- Pricing
- Additional historical observations

---

 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Exploratory Data Analysis
- Machine Learning
- Statistical Analysis
- Business Intelligence
- Revenue Forecasting
