# ============================================================
# SALES & REVENUE PERFORMANCE ANALYSIS
# ============================================================
# Author: Oluwaseyi Obarayo
# Project: Sales & Revenue Performance Analysis
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import os
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


warnings.filterwarnings("ignore")


# ============================================================
# 2. FILE PATHS
# ============================================================

DATA_PATH = "/storage/emulated/0/sales_revenue_dataset.csv"

OUTPUT_DIR = "/storage/emulated/0/sales_revenue_project_outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# 3. LOAD DATA
# ============================================================

print("=" * 70)
print("SALES & REVENUE PERFORMANCE ANALYSIS")
print("=" * 70)

df = pd.read_csv(DATA_PATH)

df["Date"] = pd.to_datetime(df["Date"])

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# ============================================================
# 4. DATA QUALITY AUDIT
# ============================================================

print("\n" + "=" * 70)
print("DATA QUALITY AUDIT")
print("=" * 70)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)


# ============================================================
# 5. OVERALL BUSINESS PERFORMANCE
# ============================================================

total_revenue = df["Revenue"].sum()
total_cost = df["Cost"].sum()
total_gross_profit = df["Gross_Profit"].sum()

overall_gross_margin = (
    total_gross_profit / total_revenue
) * 100

total_sales_target = df["Sales_Target"].sum()

target_achievement = (
    total_revenue / total_sales_target
) * 100


print("\n" + "=" * 70)
print("OVERALL BUSINESS PERFORMANCE")
print("=" * 70)

print(f"\nTotal Revenue: ₦ {total_revenue:,.2f}")
print(f"Total Cost: ₦ {total_cost:,.2f}")
print(f"Total Gross Profit: ₦ {total_gross_profit:,.2f}")
print(f"Overall Gross Margin: {overall_gross_margin:.1f} %")
print(f"Total Sales Target: ₦ {total_sales_target:,.2f}")
print(f"Overall Target Achievement: {target_achievement:.1f} %")


# ============================================================
# 6. MONTHLY PERFORMANCE
# ============================================================

monthly = (
    df.groupby(df["Date"].dt.to_period("M"))
    .agg(
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross_Profit", "sum"),
        Sales_Target=("Sales_Target", "sum"),
        Units_Sold=("Units_Sold", "sum")
    )
    .reset_index()
)

monthly["Month"] = monthly["Date"].astype(str)

monthly["Gross_Margin"] = (
    monthly["Gross_Profit"] /
    monthly["Revenue"] * 100
)

monthly["Target_Achievement"] = (
    monthly["Revenue"] /
    monthly["Sales_Target"] * 100
)

monthly["MoM_Growth"] = (
    monthly["Revenue"].pct_change() * 100
)


print("\n" + "=" * 70)
print("MONTHLY PERFORMANCE")
print("=" * 70)

print(
    monthly[
        [
            "Month",
            "Revenue",
            "Cost",
            "Gross_Profit",
            "Sales_Target",
            "Target_Achievement",
            "MoM_Growth"
        ]
    ]
)


# ============================================================
# 7. REGIONAL PERFORMANCE
# ============================================================

