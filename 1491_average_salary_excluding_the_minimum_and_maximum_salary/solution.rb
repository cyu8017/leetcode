# LeetCode 1491 - Average Salary Excluding The Minimum And Maximum Salary
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

def average(salary)
  (salary.sum - salary.min - salary.max).to_f / (salary.length - 2)
end
