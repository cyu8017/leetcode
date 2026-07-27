# LeetCode 1664 - Ways to Make a Fair Array
# https://leetcode.com/problems/ways-to-make-a-fair-array/

# @param {Integer[]} nums
# @return {Integer}
def ways_to_make_fair(nums)
  te = nums.each_with_index.sum { |x, i| i.even? ? x : 0 }
  to = nums.each_with_index.sum { |x, i| i.odd? ? x : 0 }
  le = 0
  lo = 0
  ans = 0
  nums.each_with_index do |x, i|
    if i.odd?
      to -= x
    else
      te -= x
    end
    ans += 1 if le + to == lo + te
    if i.odd?
      lo += x
    else
      le += x
    end
  end
  ans
end
