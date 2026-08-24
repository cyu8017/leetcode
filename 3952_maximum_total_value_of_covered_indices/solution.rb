# LeetCode 3952 - Maximum Total Value of Covered Indices
# https://leetcode.com/problems/maximum-total-value-of-covered-indices/

# @param {Integer[]} nums
# @param {String} s
# @return {Integer}
def max_total_value(nums, s)
  answer = 0
  i = 0
  while i < s.length
    if s[i] == "0"
      i += 1
      next
    end
    start = i
    i += 1 while i < s.length && s[i] == "1"
    finish = i - 1
    if start == 0
      (start..finish).each { |index| answer += nums[index] }
      next
    end
    minimum = nums[start - 1]
    total = 0
    ((start - 1)..finish).each do |index|
      total += nums[index]
      minimum = nums[index] if nums[index] < minimum
    end
    answer += total - minimum
  end
  answer
end