regional = (
    df.groupby("Region")
    .agg(
        Revenue=("Revenue", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross_Profit", "sum"),
        Sales_Target=("Sales_Target", "sum"),
        Units_Sold=("Units_Sold", "sum")
    )
    .reset_index()
)

regional["Gross_Margin"] = (
    regional["Gross_Profit"] /
    regional["Revenue"] * 100
)

regional["Target_Achievement"] = (
    regional["Revenue"] /
    regional["Sales_Target"] * 100
)

regional = regional.sort_values(
    "Revenue",
    ascending=False
)


print("\n" + "=" * 70)
print("REGIONAL PERFORMANCE")
print("=" * 70)

print(regional)


# ============================================================
# 8. PRODUCT PERFORMANCE
# ============================================================

product = (
    df.groupby("Product")
    .agg(
        Revenue=("Revenue", "sum"),
        Gross_Profit=("Gross_Profit", "sum"),
        Sales_Target=("Sales_Target", "sum"),
        Units_Sold=("Units_Sold", "sum")
    )
    .reset_index()
)

product["Gross_Margin"] = (
    product["Gross_Profit"] /
    product["Revenue"] * 100
)

product = product.sort_values(
    "Revenue",
    ascending=False
)


print("\n" + "=" * 70)
print("PRODUCT PERFORMANCE")
print("=" * 70)

print(product)


# ============================================================
# 9. SALESPERSON PERFORMANCE
# ============================================================

salesperson = (
    df.groupby("Salesperson")
    .agg(
        Revenue=("Revenue", "sum"),
        Gross_Profit=("Gross_Profit", "sum"),
        Units_Sold=("Units_Sold", "sum")
    )
    .reset_index()
)

salesperson["Gross_Margin"] = (
    salesperson["Gross_Profit"] /
    salesperson["Revenue"] * 100
)

salesperson = salesperson.sort_values(
    "Revenue",
    ascending=False
)


print("\n" + "=" * 70)
print("SALESPERSON PERFORMANCE")
print("=" * 70)

print(salesperson)


# ============================================================
# 10. CUSTOMER TYPE PERFORMANCE
# ============================================================

customer_type = (
    df.groupby("Customer_Type")
    .agg(
        Revenue=("Revenue", "sum"),
        Gross_Profit=("Gross_Profit", "sum"),
        Units_Sold=("Units_Sold", "sum")
    )
    .reset_index()
)

customer_type["Gross_Margin"] = (
    customer_type["Gross_Profit"] /
    customer_type["Revenue"] * 100
)

customer_type = customer_type.sort_values(
    "Revenue",
    ascending=False
)


print("\n" + "=" * 70)
print("CUSTOMER TYPE PERFORMANCE")
print("=" * 70)

print(customer_type)


# ============================================================
# 11. DISCOUNT ANALYSIS
# ============================================================

df["Discount_Group"] = pd.cut(
    df["Discount"] * 100,
    bins=[0, 5, 10, 15, 100],
    labels=[
        "0-5%",
        "5-10%",
        "10-15%",
        "15%+"
    ],
    include_lowest=True
)

average_discount = df["Discount"].mean() * 100


discount_analysis = (
    df.groupby(
        "Discount_Group",
        observed=False
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Gross_Profit=("Gross_Profit", "sum")
    )
    .reset_index()
)

discount_analysis["Gross_Margin"] = (
    discount_analysis["Gross_Profit"] /
    discount_analysis["Revenue"] * 100
)


print("\n" + "=" * 70)
print("DISCOUNT ANALYSIS")
print("=" * 70)

print(f"\nAverage Discount: {average_discount:.2f} %")

print(discount_analysis)


# ============================================================
# 12. TOP PERFORMERS
# ============================================================

highest_region = regional.iloc[0]

lowest_region = regional.iloc[-1]

highest_product = product.iloc[0]

lowest_product = product.iloc[-1]

top_salesperson = salesperson.iloc[0]


print("\n" + "=" * 70)
print("TOP PERFORMERS")
print("=" * 70)

print(
    f"\nHighest Revenue Region: "
    f"{highest_region['Region']}"
)

print(
    f"Revenue: ₦ "
    f"{highest_region['Revenue']:,.2f}"
)

print(
    f"\nHighest Revenue Product: "
    f"{highest_product['Product']}"
)

print(
    f"Revenue: ₦ "
    f"{highest_product['Revenue']:,.2f}"
)

print(
    f"\nTop Salesperson: "
    f"{top_salesperson['Salesperson']}"
)

print(
    f"Revenue: ₦ "
    f"{top_salesperson['Revenue']:,.2f}"
)


# ============================================================
# 13. AREAS NEEDING ATTENTION
# ============================================================

print("\n" + "=" * 70)
print("AREAS NEEDING ATTENTION")
print("=" * 70)

print(
    f"\nLowest Revenue Region: "
    f"{lowest_region['Region']}"
)

print(
    f"Revenue: ₦ "
    f"{lowest_region['Revenue']:,.2f}"
)

print(
    f"\nLowest Revenue Product: "
    f"{lowest_product['Product']}"
)

print(
    f"Revenue: ₦ "
    f"{lowest_product['Revenue']:,.2f}"
)


# ============================================================
# 14. PERFORMANCE DRIVER ANALYSIS
# ============================================================

numeric_columns = [
    "Revenue",
    "Sales_Target",
    "Cost",
    "Gross_Profit",
    "Units_Sold",
    "Unit_Price",
    "Gross_Margin",
    "Discount"
]

correlation = df[numeric_columns].corr()["Revenue"].sort_values(
    ascending=False
)


print("\n" + "=" * 70)
print("PERFORMANCE DRIVER ANALYSIS")
print("=" * 70)

print("\nCorrelation with Revenue:")
print(correlation)


# ============================================================
# 15. VISUALIZATION 1
# MONTHLY REVENUE TREND
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    monthly["Month"],
    monthly["Revenue"] / 1e6,
    marker="o"
)

plt.title("Monthly Revenue Trend")

plt.xlabel("Month")

plt.ylabel("Revenue (₦ Million)")

plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "monthly_revenue_trend.png"
    ),
    dpi=300
)

plt.show()

plt.close()


# ============================================================
# 16. VISUALIZATION 2
# REVENUE BY REGION
# ============================================================

