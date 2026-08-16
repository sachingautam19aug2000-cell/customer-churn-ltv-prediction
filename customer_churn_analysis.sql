


CREATE TABLE telco_customer_churn (
    customerid VARCHAR(50),
    gender VARCHAR(20),
    seniorcitizen INTEGER,
    partner VARCHAR(10),
    dependents VARCHAR(10),
    tenure INTEGER,
    phoneservice VARCHAR(10),
    multiplelines VARCHAR(30),
    internetservice VARCHAR(30),
    onlinesecurity VARCHAR(30),
    onlinebackup VARCHAR(30),
    deviceprotection VARCHAR(30),
    techsupport VARCHAR(30),
    streamingtv VARCHAR(30),
    streamingmovies VARCHAR(30),
    contract VARCHAR(30),
    paperlessbilling VARCHAR(10),
    paymentmethod VARCHAR(50),
    monthlycharges NUMERIC(10,2),
    totalcharges VARCHAR(30),
    churn VARCHAR(10)
);

SELECT * FROM telco_customer_churn

SELECT * FROM telco_customer_churn LIMIT 10;

-- Total customers
SELECT COUNT(*) AS total_customers
FROM telco_customer_churn;

-- 1. Churn count
SELECT churn, COUNT(*) AS customers
FROM telco_customer_churn
GROUP BY churn;

-- 2. Average monthly charges
SELECT AVG(monthlycharges) AS avg_monthly_charges
FROM telco_customer_churn;

-- 3. Contract-wise churn
SELECT
    contract,
    churn,
    COUNT(*) AS customers
FROM telco_customer_churn
GROUP BY contract, churn
ORDER BY contract, churn;

-- 4. Internet service-wise churn
SELECT
    internetservice,
    churn,
    COUNT(*) AS customers
FROM telco_customer_churn
GROUP BY internetservice, churn
ORDER BY internetservice, churn;

-- 5. Average tenure by churn
SELECT
    churn,
    ROUND(AVG(tenure), 2) AS avg_tenure
FROM telco_customer_churn
GROUP BY churn;

-- 6. Average monthly charges by churn
SELECT
    churn,
    ROUND(AVG(monthlycharges), 2) AS avg_monthly_charges
FROM telco_customer_churn
GROUP BY churn;

-- 7. Blank TotalCharges check
SELECT COUNT(*) AS blank_total_charges
FROM telco_customer_churn
WHERE totalcharges IS NULL
   OR TRIM(totalcharges) = '';