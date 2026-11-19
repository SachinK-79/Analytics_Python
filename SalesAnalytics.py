import pandas as pd
import numpy as np

class SalesAnalytics:

    def __init__(self,data):
        self.df=data.copy()

        self.df["revenue"]=(
            self.df["units_sold"]*self.df["unit_price"]
        )

        # Calculate cost
        self.df["cost"]=(
            self.df["units_sold"]*self.df["unit_cost"]
        )

        self.df["profit"]=(
            self.df["revenue"]-self.df["cost"]
        )

        # profit margin
        self.df["profit_margin"]=np.where(
            self.df["revenue"]>0,
            (self.df["profit"]/self.df["revenue"])*100,
            0
        )

    def overall_summary(self):
        total_revenue=self.df["revenue"].sum()
        total_cost=self.df["cost"].sum()
        total_profit=self.df["profit"].sum()
        total_units=self.df["units_sold"].sum()

        average_order_value=(
            self.df["revenue"].sum()/
            self.df["order_id"].nunique()
        )

        return{
            "Total Revenue":total_revenue,
            "Total Cost":total_cost,
            "Total profit":total_profit,
            "Total Units":total_units,
            "Average Order Value":average_order_value
        }

    def region_analysis(self):
        result=(
            self.df
            .groupby("region")
            .agg(
                revenue=("revenue","sum"),
                profit=("profit","sum"),
                units=("units_sold","sum"),
                orders=("order_id","nunique")
            )
            .reset_index()
        )

        result["profit_margin"]=np.where(
            result["revenue"]>0,
            (result["profit"]/result["revenue"]*100,0)
            return result)

    def product_analysis(self):
        result=(
            self.df
            .groupby("product")
            .agg(
                revenue=("revenue","sum"),
                profit=("profit","sum"),
                units=("units_sold","sum")
        )
        .reset_index()
        )

        result["profit_margin"]=np.where(
               result["revenue"]>0,
               (result["profit"]/result["revenue"])*100,
               0
        )
        return result

    def monthly_analysis(self):
        self.df["date"]=pd.to_datetime(self.df["date"])
        self.df["month"]=self.df["date"].dt.month_name()

        result=(
            self.df
            .groupby("month")
            .agg(
                revenue=("revenue","sum"),
                profit=("profit","sum"),
                units=("units_sold","sum")
            )
            .reset_index()
        )

        return result

    def return_analysis(self):
        total_orders=self.df["order_id"].nunique()

        returned_orders=(
            self.df[self.df["returned"]==True]
            ["order_id"]
            .nunique()
        )

        return_rate=np.where(
                      total_orders>0,
                      (returned_orders/total_orders)*100,
                      0
                      )
        return{
                "Total Orders":total_orders,
                "Returned Orders":returned_orders,
                "Return Rate":return_rate
        }

# Sample Data
data = pd.DataFrame({

    "order_id": [
        "O1001", "O1002", "O1003", "O1004",
        "O1005", "O1006", "O1007", "O1008",
        "O1009", "O1010"
    ],

    "date": [
        "2026-01-05",
        "2026-01-06",
        "2026-01-10",
        "2026-01-15",
        "2026-02-02",
        "2026-02-10",
        "2026-02-15",
        "2026-03-01",
        "2026-03-10",
        "2026-03-15"
    ],

    "region": [
        "North",
        "South",
        "North",
        "West",
        "South",
        "East",
        "West",
        "North",
        "East",
        "South"
    ],

    "product": [
        "Laptop",
        "Phone",
        "Tablet",
        "Laptop",
        "Phone",
        "Tablet",
        "Laptop",
        "Phone",
        "Laptop",
        "Tablet"
    ],

    "units_sold": [
        2, 5, 3, 1, 8,
        4, 2, 6, 3, 5
    ],

    "unit_price": [
        70000, 30000, 25000, 70000, 30000,
        25000, 70000, 30000, 70000, 25000
    ],

    "unit_cost": [
        55000, 22000, 18000, 55000, 22000,
        18000, 55000, 22000, 55000, 18000
    ],

    "returned": [
        False, False, True, False, False,
        False, True, False, False, True
    ]
})

analytics=SalesAnalytics(data)
print("Overall summary")
print(analytics.overall_summary())
print("Region analysis")
print(analytics.region_analysis())
print("Product analysis")
print(analytics.product_analysis())
print("Monthly analysis")
print(analytics.monthly_analysis())
print("\n Return analysis")
print(analytics.return_analysis())
        