// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

class Solution {
    public int hIndex(int[] citations) {
        int[] buckets = new int[citations.length + 1];
        for (int citation : citations) {
            buckets[Math.min(citation, citations.length)]++;
        }
        int total = 0;
        for (int h = buckets.length - 1; h >= 0; h--) {
            total += buckets[h];
            if (total >= h) {
                return h;
            }
        }
        return 0;
    }
}
