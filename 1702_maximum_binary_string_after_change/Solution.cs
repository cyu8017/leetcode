// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

public class Solution {
    public string MaximumBinaryString(string binary) {
        int zeros = 0;
        foreach (char ch in binary) {
            if (ch == '0') {
                zeros++;
            }
        }
        if (zeros <= 1) {
            return binary;
        }
        int first = binary.IndexOf('0');
        int n = binary.Length;
        return new string('1', first + zeros - 1) + "0" + new string('1', n - first - zeros);
    }
}
