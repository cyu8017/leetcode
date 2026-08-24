# LeetCode 0779 - K-th Symbol in Grammar
# https://leetcode.com/problems/k-th-symbol-in-grammar/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def kth_grammar(n, k)
  return 0 if n == 1

  mid = 1 << (n - 2)
  return kth_grammar(n - 1, k) if k <= mid

  1 - kth_grammar(n - 1, k - mid)
end
