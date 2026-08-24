# LeetCode 3583 - Count Special Triplets
# https://leetcode.com/problems/count-special-triplets/

# @param {Integer[]} nums
# @return {Integer}
def special_triplets(nums)
  left = {}
  right = {}
  nums.each { |x| right[x] = (right[x] || 0) + 1 }
  ans = 0
  mod = 1000000007
  nums.each do |x|
    right[x] -= 1
    lv = left[x * 2] || 0
    rv = right[x * 2] || 0
    ans = (ans + lv * rv % mod) % mod
    left[x] = (left[x] || 0) + 1
  end
  ans
end
