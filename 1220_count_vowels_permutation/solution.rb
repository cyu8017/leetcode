# LeetCode 1220 - Count Vowels Permutation
# https://leetcode.com/problems/count-vowels-permutation/

# @param {Integer} n
# @return {Integer}
def count_vowel_permutation(n)
  mod = 1_000_000_007
  aa = ee = ii = oo = uu = 1
  (n - 1).times do
    aa, ee, ii, oo, uu = (ee + ii + uu) % mod, (aa + ii) % mod, (ee + oo) % mod, ii, (ii + oo) % mod
  end
  (aa + ee + ii + oo + uu) % mod
end
