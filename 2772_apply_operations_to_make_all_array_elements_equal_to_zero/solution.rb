# LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
# https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_array(nums, k)
  n = nums.length
  diff = Array.new(n + 1, 0)
  cur = 0
  (0...n).each do |i|
    cur += diff[i]
    need = nums[i] - cur
    return false if need < 0
    if need > 0
      return false if i + k > n
      cur += need
      diff[i + k] -= need
    end
  end
  true
end
