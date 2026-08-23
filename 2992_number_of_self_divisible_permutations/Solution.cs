// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

public class Solution {
    static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public int SelfDivisiblePermutationCount(int n) {
        int ans = 0;
        bool[] used = new bool[n + 1];
        void Dfs(int pos) {
            if (pos > n) {
                ans++;
                return;
            }
            for (int v = 1; v <= n; v++) {
                if (used[v]) continue;
                if (Gcd(v, pos) != 1) continue;
                used[v] = true;
                Dfs(pos + 1);
                used[v] = false;
            }
        }
        Dfs(1);
        return ans;
    }
}
