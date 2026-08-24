# LeetCode 2191 - Sort the Jumbled Numbers
# https://leetcode.com/problems/sort-the-jumbled-numbers/

# @param {Integer[]} mapping
# @param {Integer[]} nums
# @return {Integer[]}
def sort_jumbled(mapping, nums)
  map_val = lambda do |x|
    return mapping[0] if x == 0

    digits = []
    while x > 0
      digits << x % 10
      x /= 10
    end
    res = 0
    (digits.length - 1).downto(0) { |i| res = res * 10 + mapping[digits[i]] }
    res
  end

  arr = nums.each_with_index.map { |v, i| [map_val.call(v), i, v] }
  arr.sort_by! { |x| [x[0], x[1]] }
  arr.map { |x| x[2] }
end
