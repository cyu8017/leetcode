# LeetCode 1073 - Adding Two Negabinary Numbers
# https://leetcode.com/problems/adding-two-negabinary-numbers/

# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer[]}
def add_negabinary(arr1, arr2)
  i = arr1.length - 1
  j = arr2.length - 1
  carry = 0
  ans = []
  while i >= 0 || j >= 0 || carry != 0
    total = carry
    if i >= 0
      total += arr1[i]
      i -= 1
    end
    if j >= 0
      total += arr2[j]
      j -= 1
    end
    ans << (total & 1)
    carry = -(total >> 1)
  end
  ans.pop while ans.length > 1 && ans[-1].zero?
  ans.reverse
end
