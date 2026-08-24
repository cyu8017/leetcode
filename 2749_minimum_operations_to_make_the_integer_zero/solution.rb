# LeetCode 2749 - Minimum Operations to Make the Integer Zero
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def make_the_integer_zero(num1, num2)
  (1..60).each do |k|
    target = num1 - k * num2
    next if target < k
    bits = target.to_s(2).count("1")
    return k if bits <= k
  end
  -1
end
