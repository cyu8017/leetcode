// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/
// JS generator stand-in using civil-day arithmetic.

using System.Collections.Generic;

public class Solution {
    public IList<string> DateRangeGenerator(string start, string end, int step) {
        var sp = start.Split('-');
        var ep = end.Split('-');
        if (sp.Length != 3 || ep.Length != 3) return new List<string>();
        int y = int.Parse(sp[0]), m = int.Parse(sp[1]), d = int.Parse(sp[2]);
        int ey = int.Parse(ep[0]), em = int.Parse(ep[1]), ed = int.Parse(ep[2]);
        bool IsLeap(int yy) => (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0);
        void AddDays(ref int yy, ref int mm, ref int dd, int days) {
            int[] mdays = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
            while (days-- > 0) {
                mdays[2] = IsLeap(yy) ? 29 : 28;
                dd++;
                if (dd > mdays[mm]) { dd = 1; mm++; }
                if (mm > 12) { mm = 1; yy++; }
            }
        }
        bool Cmp() {
            if (y != ey) return y < ey;
            if (m != em) return m < em;
            return d <= ed;
        }
        var ans = new List<string>();
        while (Cmp()) {
            ans.Add($"{y:D4}-{m:D2}-{d:D2}");
            AddDays(ref y, ref m, ref d, step);
        }
        return ans;
    }
}
