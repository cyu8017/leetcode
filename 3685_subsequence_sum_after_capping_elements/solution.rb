# LeetCode 3685 - Subsequence Sum After Capping Elements
# https://leetcode.com/problems/subsequence-sum-after-capping-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean[]}
def subsequence_sum_after_capping(nums, k)
  n = nums.length
  sorted_nums = nums.sort
  ans = Array.new(n, false)
  reach = Array.new(k + 1, false)
  reach[0] = true
  idx = 0
  (1..n).each do |x|
    while idx < n && sorted_nums[idx] <= x
      v = sorted_nums[idx]
      k.downto(v) { |s| reach[s] = true if reach[s - v] }
      idx += 1
    end
    tmp = reach.dup
    rem = n - idx
    (0..k).each do |s|
      next unless reach[s]

      t = 1
      while t <= rem && s + t * x <= k
        tmp[s + t * x] = true
        t += 1
      end
    end
    ans[x - 1] = tmp[k]
  end
  ans
end
