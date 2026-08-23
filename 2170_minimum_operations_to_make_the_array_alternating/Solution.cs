// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

public class Solution {
    public int MinimumOperations(int[] nums) {
        int n = nums.Length;
        if (n == 1) return 0;
        int[] Top2(List<int> idxs) {
            var freq = new Dictionary<int, int>();
            foreach (int i in idxs) {
                if (!freq.ContainsKey(nums[i])) freq[nums[i]] = 0;
                freq[nums[i]]++;
            }
            int a = 0, ac = 0, b = 0, bc = 0;
            foreach (var kv in freq) {
                int v = kv.Key, c = kv.Value;
                if (c > ac) { b = a; bc = ac; a = v; ac = c; }
                else if (c > bc) { b = v; bc = c; }
            }
            return new[] { a, ac, b, bc };
        }
        var even = new List<int>();
        var odd = new List<int>();
        for (int i = 0; i < n; i++) (i % 2 == 0 ? even : odd).Add(i);
        var e = Top2(even);
        var o = Top2(odd);
        if (e[0] != o[0]) return n - e[1] - o[1];
        return Math.Min(n - e[1] - o[3], n - e[3] - o[1]);
    }
}
