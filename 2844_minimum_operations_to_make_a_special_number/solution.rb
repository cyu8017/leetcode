# LeetCode 2844 - Minimum Operations to Make a Special Number
# https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

# @param {String} num
# @return {Integer}
def minimum_operations(num)
  n = num.length
  ans = n
  ans = [ans, n - 1].min if num.include?("0")
  %w[00 25 50 75].each do |t|
    j = n - 1
    j -= 1 while j >= 0 && num[j] != t[1]
    next if j < 0

    i = j - 1
    i -= 1 while i >= 0 && num[i] != t[0]
    next if i < 0

    ans = [ans, n - i - 2].min
  end
  ans
end
