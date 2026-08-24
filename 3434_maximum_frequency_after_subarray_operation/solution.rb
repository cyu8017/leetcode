# LeetCode 3434 - Maximum Frequency After Subarray Operation
# https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_frequency(nums, k)
  base = 0
  nums.each { |x| base += 1 if x == k }
  ans = base
  uniq = {}
  nums.each { |x| uniq[x] = true }
  uniq.each_key do |v|
    next if v == k

    best = 0
    cur = 0
    nums.each do |x|
      delta = 0
      if x == v
        delta = 1
      elsif x == k
        delta = -1
      end
      cur += delta
      cur = 0 if cur < 0
      best = cur if cur > best
    end
    ans = base + best if base + best > ans
  end
  ans
end
