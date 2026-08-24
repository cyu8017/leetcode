# LeetCode 2870 - Minimum Number of Operations to Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  freq = {}
  nums.each { |v| freq[v] = freq.fetch(v, 0) + 1 }
  ans = 0
  freq.each_value do |c|
    return -1 if c == 1

    ans += (c + 2) / 3
  end
  ans
end
