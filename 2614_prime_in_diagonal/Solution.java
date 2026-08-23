// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

class Solution {
    public int diagonalPrime(int[][] nums) {
        int n = nums.length;
        int best = 0;
        for (int i = 0; i < n; ++i) {
            int a = nums[i][i], b = nums[i][n - 1 - i];
            if (isPrime(a) && a > best) best = a;
            if (isPrime(b) && b > best) best = b;
        }
        return best;
    }

    private boolean isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; ++i) if (x % i == 0) return false;
        return true;
    }
}
