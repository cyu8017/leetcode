# LeetCode 3718 - Smallest Missing Multiple of K
# https://leetcode.com/problems/smallest-missing-multiple-of-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def missing_multiple(nums, k)
  s = {}
  nums.each { |x| s[x] = true }
  i = 1
  loop do
    x = k * i
    return x unless s[x]

    i += 1
  end
end
