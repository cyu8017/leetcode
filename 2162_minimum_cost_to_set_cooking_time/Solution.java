// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

class Solution {
    private int cost(int startAt, int moveCost, int pushCost, int mins, int secs) {
        if (mins < 0 || mins > 99 || secs < 0 || secs > 99) return Integer.MAX_VALUE / 2;
        String s;
        if (mins > 0) s = mins + "" + (char) ('0' + secs / 10) + (char) ('0' + secs % 10);
        else s = Integer.toString(secs);
        char cur = (char) ('0' + startAt);
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c != cur) { ans += moveCost; cur = c; }
            ans += pushCost;
        }
        return ans;
    }

    public int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        int mins = targetSeconds / 60, secs = targetSeconds % 60;
        int ans = cost(startAt, moveCost, pushCost, mins, secs);
        if (mins > 0) ans = Math.min(ans, cost(startAt, moveCost, pushCost, mins - 1, secs + 60));
        return ans;
    }
}
