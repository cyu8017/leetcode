// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

public class Solution {
    public int HIndex(int[] citations) {
        int[] buckets = new int[citations.Length + 1];
        foreach (int citation in citations) {
            buckets[System.Math.Min(citation, citations.Length)]++;
        }
        int total = 0;
        for (int h = buckets.Length - 1; h >= 0; h--) {
            total += buckets[h];
            if (total >= h) {
                return h;
            }
        }
        return 0;
    }
}
