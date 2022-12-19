SELECT * FROM employees ORDER BY FIRST_NAME;

SELECT FIRST_NAME, LAST_NAME, SALARY, COMMISSION_PCT FROM employees WHERE COMMISSION_PCT = 0.15;

SELECT SUM(SALARY) FROM employees;

SELECT MIN(SALARY), MAX(SALARY) FROM employees;

SELECT AVG(SALARY), COUNT(EMPLOYEE_ID) FROM employees;