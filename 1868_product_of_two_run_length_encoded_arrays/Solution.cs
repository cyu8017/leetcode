// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

public class Solution {
    public int[][] FindRLEArray(int[][] encoded1, int[][] encoded2) {
        var result = new List<int[]>();
        int i = 0;
        int j = 0;
        int rem1 = encoded1[0][1];
        int rem2 = encoded2[0][1];

        while (i < encoded1.Length) {
            int take = Math.Min(rem1, rem2);
            int value = encoded1[i][0] * encoded2[j][0];
            if (result.Count > 0 && result[^1][0] == value) {
                result[^1][1] += take;
            } else {
                result.Add(new[] { value, take });
            }
            rem1 -= take;
            rem2 -= take;
            if (rem1 == 0) {
                i++;
                if (i < encoded1.Length) {
                    rem1 = encoded1[i][1];
                }
            }
            if (rem2 == 0) {
                j++;
                if (j < encoded2.Length) {
                    rem2 = encoded2[j][1];
                }
            }
        }
        return result.ToArray();
    }
}
