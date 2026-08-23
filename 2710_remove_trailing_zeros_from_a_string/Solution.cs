// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

public class Solution {
    public string RemoveTrailingZeros(string num) {
        int end = num.Length;
        while (end > 0 && num[end - 1] == '0') end--;
        return num.Substring(0, end);
    }
}
