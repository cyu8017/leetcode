// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<>();

        backtrack(num, target, 0, "", 0L, 0L, result);
        return result;
    }

    private void backtrack(
            String num,
            int target,
            int index,
            String path,
            long value,
            long previous,
            List<String> result) {
        if (index == num.length()) {
            if (value == target) {
                result.add(path);
            }
            return;
        }

        for (int end = index; end < num.length(); end++) {
            if (end > index && num.charAt(index) == '0') {
                break;
            }
            String currentStr = num.substring(index, end + 1);
            long current = Long.parseLong(currentStr);
            if (index == 0) {
                backtrack(num, target, end + 1, currentStr, current, current, result);
            } else {
                backtrack(num, target, end + 1, path + "+" + currentStr, value + current, current, result);
                backtrack(num, target, end + 1, path + "-" + currentStr, value - current, -current, result);
                backtrack(
                        num,
                        target,
                        end + 1,
                        path + "*" + currentStr,
                        value - previous + previous * current,
                        previous * current,
                        result);
            }
        }
    }
}
