// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

public class Solution {
    public bool MakeStringsEqual(string s, string target) {
        bool has1s = false, has1t = false;
        for (int i = 0; i < s.Length; ++i) {
            if (s[i] == '1') has1s = true;
            if (target[i] == '1') has1t = true;
        }
        return has1s == has1t;
    }
}
