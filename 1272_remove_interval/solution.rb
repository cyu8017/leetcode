# LeetCode 1272 - Remove Interval
# https://leetcode.com/problems/remove-interval/

# @param {Integer[][]} intervals
# @param {Integer[]} to_be_removed
# @return {Integer[][]}
def remove_interval(intervals, to_be_removed)
  left, right = to_be_removed
  answer = []
  intervals.each do |start, finish|
    if finish <= left || start >= right
      answer << [start, finish]
    else
      answer << [start, left] if start < left
      answer << [right, finish] if finish > right
    end
  end
  answer
end
