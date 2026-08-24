# LeetCode 2164 - Sort Even and Odd Indices Independently
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_even_odd(nums)
  even = []
  odd = []
  nums.each_with_index do |x, i|
    if i.even?
      even << x
    else
      odd << x
    end
  end
  even.sort!
  odd.sort!.reverse!
  ei = 0
  oi = 0
  nums.each_index do |i|
    if i.even?
      nums[i] = even[ei]
      ei += 1
    else
      nums[i] = odd[oi]
      oi += 1
    end
  end
  nums
end
