// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

using System.Collections.Generic;

public class Solution {
    public IList<int> CircularPermutation(int n, int start) {
        var answer = new List<int>();
        for (int i = 0; i < (1 << n); i++) {
            answer.Add(start ^ i ^ (i >> 1));
        }
        return answer;
    }
}
