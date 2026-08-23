// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

import java.util.*;

class Solution {
    public List<String> cellsInRange(String s) {
        List<String> ans = new ArrayList<>();
        for (char c = s.charAt(0); c <= s.charAt(3); c++)
            for (char r = s.charAt(1); r <= s.charAt(4); r++)
                ans.add("" + c + r);
        return ans;
    }
}
