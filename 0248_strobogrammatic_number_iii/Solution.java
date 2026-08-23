// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

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

    public int strobogrammaticInRange(String low, String high) {
        long lowValue = Long.parseLong(low);
        long highValue = Long.parseLong(high);
        int count = 0;

        for (int length = low.length(); length <= high.length(); length++) {
            for (String value : build(0, length - 1)) {
                long numeric = Long.parseLong(value);
                if (lowValue <= numeric && numeric <= highValue) {
                    count++;
                }
            }
        }
        return count;
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
