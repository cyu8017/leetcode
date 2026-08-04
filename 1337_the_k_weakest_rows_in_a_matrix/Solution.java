// LeetCode 1337 - The K Weakest Rows In A Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

import java.util.*;

class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        Integer[] idx = new Integer[mat.length];
        for (int i = 0; i < mat.length; i++) idx[i] = i;
        Arrays.sort(idx, (i, j) -> {
            int si = 0, sj = 0;
            for (int v : mat[i]) si += v;
            for (int v : mat[j]) sj += v;
            return si != sj ? Integer.compare(si, sj) : Integer.compare(i, j);
        });
        int[] answer = new int[k];
        for (int i = 0; i < k; i++) answer[i] = idx[i];
        return answer;
    }
}
