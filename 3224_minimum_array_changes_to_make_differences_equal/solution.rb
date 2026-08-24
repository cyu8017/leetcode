# LeetCode 3224 - Minimum Array Changes to Make Differences Equal
# https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_changes(nums, k)
  d = Array.new(k + 2, 0)
  n = nums.length
  (0...(n / 2)).each do |i|
    x = nums[i]
    y = nums[n - 1 - i]
    x, y = y, x if x > y
    d[0] += 1
    d[y - x] -= 1
    d[y - x + 1] += 1
    mx = [y, k - x].max
    d[mx + 1] -= 1
    d[mx + 1] += 2
  end
  ans = n
  s = 0
  d.each do |x|
    s += x
    ans = [ans, s].min
  end
  ans
end
