// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

using System.Collections.Generic;

public class Solution {
    public int MinimizedStringLength(string s) {
        return new HashSet<char>(s).Count;
    }
}