plt.figure(figsize=(10, 6))

plt.barh(
    regional["Region"],
    regional["Revenue"] / 1e9
)

plt.title("Revenue by Region")

plt.xlabel("Revenue (₦ Billion)")

plt.ylabel("Region")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "revenue_by_region.png"
    ),
    dpi=300
)

plt.show()

plt.close()


# ============================================================
# 17. VISUALIZATION 3
# PRODUCT REVENUE VS GROSS PROFIT
# ============================================================

x = np.arange(len(product))

width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(
    x - width / 2,
    product["Revenue"] / 1e9,
    width,
    label="Revenue"
)

plt.bar(
    x + width / 2,
    product["Gross_Profit"] / 1e9,
    width,
    label="Gross Profit"
)

plt.xticks(
    x,
    product["Product"]
)

plt.title("Product Revenue vs Gross Profit")

plt.xlabel("Product")

plt.ylabel("Amount (₦ Billion)")

plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "product_revenue_vs_gross_profit.png"
    ),
    dpi=300
)

plt.show()

plt.close()


# ============================================================
# 18. VISUALIZATION 4
# MONTHLY REVENUE VS SALES TARGET
# ============================================================

plt.figure(figsize=(11, 6))

plt.plot(
    monthly["Month"],
    monthly["Revenue"] / 1e6,
    marker="o",
    label="Actual Revenue"
)

plt.plot(
    monthly["Month"],
    monthly["Sales_Target"] / 1e6,
    marker="o",
    label="Sales Target"
)

plt.title("Monthly Revenue vs Sales Target")

plt.xlabel("Month")

plt.ylabel("Amount (₦ Million)")

plt.xticks(rotation=45)

plt.legend()

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "monthly_revenue_vs_target.png"
    ),
    dpi=300
)

plt.show()

plt.close()


# ============================================================
# 19. REVENUE FORECASTING DATASET
# ============================================================

print("\n" + "=" * 70)
print("SALES REVENUE FORECASTING")
print("=" * 70)


forecast = monthly[
    ["Date", "Revenue"]
].copy()

forecast["Lag_1"] = forecast["Revenue"].shift(1)

forecast["Lag_2"] = forecast["Revenue"].shift(2)

forecast["Lag_3"] = forecast["Revenue"].shift(3)

forecast["Rolling_3_Month"] = (
    forecast["Revenue"]
    .shift(1)
    .rolling(3)
    .mean()
)

forecast = forecast.dropna().reset_index(drop=True)


print("\nForecasting Dataset:")

print(forecast)


print(
    f"\nNumber of observations: "
    f"{len(forecast)}"
)


# ============================================================
# 20. TRAIN / TEST SPLIT
# ============================================================

features = [
    "Lag_1",
    "Lag_2",
    "Lag_3",
    "Rolling_3_Month"
]

X = forecast[features]

y = forecast["Revenue"]


# Use chronological split
# 75% training / 25% testing

split_index = int(len(forecast) * 0.75)

X_train = X.iloc[:split_index]

X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]

y_test = y.iloc[split_index:]

test_dates = forecast["Date"].iloc[split_index:]


print(
    f"\nTraining observations: "
    f"{len(X_train)}"
)

print(
    f"Testing observations: "
    f"{len(X_test)}"
)


# ============================================================
# 21. EVALUATION FUNCTION
# ============================================================

def evaluate_model(
    model_name,
    actual,
    predicted
):

    mae = mean_absolute_error(
        actual,
        predicted
    )

    rmse = np.sqrt(
        mean_squared_error(
            actual,
            predicted
        )
    )

    mape = (
        np.mean(
            np.abs(
                (actual - predicted) /
                actual
            )
        ) * 100
    )

    print(f"\n{model_name}")

    print(
        f"MAE: ₦ "
        f"{mae / 1e9:.3f} Billion"
    )

    print(
        f"RMSE: ₦ "
        f"{rmse / 1e9:.3f} Billion"
    )

    print(
        f"MAPE: "
        f"{mape:.2f} %"
    )

    return mae, rmse, mape


# ============================================================
# 22. LINEAR REGRESSION
# ============================================================

print("\n" + "=" * 70)
print("LINEAR REGRESSION FORECAST")
print("=" * 70)


linear_model = LinearRegression()

linear_model.fit(
    X_train,
    y_train
)

linear_predictions = linear_model.predict(
    X_test
)


linear_mae, linear_rmse, linear_mape = evaluate_model(
    "Linear Regression Performance",
    y_test,
    linear_predictions
)


linear_results = pd.DataFrame({
    "Month": test_dates,
    "Actual_Revenue": y_test.values,
    "Linear_Predicted": linear_predictions
})


print("\nActual vs Predicted:")

