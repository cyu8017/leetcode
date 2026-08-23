// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/
// JS Date stand-in using civil-day arithmetic.

class Solution {
    public String nextDay(String date) {
        String[] parts = date.split("-");
        if (parts.length != 3) return date;
        int y = Integer.parseInt(parts[0]), m = Integer.parseInt(parts[1]), d = Integer.parseInt(parts[2]);
        int[] mdays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (isLeap(y)) mdays[2] = 29;
        d++;
        if (d > mdays[m]) { d = 1; m++; }
        if (m > 12) { m = 1; y++; }
        return String.format("%04d-%02d-%02d", y, m, d);
    }

    private boolean isLeap(int yy) {
        return (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0);
    }
}
