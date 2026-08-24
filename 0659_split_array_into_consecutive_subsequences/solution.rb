# LeetCode 0659 - Split Array into Consecutive Subsequences
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

# @param {Integer[]} nums
# @return {Boolean}
def is_possible(nums)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  tails = Hash.new(0)

  nums.each do |num|
    next if freq[num].zero?

    freq[num] -= 1
    if tails[num - 1] > 0
      tails[num - 1] -= 1
      tails[num] += 1
    elsif freq[num + 1] > 0 && freq[num + 2] > 0
      freq[num + 1] -= 1
      freq[num + 2] -= 1
      tails[num + 2] += 1
    else
      return false
    end
  end
  true
end
