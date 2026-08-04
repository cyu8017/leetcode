// LeetCode 1441 - Build An Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

import java.util.*;

class Solution {
    public List<String> buildArray(int[] target, int n) {
        var answer = new ArrayList<>(); int current = 1;
        for (int value : target) {
            while (current < value) { answer.add("Push"); answer.add("Pop"); current++; }
            answer.add("Push"); current++;
        }
        return answer;
    }
}
