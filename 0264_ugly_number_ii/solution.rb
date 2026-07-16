# LeetCode 0264 - Ugly Number II
# https://leetcode.com/problems/ugly-number-ii/

# @param {Integer} n
# @return {Integer}
def nth_ugly_number(n)
  ugly = [1]
  index2 = 0
  index3 = 0
  index5 = 0
  while ugly.length < n
    next_ugly = [ugly[index2] * 2, ugly[index3] * 3, ugly[index5] * 5].min
    index2 += 1 if next_ugly == ugly[index2] * 2
    index3 += 1 if next_ugly == ugly[index3] * 3
    index5 += 1 if next_ugly == ugly[index5] * 5
    ugly << next_ugly
  end
  ugly.last
end
