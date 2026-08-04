// LeetCode 1409 - Queries On A Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

import java.util.*;

class Solution {
    public int[] processQueries(int[] queries, int m) {
        var values = new ArrayList<>();
        for (int i = 1; i <= m; i++) values.add(i);
        var answer = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int index = values.indexOf(queries[q]);
            answer[q] = index;
            values.remove(index);
            values.Insert(0, queries[q]);
        }
        return answer;
    }
}
