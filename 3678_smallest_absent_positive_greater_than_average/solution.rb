# LeetCode 3678 - Smallest Absent Positive Greater Than Average
# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

# @param {Integer[]} nums
# @return {Integer}
def smallest_absent(nums)
  s = {}
  total = 0
  nums.each do |x|
    s[x] = true
    total += x
  end
  ans = [1, total / nums.length + 1].max
  ans += 1 while s[ans]
  ans
end
