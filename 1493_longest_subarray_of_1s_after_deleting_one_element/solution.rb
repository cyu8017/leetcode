# LeetCode 1493 - Longest Subarray Of 1S After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

def longest_subarray(nums)
  left = zeros = ans = 0
  nums.each_with_index do |x, right|
    zeros += 1 if x == 0
    while zeros > 1
      zeros -= 1 if nums[left] == 0
      left += 1
    end
    ans = [ans, right - left].max
  end
  ans
end
