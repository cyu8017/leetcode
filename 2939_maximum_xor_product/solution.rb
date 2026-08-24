# LeetCode 2939 - Maximum Xor Product
# https://leetcode.com/problems/maximum-xor-product/

# @param {Integer} a
# @param {Integer} b
# @param {Integer} n
# @return {Integer}
def maximum_xor_product(a, b, n)
  mod = 1_000_000_007
  aa = a
  bb = b
  (n - 1).downto(0) do |i|
    bit = 1 << i
    abit = aa & bit
    bbit = bb & bit
    if abit == bbit
      aa |= bit
      bb |= bit
    elsif aa > bb
      bb |= bit
      aa &= ~bit
    else
      aa |= bit
      bb &= ~bit
    end
  end
  ((aa % mod) * (bb % mod)) % mod
end
