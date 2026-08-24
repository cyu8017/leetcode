# LeetCode 3640 - Trionic Array II
# https://leetcode.com/problems/trionic-array-ii/

# @param {Integer[]} nums
# @return {Integer}
def max_sum_trionic(nums)
  n = nums.length
  i = 0
  ans = -Float::INFINITY
  while i < n
    l = i
    i += 1
    i += 1 while i < n && nums[i - 1] < nums[i]
    next if i == l + 1

    p = i - 1
    s = nums[p - 1] + nums[p]
    while i < n && nums[i - 1] > nums[i]
      s += nums[i]
      i += 1
    end
    next if i == p + 1 || i == n || nums[i - 1] == nums[i]

    q = i - 1
    s += nums[i]
    i += 1
    mx = 0
    t = 0
    while i < n && nums[i - 1] < nums[i]
      t += nums[i]
      i += 1
      mx = t if t > mx
    end
    s += mx
    mx = 0
    t = 0
    (p - 2).downto(l) do |j|
      t += nums[j]
      mx = t if t > mx
    end
    s += mx
    ans = s if s > ans
    i = q
  end
  ans.to_i
end
