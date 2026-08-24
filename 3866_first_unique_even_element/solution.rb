# LeetCode 3866 - First Unique Even Element
# https://leetcode.com/problems/first-unique-even-element/

# @param {Integer[]} nums
# @return {Integer}
def first_unique_even(nums)
  cnt = Array.new(101, 0)
  nums.each { |x| cnt[x] += 1 }
  nums.each { |x| return x if x.even? && cnt[x] == 1 }
  -1
end
