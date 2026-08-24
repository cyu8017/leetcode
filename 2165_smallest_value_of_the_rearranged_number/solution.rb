# LeetCode 2165 - Smallest Value of the Rearranged Number
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

# @param {Integer} num
# @return {Integer}
def smallest_number(num)
  neg = num < 0
  num = -num if neg
  return 0 if num == 0

  digits = []
  while num > 0
    digits << num % 10
    num /= 10
  end
  if neg
    digits.sort!.reverse!
    ans = 0
    digits.each { |d| ans = ans * 10 + d }
    return -ans
  end
  digits.sort!
  if digits[0] == 0
    (1...digits.length).each do |i|
      next if digits[i] == 0

      digits[0], digits[i] = digits[i], digits[0]
      break
    end
  end
  res = 0
  digits.each { |d| res = res * 10 + d }
  res
end
