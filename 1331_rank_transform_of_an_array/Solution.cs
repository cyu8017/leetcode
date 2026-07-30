// LeetCode 1331 - Rank Transform Of An Array
// https://leetcode.com/problems/rank-transform-of-an-array/

using System.Collections.Generic;

public class Solution {
    public int[] ArrayRankTransform(int[] arr) {
        var sorted = new SortedSet<int>(arr);
        var rank = new Dictionary<int, int>();
        int i = 1;
        foreach (int value in sorted) rank[value] = i++;
        var answer = new int[arr.Length];
        for (int j = 0; j < arr.Length; j++) answer[j] = rank[arr[j]];
        return answer;
    }
}
