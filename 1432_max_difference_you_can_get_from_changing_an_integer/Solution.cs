// LeetCode 1432 - Max Difference You Can Get From Changing An Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

public class Solution {
    public int MaxDiff(int num) {
        string s = num.ToString(), high = s, low = s;
        foreach (char c in s) if (c != '9') { high = s.Replace(c, '9'); break; }
        if (s[0] != '1') low = s.Replace(s[0], '1');
        else for (int i = 1; i < s.Length; i++)
            if (s[i] != '0' && s[i] != '1') { low = s.Replace(s[i], '0'); break; }
        return int.Parse(high) - int.Parse(low);
    }
}
