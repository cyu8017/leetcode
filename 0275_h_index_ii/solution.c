// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

int hIndex(int* citations, int citationsSize) {
    int left = 0;
    int right = citationsSize - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int papers = citationsSize - mid;
        if (citations[mid] >= papers) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return citationsSize - left;
}
