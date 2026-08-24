# LeetCode 0667 - Beautiful Arrangement II
# https://leetcode.com/problems/beautiful-arrangement-ii/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def construct_array(n, k)
  res = (1..(n - k)).to_a
  left = n - k + 1
  right = n
  take_high = true
  while left <= right
    if take_high
      res << right
      right -= 1
    else
      res << left
      left += 1
    end
    take_high = !take_high
  end
  res
end
