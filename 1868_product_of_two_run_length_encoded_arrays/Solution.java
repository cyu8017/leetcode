// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] findRLEArray(int[][] encoded1, int[][] encoded2) {
        List<int[]> result = new ArrayList<>();
        int i = 0;
        int j = 0;
        int rem1 = encoded1[0][1];
        int rem2 = encoded2[0][1];

        while (i < encoded1.length) {
            int take = Math.min(rem1, rem2);
            int value = encoded1[i][0] * encoded2[j][0];
            if (!result.isEmpty() && result.get(result.size() - 1)[0] == value) {
                result.get(result.size() - 1)[1] += take;
            } else {
                result.add(new int[] { value, take });
            }

            rem1 -= take;
            rem2 -= take;
            if (rem1 == 0) {
                i++;
                if (i < encoded1.length) {
                    rem1 = encoded1[i][1];
                }
            }
            if (rem2 == 0) {
                j++;
                if (j < encoded2.length) {
                    rem2 = encoded2[j][1];
                }
            }
        }

        int[][] answer = new int[result.size()][2];
        for (int idx = 0; idx < result.size(); idx++) {
            answer[idx] = result.get(idx);
        }
        return answer;
    }
}
