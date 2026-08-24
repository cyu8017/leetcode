# LeetCode 0757 - Set Intersection Size At Least Two
# https://leetcode.com/problems/set-intersection-size-at-least-two/

# @param {Integer[][]} intervals
# @return {Integer}
def intersection_size_two(intervals)
  intervals = intervals.sort_by { |interval| [interval[1], interval[0]] }
  size = 0
  first = -1
  second = -1
  intervals.each do |left, right|
    next if left <= first

    if left <= second
      size += 1
      first = second
      second = right
    else
      size += 2
      first = right - 1
      second = right
    end
  end
  size
end
