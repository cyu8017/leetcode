# LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

# @param {Integer[][]} groups
# @param {Integer[]} nums
# @return {Boolean}
def can_choose(groups, nums)
  n = nums.length
  dfs = lambda do |i, start|
    return start == n if i == groups.length
    g = groups[i]
    m = g.length
    (start..n - m).each do |j|
      return true if nums[j, m] == g && dfs.call(i + 1, j + m)
    end
    false
  end
  dfs.call(0, 0)
end
