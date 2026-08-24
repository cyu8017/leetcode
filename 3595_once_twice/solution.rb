# LeetCode 3595 - Once Twice
# https://leetcode.com/problems/once-twice/

# @param {Integer[]} nums
# @return {Integer[]}
def once_twice(nums)
  freq = {}
  nums.each { |x| freq[x] = (freq[x] || 0) + 1 }
  a = 0
  b = 0
  freq.each do |key, v|
    if v == 1
      a = key
    elsif v == 2
      b = key
    end
  end
  [a, b]
end
