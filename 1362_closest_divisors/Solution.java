// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

class Solution {
    public int[] closestDivisors(int num) {
        int[] best = null;
        for (int x : new int[]{ num + 1, num + 2 }) {
            for (int a = (int)Math.Sqrt(x); a >= 1; a--) {
                if (x % a == 0) {
                    var pair = new int[]{ a, x / a };
                    if (best == null || pair[1] - pair[0] < best[1] - best[0]) best = pair;
                    break;
                }
            }
        }
        return best;
    }
}
