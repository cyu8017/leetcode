// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

public class Solution {
    public int KthGrammar(int n, int k) {
        if (n == 1) return 0;
        int mid = 1 << (n - 2);
        if (k <= mid) return KthGrammar(n - 1, k);
        return 1 - KthGrammar(n - 1, k - mid);
    }
}
