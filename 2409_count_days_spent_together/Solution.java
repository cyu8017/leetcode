// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

class Solution {
    private static final int[] DAYS = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int a1 = toDay(arriveAlice), a2 = toDay(leaveAlice);
        int b1 = toDay(arriveBob), b2 = toDay(leaveBob);
        int start = Math.max(a1, b1);
        int end = Math.min(a2, b2);
        if (end < start) return 0;
        return end - start + 1;
    }

    private int toDay(String s) {
        int m = (s.charAt(0) - '0') * 10 + (s.charAt(1) - '0');
        int d = (s.charAt(3) - '0') * 10 + (s.charAt(4) - '0');
        int res = d;
        for (int i = 0; i < m - 1; i++) res += DAYS[i];
        return res;
    }
}
