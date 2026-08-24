# LeetCode 2798 - Number of Employees Who Met the Target
# https://leetcode.com/problems/number-of-employees-who-met-the-target/

# @param {Integer[]} hours
# @param {Integer} target
# @return {Integer}
def number_of_employees_who_met_target(hours, target)
  hours.count { |h| h >= target }
end
