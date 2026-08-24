# LeetCode 2025 - Maximum Number of Ways to Partition an Array
# https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def ways_to_partition(nums, k)
  n = nums.length
  pref = Array.new(n, 0)
  pref[0] = nums[0]
  (1...n).each { |i| pref[i] = pref[i - 1] + nums[i] }
  total = pref[n - 1]
  right = Hash.new(0)
  left = Hash.new(0)
  (0...n - 1).each { |i| right[pref[i]] += 1 }
  ans = 0
  ans = right[total / 2] if total.even?
  n.times do |i|
    diff = k - nums[i]
    new_total = total + diff
    cur = 0
    if new_total.even?
      half = new_total / 2
      cur = left[half] + right[half - diff]
    end
    ans = [ans, cur].max
    if i < n - 1
      left[pref[i]] += 1
      right[pref[i]] -= 1
    end
  end
  ans
end
