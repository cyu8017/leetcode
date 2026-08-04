// LeetCode 1331 - Rank Transform Of An Array
// https://leetcode.com/problems/rank-transform-of-an-array/

import java.util.*;

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        var sorted = new SortedSet<int>(arr);
        var rank = new HashMap<>();
        int i = 1;
        for (int value : sorted) rank[value] = i++;
        var answer = new int[arr.length];
        for (int j = 0; j < arr.length; j++) answer[j] = rank[arr[j]];
        return answer;
    }
}
