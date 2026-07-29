// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

int kthGrammar(int n, int k) {
    (void)n;
    int x = k - 1, bits = 0;
    while (x) { bits += x & 1; x >>= 1; }
    return bits & 1;
}
