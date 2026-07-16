# LeetCode 0470 - Implement Rand10() Using Rand7()
# https://leetcode.com/problems/implement-rand10-using-rand7/

def rand7
  raise "rand7 must be provided by the test harness"
end

class Solution
  def rand10
    loop do
      num = (rand7 - 1) * 7 + rand7
      return (num - 1) % 10 + 1 if num <= 40
    end
  end
end
