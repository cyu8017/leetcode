# LeetCode 3985 - Palindromic Subarray Sum
# https://leetcode.com/problems/palindromic-subarray-sum/

# @param {Integer[]} nums
# @return {Integer}
def max_palindromic_subarray_sum(nums)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  n.times { |i| prefix[i + 1] = prefix[i] + nums[i] }
  odd = Array.new(n, 0)
  left = 0
  right = -1
  n.times do |i|
    radius = 1
    if i <= right
      mirror = left + right - i
      radius = odd[mirror]
      radius = right - i + 1 if right - i + 1 < radius
    end
    radius += 1 while i - radius >= 0 && i + radius < n && nums[i - radius] == nums[i + radius]
    odd[i] = radius
    if i + radius - 1 > right
      left = i - radius + 1
      right = i + radius - 1
    end
  end
  even = Array.new(n, 0)
  left = 0
  right = -1
  n.times do |i|
    radius = 0
    if i <= right
      mirror = left + right - i + 1
      radius = even[mirror]
      radius = right - i + 1 if right - i + 1 < radius
    end
    radius += 1 while i - radius - 1 >= 0 && i + radius < n && nums[i - radius - 1] == nums[i + radius]
    even[i] = radius
    if i + radius - 1 > right
      left = i - radius
      right = i + radius - 1
    end
  end
  answer = 0
  n.times do |i|
    s = prefix[i + odd[i]] - prefix[i - odd[i] + 1]
    answer = s if s > answer
    if even[i] > 0
      s = prefix[i + even[i]] - prefix[i - even[i]]
      answer = s if s > answer
    end
  end
  answer
end
