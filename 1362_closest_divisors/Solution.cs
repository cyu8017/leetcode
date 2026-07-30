// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

public class Solution {
    public int[] ClosestDivisors(int num) {
        int[] best = null;
        foreach (int x in new[] { num + 1, num + 2 }) {
            for (int a = (int)System.Math.Sqrt(x); a >= 1; a--) {
                if (x % a == 0) {
                    var pair = new[] { a, x / a };
                    if (best == null || pair[1] - pair[0] < best[1] - best[0]) best = pair;
                    break;
                }
            }
        }
        return best;
    }
}
