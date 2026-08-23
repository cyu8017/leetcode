// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

public class Solution {
    public long CountPairs(int[] nums, int k) {
        int Gcd(int a, int b) { while (b != 0) { int t = a % b; a = b; b = t; } return a; }
        var freq = new Dictionary<int, int>();
        long ans = 0;
        foreach (int x in nums) {
            int g1 = Gcd(x, k);
            foreach (var kv in freq)
                if (1L * g1 * kv.Key % k == 0) ans += kv.Value;
            if (!freq.ContainsKey(g1)) freq[g1] = 0;
            freq[g1]++;
        }
        return ans;
    }
}
