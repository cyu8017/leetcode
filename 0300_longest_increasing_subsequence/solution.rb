# LeetCode 0300 - Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution
  def lengthOfLIS(nums)
    piles = []
    nums.each do |num|
      left = 0
      right = piles.length
      while left < right
        mid = (left + right) / 2
        if piles[mid] < num
          left = mid + 1
        else
          right = mid
        end
      end
      if left == piles.length
        piles << num
      else
        piles[left] = num
      end
    end
    piles.length
  end
end
