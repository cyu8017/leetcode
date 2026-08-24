# LeetCode 2154 - Keep Multiplying Found Values by Two
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

# @param {Integer[]} nums
# @param {Integer} original
# @return {Integer}
def find_final_value(nums, original)
  have = {}
  nums.each { |x| have[x] = true }
  original *= 2 while have[original]
  original
end
