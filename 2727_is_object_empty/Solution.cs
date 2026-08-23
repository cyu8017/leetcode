// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

using System.Collections.Generic;

public class Solution {
    public bool IsEmpty(Dictionary<string, int> obj) {
        return obj.Count == 0;
    }

    public bool IsEmpty(int[] arr) {
        return arr.Length == 0;
    }
}
