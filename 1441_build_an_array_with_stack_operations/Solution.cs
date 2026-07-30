// LeetCode 1441 - Build An Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

using System.Collections.Generic;
public class Solution {
    public IList<string> BuildArray(int[] target, int n) {
        var answer = new List<string>(); int current = 1;
        foreach (int value in target) {
            while (current < value) { answer.Add("Push"); answer.Add("Pop"); current++; }
            answer.Add("Push"); current++;
        }
        return answer;
    }
}
