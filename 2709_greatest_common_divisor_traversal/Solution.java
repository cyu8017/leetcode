// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

class Solution {
    private int[] parent;

    public boolean canTraverseAllPairs(int[] nums) {
        int n = nums.length;
        if (n == 1) return true;
        int mx = nums[0];
        for (int x : nums) if (x > mx) mx = x;
        parent = new int[mx + 1];
        for (int i = 0; i <= mx; i++) parent[i] = i;
        boolean[] has = new boolean[mx + 1];
        for (int x : nums) {
            if (x == 1) return false;
            has[x] = true;
        }
        int[] sieve = new int[mx + 1];
        for (int i = 2; i <= mx; i++) {
            if (sieve[i] == 0) {
                for (int j = i; j <= mx; j += i) {
                    if (sieve[j] == 0) sieve[j] = i;
                    if (has[j]) unite(i, j);
                }
            }
        }
        int root = find(nums[0]);
        for (int x : nums) if (find(x) != root) return false;
        return true;
    }

    private int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    private void unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra != rb) parent[ra] = rb;
    }
}
