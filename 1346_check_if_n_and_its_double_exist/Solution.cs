// LeetCode 1346 - Check If N And Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

using System.Collections.Generic;
public class Solution {
    public bool CheckIfExist(int[] arr) {
        var seen = new HashSet<int>();
        foreach (int value in arr) {
            if (seen.Contains(2 * value) || (value % 2 == 0 && seen.Contains(value / 2))) return true;
            seen.Add(value);
        }
        return false;
    }
}
