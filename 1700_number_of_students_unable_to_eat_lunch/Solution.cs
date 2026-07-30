// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

using System.Collections.Generic;

public class Solution {
    public int CountStudents(int[] students, int[] sandwiches) {
        var c = new Dictionary<int, int>();
        foreach (var s in students) {
            if (!c.ContainsKey(s)) c[s] = 0;
            c[s]++;
        }
        for (int i = 0; i < sandwiches.Length; i++) {
            int x = sandwiches[i];
            if (!c.ContainsKey(x) || c[x] == 0) return students.Length - i;
            c[x]--;
        }
        return 0;
    }
}