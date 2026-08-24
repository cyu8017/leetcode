# LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  lst = nums.dup
  ops = 0
  loop do
    seen = {}
    dup = false
    lst.each do |x|
      if seen[x]
        dup = true
        break
      end
      seen[x] = true
    end
    return ops unless dup
    return ops + 1 if lst.length <= 3

    lst = lst[3..]
    ops += 1
  end
end
