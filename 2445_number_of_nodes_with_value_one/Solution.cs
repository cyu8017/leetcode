// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

public class Solution {
    public int NumberOfNodes(int n, int[] queries) {
        int[] flip = new int[n + 1], val = new int[n + 1];
        foreach (int q in queries) flip[q] ^= 1;
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            val[i] = flip[i];
            if (i > 1) val[i] ^= val[i / 2];
            ans += val[i];
        }
        return ans;
    }
}
