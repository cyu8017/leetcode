// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

public class Solution {
    public int[] FindEvenNumbers(int[] digits) {
        int[] freq = new int[10];
        foreach (int d in digits) freq[d]++;
        var ans = new List<int>();
        for (int x = 100; x <= 998; x += 2) {
            int a = x / 100, b = (x / 10) % 10, c = x % 10;
            freq[a]--; freq[b]--; freq[c]--;
            if (freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0) ans.Add(x);
            freq[a]++; freq[b]++; freq[c]++;
        }
        return ans.ToArray();
    }
}
