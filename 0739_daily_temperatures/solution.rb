# LeetCode 0739 - Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# @param {Integer[]} temperatures
# @return {Integer[]}
def daily_temperatures(temperatures)
  answer = Array.new(temperatures.length, 0)
  stack = []
  temperatures.each_with_index do |temp, i|
    while !stack.empty? && temperatures[stack[-1]] < temp
      prev = stack.pop
      answer[prev] = i - prev
    end
    stack << i
  end
  answer
end
