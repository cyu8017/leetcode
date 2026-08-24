# LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

# @param {Integer[]} nums
# @return {Integer}
def duplicate_numbers_xor(nums)
  cnt = Array.new(51, 0)
  ans = 0
  nums.each do |x|
    cnt[x] += 1
    ans ^= x if cnt[x] == 2
  end
  ans
end
