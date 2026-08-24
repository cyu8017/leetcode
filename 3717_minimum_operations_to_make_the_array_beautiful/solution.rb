# LeetCode 3717 - Minimum Operations to Make the Array Beautiful
# https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  f = { nums[0] => 0 }
  (1...nums.length).each do |i|
    x = nums[i]
    g = {}
    f.each do |pre, s|
      cur = ((x + pre - 1) / pre) * pre
      while cur <= 100
        val = s + (cur - x)
        old = g[cur]
        g[cur] = val if old.nil? || old > val
        cur += pre
      end
    end
    f = g
  end
  f.empty? ? 0 : f.values.min
end
