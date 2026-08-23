// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/
// JS generator stand-in using civil-day arithmetic.

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> dateRangeGenerator(String start, String end, int step) {
        String[] sp = start.split("-");
        String[] ep = end.split("-");
        if (sp.length != 3 || ep.length != 3) return new ArrayList<>();
        int y = Integer.parseInt(sp[0]), m = Integer.parseInt(sp[1]), d = Integer.parseInt(sp[2]);
        int ey = Integer.parseInt(ep[0]), em = Integer.parseInt(ep[1]), ed = Integer.parseInt(ep[2]);
        List<String> ans = new ArrayList<>();
        while (cmp(y, m, d, ey, em, ed)) {
            ans.add(String.format("%04d-%02d-%02d", y, m, d));
            int[] ymd = addDays(y, m, d, step);
            y = ymd[0];
            m = ymd[1];
            d = ymd[2];
        }
        return ans;
    }

    private boolean isLeap(int yy) {
        return (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0);
    }

    private int[] addDays(int yy, int mm, int dd, int days) {
        int[] mdays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        while (days-- > 0) {
            mdays[2] = isLeap(yy) ? 29 : 28;
            dd++;
            if (dd > mdays[mm]) {
                dd = 1;
                mm++;
            }
            if (mm > 12) {
                mm = 1;
                yy++;
            }
        }
        return new int[]{yy, mm, dd};
    }

    private boolean cmp(int y, int m, int d, int ey, int em, int ed) {
        if (y != ey) return y < ey;
        if (m != em) return m < em;
        return d <= ed;
    }
}
