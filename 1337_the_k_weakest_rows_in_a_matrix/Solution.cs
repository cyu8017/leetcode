// LeetCode 1337 - The K Weakest Rows In A Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

using System.Linq;
public class Solution {
    public int[] KWeakestRows(int[][] mat, int k) {
        return Enumerable.Range(0, mat.Length).OrderBy(i => mat[i].Sum()).ThenBy(i => i).Take(k).ToArray();
    }
}
