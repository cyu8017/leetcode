// LeetCode 1253 - Reconstruct a 2 Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

import java.util.*;

class Solution {
    public List<List<Integer>> reconstructMatrix(int upper, int lower, int[] colsum) {
        int n = colsum.length;
        int[] top = new int[n], bottom = new int[n];
        for (int i = 0; i < n; i++) {
            if (colsum[i] == 2) {
                top[i] = bottom[i] = 1;
                upper--;
                lower--;
            }
        }
        if (upper < 0 || lower < 0) return new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (colsum[i] == 1) {
                if (upper > 0) {
                    top[i] = 1;
                    upper--;
                } else if (lower > 0) {
                    bottom[i] = 1;
                    lower--;
                } else {
                    return new ArrayList<>();
                }
            }
        }
        if (upper != 0 || lower != 0) return new ArrayList<>();
        List<List<Integer>> answer = new ArrayList<>();
        answer.add(toList(top));
        answer.add(toList(bottom));
        return answer;
    }

    private List<Integer> toList(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int x : arr) list.add(x);
        return list;
    }
}

