// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] TopStudents(string[] positive_feedback, string[] negative_feedback, string[] report, int[] student_id, int k) {
        var pos = new HashSet<string>(positive_feedback);
        var neg = new HashSet<string>(negative_feedback);
        var arr = new (int id, int score)[report.Length];
        for (int i = 0; i < report.Length; i++) {
            int score = 0;
            foreach (string w in report[i].Split(' ', StringSplitOptions.RemoveEmptyEntries)) {
                if (pos.Contains(w)) score += 3;
                else if (neg.Contains(w)) score--;
            }
            arr[i] = (student_id[i], score);
        }
        Array.Sort(arr, (a, b) => {
            if (a.score != b.score) return b.score.CompareTo(a.score);
            return a.id.CompareTo(b.id);
        });
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) ans[i] = arr[i].id;
        return ans;
    }
}
