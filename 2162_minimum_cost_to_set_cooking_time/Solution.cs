// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

public class Solution {
    public int MinCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        int Cost(int mins, int secs) {
            if (mins < 0 || mins > 99 || secs < 0 || secs > 99) return int.MaxValue / 2;
            string s;
            if (mins > 0) {
                s = mins.ToString() + (char)('0' + secs / 10) + (char)('0' + secs % 10);
            } else s = secs.ToString();
            char cur = (char)('0' + startAt);
            int ans = 0;
            foreach (char c in s) {
                if (c != cur) { ans += moveCost; cur = c; }
                ans += pushCost;
            }
            return ans;
        }
        int mins = targetSeconds / 60, secs = targetSeconds % 60;
        int ans = Cost(mins, secs);
        if (mins > 0) ans = Math.Min(ans, Cost(mins - 1, secs + 60));
        return ans;
    }
}
