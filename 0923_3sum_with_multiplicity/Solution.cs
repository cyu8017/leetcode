// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

public class Solution {
    public int ThreeSumMulti(int[] arr, int target) {
        const int MOD = 1000000007;
        long[] count = new long[101];
        foreach (int x in arr) count[x]++;
        long ans = 0;
        for (int a = 0; a <= 100; a++) if (count[a] > 0) {
            for (int b = a; b <= 100; b++) if (count[b] > 0) {
                int c = target - a - b;
                if (c < b || c > 100 || count[c] == 0) continue;
                if (a == b && b == c) ans += count[a] * (count[a] - 1) * (count[a] - 2) / 6;
                else if (a == b) ans += count[a] * (count[a] - 1) / 2 * count[c];
                else if (b == c) ans += count[a] * count[b] * (count[b] - 1) / 2;
                else ans += count[a] * count[b] * count[c];
            }
        }
        return (int)(ans % MOD);
    }
}
