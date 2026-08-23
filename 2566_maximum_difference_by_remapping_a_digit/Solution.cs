// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

public class Solution {
    public int MinMaxDifference(int num) {
        string s = num.ToString();
        int Remap(char from, char to) {
            int v = 0;
            foreach (char c in s) {
                char d = (c == from) ? to : c;
                v = v * 10 + (d - '0');
            }
            return v;
        }
        int maxV = num;
        foreach (char c in s) {
            if (c != '9') {
                maxV = Remap(c, '9');
                break;
            }
        }
        int minV = Remap(s[0], '0');
        return maxV - minV;
    }
}
