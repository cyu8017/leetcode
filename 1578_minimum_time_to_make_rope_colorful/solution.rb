# LeetCode 1578 - Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

# @param {String} colors
# @param {Integer[]} needed_time
# @return {Integer}
def min_cost(colors, needed_time)
  answer = maximum = 0
  needed_time.each_with_index do |cost, i|
    maximum = 0 if i.positive? && colors[i] != colors[i - 1]
    answer += [maximum, cost].min
    maximum = [maximum, cost].max
  end
  answer
end
