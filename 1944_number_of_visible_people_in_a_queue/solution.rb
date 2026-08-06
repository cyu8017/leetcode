# LeetCode 1944 - Number of Visible People in a Queue
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

# @param {Integer[]} heights
# @return {Integer[]}
def can_see_persons_count(heights)
  n = heights.length
  ans = Array.new(n, 0)
  stack = []
  (n - 1).downto(0) do |i|
    count = 0
    while !stack.empty? && heights[i] > stack[-1]
      stack.pop
      count += 1
    end
    count += 1 unless stack.empty?
    ans[i] = count
    stack << heights[i]
  end
  ans
end