print(linear_results)


# ============================================================
# 23. RANDOM FOREST
# ============================================================

print("\n" + "=" * 70)
print("RANDOM FOREST FORECAST")
print("=" * 70)


rf_model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    max_depth=5
)

rf_model.fit(
    X_train,
    y_train
)

rf_predictions = rf_model.predict(
    X_test
)


rf_mae, rf_rmse, rf_mape = evaluate_model(
    "Random Forest Performance",
    y_test,
    rf_predictions
)


rf_results = pd.DataFrame({
    "Month": test_dates,
    "Actual_Revenue": y_test.values,
    "RF_Predicted": rf_predictions
})


print("\nActual vs Predicted:")

print(rf_results)


# ============================================================
# 24. MODEL COMPARISON
# ============================================================

comparison = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest"
    ],

    "MAE_Billion": [
        linear_mae / 1e9,
        rf_mae / 1e9
    ],

    "RMSE_Billion": [
        linear_rmse / 1e9,
        rf_rmse / 1e9
    ],

    "MAPE": [
        linear_mape,
        rf_mape
    ]
})


print("\n" + "=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

print(comparison)


# ============================================================
# 25. SELECT BEST MODEL
# ============================================================

best_model_row = comparison.loc[
    comparison["MAPE"].idxmin()
]

selected_model = best_model_row["Model"]

selected_mape = best_model_row["MAPE"]


print(
    f"\nSelected Forecasting Model: "
    f"{selected_model}"
)

print(
    f"Forecast MAPE: "
    f"{selected_mape:.2f} %"
)


# ============================================================
# 26. VISUALIZATION 5
# ACTUAL VS FORECAST
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    test_dates,
    y_test.values / 1e6,
    marker="o",
    label="Actual Revenue"
)

plt.plot(
    test_dates,
    rf_predictions / 1e6,
    marker="o",
    label="Random Forest Forecast"
)

plt.title(
    "Actual vs Forecasted Revenue"
)

plt.xlabel("Month")

plt.ylabel("Revenue (₦ Million)")

plt.legend()

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "actual_vs_forecast.png"
    ),
    dpi=300
)

plt.show()

plt.close()


# ============================================================
# 27. SAVE ANALYSIS OUTPUTS
# ============================================================

monthly.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "monthly_performance.csv"
    ),
    index=False
)

regional.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "regional_performance.csv"
    ),
    index=False
)

product.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "product_performance.csv"
    ),
    index=False
)

salesperson.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "salesperson_performance.csv"
    ),
    index=False
)

customer_type.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "customer_type_performance.csv"
    ),
    index=False
)

discount_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "discount_analysis.csv"
    ),
    index=False
)

comparison.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "model_comparison.csv"
    ),
    index=False
)

rf_results.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "forecast_results.csv"
    ),
    index=False
)


# ============================================================
# 28. EXECUTIVE BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 70)
print("EXECUTIVE BUSINESS INSIGHTS")
print("=" * 70)

print(
    f"\n1. Total Revenue: "
    f"₦ {total_revenue:,.2f}"
)

print(
    f"2. Total Gross Profit: "
    f"₦ {total_gross_profit:,.2f}"
)

print(
    f"3. Overall Gross Margin: "
    f"{overall_gross_margin:.1f} %"
)

print(
    f"4. Overall Target Achievement: "
    f"{target_achievement:.1f} %"
)

print(
    f"5. Best Performing Region: "
    f"{highest_region['Region']}"
)

print(
    f"6. Best Performing Product: "
    f"{highest_product['Product']}"
)

print(
    f"7. Top Salesperson: "
    f"{top_salesperson['Salesperson']}"
)


# ============================================================
# 29. BUSINESS RECOMMENDATIONS
# ============================================================

print("\n" + "=" * 70)
print("BUSINESS RECOMMENDATIONS")
print("=" * 70)

print("""
1. Identify and replicate the practices of the highest
   performing regions and sales teams.

2. Investigate low-performing regions and products to
   understand whether pricing, demand, distribution or
   sales execution is responsible.

3. Monitor gross margin alongside revenue to ensure that
   revenue growth translates into profitable growth.

4. Review discount levels and their effect on profitability.

5. Use monthly revenue trends and target achievement to
   identify periods requiring corrective action.

6. Prioritize high-performing products and customer segments
   while investigating opportunities to improve weaker categories.

7. Improve future forecasting by incorporating additional
   historical data, seasonality, product, region, customer type,
   pricing and discount variables.
""")


# ============================================================
# 30. COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 70)
print("SALES & REVENUE ANALYSIS COMPLETE")
print("=" * 70)

print(
    f"\nAll output files saved to:"
)

print(OUTPUT_DIR)
