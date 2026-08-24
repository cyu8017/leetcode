# LeetCode 2011 - Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

# @param {String[]} operations
# @return {Integer}
def final_value_after_operations(operations)
  x = 0
  operations.each { |op| op[1] == "+" ? x += 1 : x -= 1 }
  x
end
