// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

public class Solution {
    public bool IsAdditiveNumber(string num) {
        for (int firstEnd = 1; firstEnd < num.Length; firstEnd++) {
            for (int secondEnd = firstEnd + 1; secondEnd < num.Length; secondEnd++) {
                if (Valid(num, num[..firstEnd], num[firstEnd..secondEnd], secondEnd)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static bool Valid(string num, string first, string second, int start) {
        if ((first.Length > 1 && first[0] == '0') || (second.Length > 1 && second[0] == '0')) {
            return false;
        }
        while (start < num.Length) {
            string total = AddStrings(first, second);
            if (!num.StartsWith(total, start)) {
                return false;
            }
            first = second;
            second = total;
            start += total.Length;
        }
        return true;
    }

    private static string AddStrings(string left, string right) {
        return (long.Parse(left) + long.Parse(right)).ToString();
    }
}
