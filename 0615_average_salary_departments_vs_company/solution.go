// LeetCode 0615 - Average Salary Departments Vs Company
// https://leetcode.com/problems/average-salary-departments-vs-company/

const QUERY = `
SELECT
    DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month,
    e.department_id,
    CASE
        WHEN AVG(s.amount) > company.avg_amount THEN 'higher'
        WHEN AVG(s.amount) < company.avg_amount THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM Salary s
JOIN Employee e ON s.employee_id = e.employee_id
JOIN (
    SELECT DATE_FORMAT(pay_date, '%Y-%m') AS pay_month, AVG(amount) AS avg_amount
    FROM Salary
    GROUP BY DATE_FORMAT(pay_date, '%Y-%m')
) company ON DATE_FORMAT(s.pay_date, '%Y-%m') = company.pay_month
GROUP BY DATE_FORMAT(s.pay_date, '%Y-%m'), e.department_id, company.avg_amount
`
