# LeetCode 2169 - Count Operations to Obtain Zero
# https://leetcode.com/problems/count-operations-to-obtain-zero/

# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def count_operations(num1, num2)
  ans = 0
  while num1 > 0 && num2 > 0
    if num1 >= num2
      ans += num1 / num2
      num1 %= num2
    else
      ans += num2 / num1
      num2 %= num1
    end
  end
  ans
end
