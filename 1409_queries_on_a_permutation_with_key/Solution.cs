// LeetCode 1409 - Queries On A Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

using System.Collections.Generic;
public class Solution {
    public int[] ProcessQueries(int[] queries, int m) {
        var values = new List<int>();
        for (int i = 1; i <= m; i++) values.Add(i);
        var answer = new int[queries.Length];
        for (int q = 0; q < queries.Length; q++) {
            int index = values.IndexOf(queries[q]);
            answer[q] = index;
            values.RemoveAt(index);
            values.Insert(0, queries[q]);
        }
        return answer;
    }
}
