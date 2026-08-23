// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

class Solution {
    public int hIndex(int[] citations) {
        int left = 0;
        int right = citations.length - 1;
        int length = citations.length;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int papers = length - mid;
            if (citations[mid] >= papers) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return length - left;
    }
}
