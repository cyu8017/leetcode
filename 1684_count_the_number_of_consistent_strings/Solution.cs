// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int CountConsistentStrings(string allowed, string[] words) {
        var a = new HashSet<char>(allowed);
        return words.Count(w => w.All(c => a.Contains(c)));
    }
}
