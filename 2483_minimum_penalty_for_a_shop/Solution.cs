// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

public class Solution {
    public int BestClosingTime(string customers) {
        int n = customers.Length;
        int penalty = 0;
        foreach (char c in customers) if (c == 'Y') penalty++;
        int best = penalty, ans = 0;
        for (int i = 0; i < n; i++) {
            if (customers[i] == 'Y') penalty--;
            else penalty++;
            if (penalty < best) {
                best = penalty;
                ans = i + 1;
            }
        }
        return ans;
    }
}
