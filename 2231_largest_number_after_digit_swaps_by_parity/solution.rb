# LeetCode 2231 - Largest Number After Digit Swaps by Parity
# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

# @param {Integer} num
# @return {Integer}
def largest_integer(num)
  digits = num.to_s.chars.map(&:to_i)
  even = digits.select(&:even?).sort.reverse
  odd = digits.select(&:odd?).sort.reverse
  ei = oi = 0
  ans = 0
  digits.each do |d|
    if d.even?
      ans = ans * 10 + even[ei]
      ei += 1
    else
      ans = ans * 10 + odd[oi]
      oi += 1
    end
  end
  ans
end
