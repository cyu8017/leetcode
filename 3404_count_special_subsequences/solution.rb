# LeetCode 3404 - Count Special Subsequences
# https://leetcode.com/problems/count-special-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def number_of_subsequences(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    ((i + 2)...n).each do |j|
      ((j + 2)...n).each do |k|
        ((k + 2)...n).each do |l|
          ans += 1 if nums[i] * nums[k] == nums[j] * nums[l]
        end
      end
    end
  end
  ans
end
