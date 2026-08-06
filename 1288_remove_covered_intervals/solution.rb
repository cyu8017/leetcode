# LeetCode 1288 - Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/

# @param {Integer[][]} intervals
# @return {Integer}
def remove_covered_intervals(intervals)
  intervals = intervals.sort_by { |x| [x[0], -x[1]] }
  answer = 0
  farthest = -1
  intervals.each do |_, finish|
    if finish > farthest
      answer += 1
      farthest = finish
    end
  end
  answer
end
