// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

public class Solution {
    public int ShareCandies(int[] candies, int k) {
        int n = candies.Length;
        var freq = new Dictionary<int, int>();
        foreach (int c in candies) {
            if (!freq.ContainsKey(c)) freq[c] = 0;
            freq[c]++;
        }
        if (k == 0) return freq.Count;
        for (int i = 0; i < k; i++) {
            if (--freq[candies[i]] == 0) freq.Remove(candies[i]);
        }
        int ans = freq.Count;
        for (int i = k; i < n; i++) {
            if (!freq.ContainsKey(candies[i - k])) freq[candies[i - k]] = 0;
            freq[candies[i - k]]++;
            if (--freq[candies[i]] == 0) freq.Remove(candies[i]);
            ans = Math.Max(ans, freq.Count);
        }
        return ans;
    }
}
