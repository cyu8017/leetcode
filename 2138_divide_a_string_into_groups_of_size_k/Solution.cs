// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

public class Solution {
    public string[] DivideString(string s, int k, char fill) {
        var ans = new List<string>();
        for (int i = 0; i < s.Length; i += k) {
            if (i + k <= s.Length) ans.Add(s.Substring(i, k));
            else {
                string chunk = s.Substring(i);
                while (chunk.Length < k) chunk += fill;
                ans.Add(chunk);
            }
        }
        return ans.ToArray();
    }
}
