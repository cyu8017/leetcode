# LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

# @param {Integer[]} nums
# @return {Integer}
def min_swaps(nums)
  f = lambda do |x|
    s = 0
    while x != 0
      s += x % 10
      x /= 10
    end
    s
  end
  n = nums.length
  arr = (0...n).map { |i| [f.call(nums[i]), nums[i]] }
  arr.sort_by! { |x| [x[0], x[1]] }
  d = {}
  (0...n).each { |i| d[arr[i][1]] = i }
  vis = Array.new(n, false)
  ans = n
  (0...n).each do |i|
    next if vis[i]
    ans -= 1
    j = i
    until vis[j]
      vis[j] = true
      j = d[nums[j]]
    end
  end
  ans
end
