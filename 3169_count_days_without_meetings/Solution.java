// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

import java.util.Arrays;

class Solution {
    public int countDays(int days, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        int last = 0, ans = 0;
        for (int[] e : meetings) {
            int st = e[0], ed = e[1];
            if (last < st) ans += st - last - 1;
            last = Math.max(last, ed);
        }
        ans += days - last;
        return ans;
    }
}
