# LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def is_possible_divide(nums, k)
  return false if nums.length % k != 0
  counts = Hash.new(0)
  nums.each { |x| counts[x] += 1 }
  counts.keys.sort.each do |start|
    amount = counts[start]
    next if amount.zero?
    (start...start + k).each do |value|
      return false if counts[value] < amount
      counts[value] -= amount
    end
  end
  true
end
