// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution {
    public int minMaxDifference(int num) {
        String s = Integer.toString(num);
        int maxV = num;
        for (char c : s.toCharArray()) {
            if (c != '9') {
                maxV = remap(s, c, '9');
                break;
            }
        }
        int minV = remap(s, s.charAt(0), '0');
        return maxV - minV;
    }

    private int remap(String s, char from, char to) {
        int v = 0;
        for (char c : s.toCharArray()) {
            char d = (c == from) ? to : c;
            v = v * 10 + (d - '0');
        }
        return v;
    }
}
