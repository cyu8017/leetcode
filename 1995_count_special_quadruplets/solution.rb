# LeetCode 1995 - Count Special Quadruplets
# https://leetcode.com/problems/count-special-quadruplets/

# @param {Integer[]} nums
# @return {Integer}
def count_quadruplets(nums)
  n = nums.length
  ans = 0
  n.times do |a|
    ((a + 1)...n).each do |b|
      ((b + 1)...n).each do |c|
        s = nums[a] + nums[b] + nums[c]
        ((c + 1)...n).each { |d| ans += 1 if nums[d] == s }
      end
    end
  end
  ans
end
