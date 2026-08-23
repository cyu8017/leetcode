// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/
// JS Date stand-in using civil-day arithmetic.

public class Solution {
    public string NextDay(string date) {
        var parts = date.Split('-');
        if (parts.Length != 3) return date;
        int y = int.Parse(parts[0]), m = int.Parse(parts[1]), d = int.Parse(parts[2]);
        bool IsLeap(int yy) => (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0);
        int[] mdays = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        if (IsLeap(y)) mdays[2] = 29;
        d++;
        if (d > mdays[m]) { d = 1; m++; }
        if (m > 12) { m = 1; y++; }
        return $"{y:D4}-{m:D2}-{d:D2}";
    }
}
