// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

using System.Collections.Generic;

public class Solution {
    public string[] FindRestaurant(string[] list1, string[] list2) {
        var index1 = new Dictionary<string, int>();
        for (int i = 0; i < list1.Length; ++i) index1[list1[i]] = i;
        int best = int.MaxValue;
        var answer = new List<string>();
        for (int j = 0; j < list2.Length; ++j) {
            if (!index1.TryGetValue(list2[j], out int i)) continue;
            int total = i + j;
            if (total < best) {
                best = total;
                answer.Clear();
                answer.Add(list2[j]);
            } else if (total == best) {
                answer.Add(list2[j]);
            }
        }
        return answer.ToArray();
    }
}
