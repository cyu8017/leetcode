# LeetCode 1224 - Maximum Equal Frequency
# https://leetcode.com/problems/maximum-equal-frequency/

# @param {Integer[]} nums
# @return {Integer}
def max_equal_freq(nums)
  count = Hash.new(0)
  frequencies = Hash.new(0)
  answer = 0
  nums.each_with_index do |x, idx|
    i = idx + 1
    old = count[x]
    frequencies[old] -= 1 if old > 0
    count[x] += 1
    frequencies[old + 1] += 1
    high = frequencies.keys.select { |k| frequencies[k] > 0 }.max
    if high == 1 || frequencies[high] * high + 1 == i || (frequencies[high] == 1 && frequencies[high - 1] * (high - 1) + high == i)
      answer = i
    end
  end
  answer
end
