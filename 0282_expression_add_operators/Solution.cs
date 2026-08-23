// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

using System.Collections.Generic;

public class Solution {
    public IList<string> AddOperators(string num, int target) {
        var result = new List<string>();
        Backtrack(num, target, 0, "", 0L, 0L, result);
        return result;
    }

    private void Backtrack(
        string num,
        int target,
        int index,
        string path,
        long value,
        long previous,
        List<string> result) {
        if (index == num.Length) {
            if (value == target) {
                result.Add(path);
            }
            return;
        }

        for (int end = index; end < num.Length; end++) {
            if (end > index && num[index] == '0') {
                break;
            }
            string currentStr = num.Substring(index, end - index + 1);
            long current = long.Parse(currentStr);
            if (index == 0) {
                Backtrack(num, target, end + 1, currentStr, current, current, result);
            } else {
                Backtrack(num, target, end + 1, path + "+" + currentStr, value + current, current, result);
                Backtrack(num, target, end + 1, path + "-" + currentStr, value - current, -current, result);
                Backtrack(
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
