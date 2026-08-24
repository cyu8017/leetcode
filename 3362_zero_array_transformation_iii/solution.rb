# LeetCode 3362 - Zero Array Transformation III
# https://leetcode.com/problems/zero-array-transformation-iii/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def max_removal(nums, queries)
  queries.sort_by! { |a| a[0] }
  h = []
  n = nums.length
  diff = Array.new(n + 1, 0)
  j = 0
  used = 0
  cur = 0
  n.times do |i|
    cur += diff[i]
    while j < queries.length && queries[j][0] == i
      h << queries[j][1]
      j += 1
    end
    while cur < nums[i]
      return -1 if h.empty?

      h.sort!.reverse!
      return -1 if h[0] < i

      r = h.shift
      cur += 1
      diff[r + 1] -= 1
      used += 1
    end
  end
  queries.length - used
end
