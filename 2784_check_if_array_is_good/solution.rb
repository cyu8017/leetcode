# LeetCode 2784 - Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/

# @param {Integer[]} nums
# @return {Boolean}
def is_good(nums)
  n = nums.length - 1
  return false if n < 1
  freq = Array.new(n + 1, 0)
  nums.each do |v|
    return false if v < 1 || v > n
    freq[v] += 1
  end
  (1...n).each { |i| return false if freq[i] != 1 }
  freq[n] == 2
end
