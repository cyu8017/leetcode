# LeetCode 1089 - Duplicate Zeros
# https://leetcode.com/problems/duplicate-zeros/

# @param {Integer[]} arr
# @return {Void} Do not return anything, modify arr in-place instead.
def duplicate_zeros(arr)
  zeros = arr.count(0)
  n = arr.length
  (n - 1).downto(0) do |i|
    if i + zeros < n
      arr[i + zeros] = arr[i]
    end
    next unless arr[i].zero?

    zeros -= 1
    arr[i + zeros] = 0 if i + zeros < n
  end
end
