// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

import java.util.*;

class Solution {
    public List<Integer> circularPermutation(int n, int start) {
        int size = 1 << n;
        List<Integer> answer = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            answer.add(start ^ i ^ (i >> 1));
        }
        return answer;
    }
}

