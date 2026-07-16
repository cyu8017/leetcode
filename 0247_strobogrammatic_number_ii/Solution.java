// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final String[][] PAIRS = {
        {"0", "0"},
        {"1", "1"},
        {"6", "9"},
        {"8", "8"},
        {"9", "6"},
    };

    public List<String> findStrobogrammatic(int n) {
        return build(0, n - 1);
    }

    private List<String> build(int left, int right) {
        if (left > right) {
            List<String> empty = new ArrayList<>();
            empty.add("");
            return empty;
        }
        if (left == right) {
            List<String> middle = new ArrayList<>();
            middle.add("0");
            middle.add("1");
            middle.add("8");
            return middle;
        }

        List<String> result = new ArrayList<>();
        for (String[] pair : PAIRS) {
            String start = pair[0];
            String end = pair[1];
            if (left == 0 && start.equals("0")) {
                continue;
            }
            for (String middle : build(left + 1, right - 1)) {
                result.add(start + middle + end);
            }
        }
        return result;
    }
}
