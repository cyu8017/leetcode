// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

public class Solution {
    public int DiagonalPrime(int[][] nums) {
        bool IsPrime(int x) {
            if (x < 2) return false;
            for (int i = 2; i * i <= x; ++i) if (x % i == 0) return false;
            return true;
        }
        int n = nums.Length;
        int best = 0;
        for (int i = 0; i < n; ++i) {
            foreach (int v in new[] { nums[i][i], nums[i][n - 1 - i] }) {
                if (IsPrime(v) && v > best) best = v;
            }
        }
        return best;
    }
}
