// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

using System.Collections.Generic;

public class Solution {
    public int[] FindingUsersActiveMinutes(int[][] logs, int k) {
        var userMinutes = new Dictionary<int, HashSet<int>>();
        foreach (var log in logs) {
            int userId = log[0], minute = log[1];
            if (!userMinutes.TryGetValue(userId, out var set)) {
                set = new HashSet<int>();
                userMinutes[userId] = set;
            }
            set.Add(minute);
        }

        int[] answer = new int[k];
        foreach (var minutes in userMinutes.Values) {
            int uam = minutes.Count;
            if (uam <= k) answer[uam - 1]++;
        }
        return answer;
    }
}
