// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

using System.Collections.Generic;

public class Solution {
    public int NumRabbits(int[] answers) {
        var counts = new Dictionary<int, int>();
        foreach (int answer in answers) {
            if (!counts.ContainsKey(answer)) counts[answer] = 0;
            counts[answer]++;
        }
        int total = 0;
        foreach (var kv in counts) {
            int group = kv.Key + 1;
            int groups = (kv.Value + group - 1) / group;
            total += groups * group;
        }
        return total;
    }
}
