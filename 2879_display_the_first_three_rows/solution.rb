# LeetCode 2879 - Display the First Three Rows
# https://leetcode.com/problems/display-the-first-three-rows/

# @param {Object[]} employees
# @return {Object[]}
def select_first_rows(employees)
  employees[0, 3] || []
end
