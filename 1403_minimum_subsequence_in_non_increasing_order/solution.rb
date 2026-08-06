# LeetCode 1403 - Minimum Subsequence In Non Increasing Order
# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

def min_subsequence(nums)
  answer = []
  chosen = 0
  total = nums.sum
  nums.sort.reverse_each do |value|
    answer << value
    chosen += value
    return answer if chosen > total - chosen
  end
  answer
end
