# LeetCode 0989 - Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/

# @param {Integer[]} num
# @param {Integer} k
# @return {Integer[]}
def add_to_array_form(num, k)
  i = num.length - 1
  while k > 0 || i >= 0
    if i >= 0
      k += num[i]
      num[i] = k % 10
      i -= 1
    else
      num.unshift(k % 10)
    end
    k /= 10
  end
  num
end
