# LeetCode 2298 - Tasks Count in the Weekend
# https:# leetcode.com/problems/tasks-count-in-the-weekend/

QUERY = <<~SQL
  SELECT
      SUM(WEEKDAY(submit_date) IN (5, 6)) AS weekend_cnt,
      SUM(WEEKDAY(submit_date) NOT IN (5, 6)) AS working_cnt
  FROM Tasks
SQL
