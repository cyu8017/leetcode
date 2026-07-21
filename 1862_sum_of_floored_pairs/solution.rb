# LeetCode 1862 - Sum of Floored Pairs
# https://leetcode.com/problems/sum-of-floored-pairs/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_floored_pairs(nums)
  mod = 10**9 + 7
  max_val = nums.max
  count = Array.new(max_val + 1, 0)
  nums.each { |num| count[num] += 1 }

  prefix = Array.new(max_val + 1, 0)
  prefix[0] = count[0]
  (1..max_val).each { |value| prefix[value] = prefix[value - 1] + count[value] }

  answer = 0
  (1..max_val).each do |divisor|
    next if count[divisor] == 0

    quotient = 1
    while quotient * divisor <= max_val
      low = quotient * divisor
      high = [(quotient + 1) * divisor - 1, max_val].min
      matches = prefix[high] - (low > 0 ? prefix[low - 1] : 0)
      answer = (answer + count[divisor] * matches * quotient) % mod
      quotient += 1
    end
  end

  answer
end
