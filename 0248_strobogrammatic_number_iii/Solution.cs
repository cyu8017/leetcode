// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

using System.Collections.Generic;

public class Solution {
    private static readonly (string Start, string End)[] Pairs = {
        ("0", "0"),
        ("1", "1"),
        ("6", "9"),
        ("8", "8"),
        ("9", "6"),
    };

    public int StrobogrammaticInRange(string low, string high) {
        long lowValue = long.Parse(low);
        long highValue = long.Parse(high);
        int count = 0;

        for (int length = low.Length; length <= high.Length; length++) {
            foreach (string value in Build(0, length - 1)) {
                long numeric = long.Parse(value);
                if (lowValue <= numeric && numeric <= highValue) {
                    count++;
                }
            }
        }
        return count;
    }

    private IList<string> Build(int left, int right) {
        if (left > right) {
            return new List<string> { "" };
        }
        if (left == right) {
            return new List<string> { "0", "1", "8" };
        }

        List<string> result = new List<string>();
        foreach ((string start, string end) in Pairs) {
            if (left == 0 && start == "0") {
                continue;
            }
            foreach (string middle in Build(left + 1, right - 1)) {
                result.Add(start + middle + end);
            }
        }
        return result;
    }
}
