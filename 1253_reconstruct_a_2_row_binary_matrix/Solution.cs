// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> ReconstructMatrix(int upper, int lower, int[] colsum) {
        var top = new int[colsum.Length];
        var bottom = new int[colsum.Length];
        for (int i = 0; i < colsum.Length; i++) {
            if (colsum[i] == 2) {
                top[i] = bottom[i] = 1;
                upper--;
                lower--;
            }
        }
        if (upper < 0 || lower < 0) return new List<IList<int>>();
        for (int i = 0; i < colsum.Length; i++) {
            if (colsum[i] == 1) {
                if (upper > 0) {
                    top[i] = 1;
                    upper--;
                } else if (lower > 0) {
                    bottom[i] = 1;
                    lower--;
                } else {
                    return new List<IList<int>>();
                }
            }
        }
        if (upper != 0 || lower != 0) return new List<IList<int>>();
        return new IList<int>[] { top, bottom };
    }
}
