-- Total Revenue
SELECT SUM(sales) AS total_revenue FROM sales;

-- Sales by Category
SELECT category, SUM(sales) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- Monthly Trend
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(sales) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;

-- Top Products
SELECT product_id, SUM(sales) AS revenue
FROM sales
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 5;
