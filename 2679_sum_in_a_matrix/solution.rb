# LeetCode 2679 - Sum in a Matrix
# https://leetcode.com/problems/sum-in-a-matrix/

# @param {Integer[][]} nums
# @return {Integer}
def matrix_sum(nums)
  nums.each(&:sort!)
  ans = 0
  n = nums[0].length
  n.times do |j|
    mx = 0
    nums.each { |row| mx = [mx, row[j]].max }
    ans += mx
  end
  ans
end
