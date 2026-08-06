# LeetCode 1187 - Make Array Strictly Increasing
# https://leetcode.com/problems/make-array-strictly-increasing/

# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def make_array_increasing(arr1, arr2)
  arr2 = arr2.uniq.sort
  dp = { -1 => 0 }
  arr1.each do |num|
    new_dp = {}
    dp.each do |prev, ops|
      if num > prev
        new_dp[num] = [new_dp.fetch(num, Float::INFINITY), ops].min
      end
      idx = arr2.bsearch_index { |x| x > prev }
      if idx
        chosen = arr2[idx]
        new_dp[chosen] = [new_dp.fetch(chosen, Float::INFINITY), ops + 1].min
      end
    end
    dp = new_dp
    return -1 if dp.empty?
  end
  dp.values.min
end
