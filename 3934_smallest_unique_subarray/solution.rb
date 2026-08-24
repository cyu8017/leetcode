# LeetCode 3934 - Smallest Unique Subarray
# https://leetcode.com/problems/smallest-unique-subarray/

# @param {Integer[]} nums
# @return {Integer}
def smallest_unique_subarray(nums)
  base = 19
  modulo = 10**9 + 7
  powers = Array.new(nums.length + 1, 1)
  min_possible_len = nums.length
  min_len = 1
  max_len = nums.length
  while min_len <= max_len
    mid_len = (min_len + max_len) / 2
    powers[0] = 1
    (1..nums.length).each do |idx|
      powers[idx] = (powers[idx - 1] * base) % modulo
    end
    current_hash = 0
    mid_len.times do |idx|
      current_hash *= base
      current_hash += nums[idx]
      current_hash %= modulo
    end
    hash_values = {}
    hash_values[current_hash] = 1
    (1..(nums.length - mid_len)).each do |idx|
      current_hash -= powers[mid_len - 1] * nums[idx - 1]
      current_hash *= base
      current_hash += nums[idx + mid_len - 1]
      current_hash %= modulo
      hash_values[current_hash] = hash_values.fetch(current_hash, 0) + 1
    end
    if hash_values.value?(1)
      min_possible_len = mid_len if mid_len < min_possible_len
      max_len = mid_len - 1
    else
      min_len = mid_len + 1
    end
  end
  min_possible_len
end
