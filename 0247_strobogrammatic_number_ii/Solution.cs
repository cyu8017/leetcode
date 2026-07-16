// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

using System.Collections.Generic;

public class Solution {
    private static readonly (string Start, string End)[] Pairs = {
        ("0", "0"),
        ("1", "1"),
        ("6", "9"),
        ("8", "8"),
        ("9", "6"),
    };

    public IList<string> FindStrobogrammatic(int n) {
        return Build(0, n - 1);
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
