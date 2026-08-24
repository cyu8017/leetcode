# LeetCode 2229 - Check if an Array Is Consecutive
# https://leetcode.com/problems/check-if-an-array-is-consecutive/

# @param {Integer[]} nums
# @return {Boolean}
def is_consecutive(nums)
  mn = mx = nums[0]
  seen = {}
  nums.each do |x|
    return false if seen.key?(x)

    seen[x] = true
    mn = [mn, x].min
    mx = [mx, x].max
  end
  mx - mn + 1 == nums.length
end

alias solve is_consecutive
