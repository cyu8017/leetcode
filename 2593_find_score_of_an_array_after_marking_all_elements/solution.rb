# LeetCode 2593 - Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

# @param {Integer[]} nums
# @return {Integer}
def find_score(nums)
  n = nums.length
  idx = (0...n).to_a.sort_by { |i| [nums[i], i] }
  marked = Array.new(n, false)
  ans = 0
  idx.each do |i|
    next if marked[i]

    ans += nums[i]
    marked[i] = true
    marked[i - 1] = true if i - 1 >= 0
    marked[i + 1] = true if i + 1 < n
  end
  ans
end
