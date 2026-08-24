// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution {
    fun kthGrammar(n: Int, k: Int): Int {
        if (n == 1) return 0
        var mid = 1  shl  (n - 2)
        if (k <= mid) return kthGrammar(n - 1, k)
        return 1 - kthGrammar(n - 1, k - mid)
    }
}
