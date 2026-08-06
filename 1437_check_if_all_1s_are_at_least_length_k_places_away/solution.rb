# LeetCode 1437 - Check If All 1S Are At Least Length K Places Away
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

def k_length_apart(nums, k)
  previous = -k - 1
  nums.each_with_index do |value, i|
    next if value == 0
    return false if i - previous <= k
    previous = i
  end
  true
end
