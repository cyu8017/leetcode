// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

class Solution {
    public String maximumBinaryString(String binary) {
        int zeros = 0;
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '0') {
                zeros++;
            }
        }
        if (zeros <= 1) {
            return binary;
        }
        int first = binary.indexOf('0');
        int n = binary.length();
        return "1".repeat(first + zeros - 1) + "0" + "1".repeat(n - first - zeros);
    }
}
