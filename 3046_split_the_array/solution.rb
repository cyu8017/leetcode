# LeetCode 3046 - Split the Array
# https://leetcode.com/problems/split-the-array/

# @param {Integer[]} nums
# @return {Boolean}
def is_possible_to_split(nums)
  cnt = Array.new(101, 0)
  nums.each do |x|
    cnt[x] += 1
    return false if cnt[x] >= 3
  end
  true
end
