// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

class Solution {
    public int numberOfNodes(int n, int[] queries) {
        int[] flip = new int[n + 1], val = new int[n + 1];
        for (int q : queries) flip[q] ^= 1;
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            val[i] = flip[i];
            if (i > 1) val[i] ^= val[i / 2];
            ans += val[i];
        }
        return ans;
    }
}
