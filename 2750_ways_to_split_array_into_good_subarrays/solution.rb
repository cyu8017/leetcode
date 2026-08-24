# LeetCode 2750 - Ways to Split Array Into Good Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def number_of_good_subarray_splits(nums)
  mod = 1_000_000_007
  ones = []
  nums.each_with_index { |v, i| ones << i if v == 1 }
  return 0 if ones.empty?
  ans = 1
  (1...ones.length).each do |i|
    ans = (ans * (ones[i] - ones[i - 1])) % mod
  end
  ans
end
