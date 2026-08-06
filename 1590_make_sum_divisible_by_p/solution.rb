# LeetCode 1590 - Make Sum Divisible by P
# https://leetcode.com/problems/make-sum-divisible-by-p/

# @param {Integer[]} nums
# @param {Integer} p
# @return {Integer}
def min_subarray(nums, p)
  target = nums.sum % p
  return 0 if target.zero?
  seen = { 0 => -1 }
  prefix = 0
  answer = nums.length
  nums.each_with_index do |x, i|
    prefix = (prefix + x) % p
    need = (prefix - target) % p
    answer = [answer, i - seen[need]].min if seen.key?(need)
    seen[prefix] = i
  end
  answer < nums.length ? answer : -1
end
