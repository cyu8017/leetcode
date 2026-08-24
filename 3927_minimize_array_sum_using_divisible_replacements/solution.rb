# LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
# https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

# @param {Integer[]} nums
# @return {Integer}
def min_array_sum(nums)
  maximum = 0
  present = Array.new(100001, false)
  nums.each do |value|
    present[value] = true
    maximum = value if value > maximum
  end
  best = Array.new(maximum + 1, 0)
  (1..maximum).each do |divisor|
    next unless present[divisor]
    multiple = divisor
    while multiple <= maximum
      best[multiple] = divisor if best[multiple] == 0
      multiple += divisor
    end
  end
  nums.sum { |value| best[value] }
end
