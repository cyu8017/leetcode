// LeetCode 1064 - Fixed Point
// https://leetcode.com/problems/fixed-point/

int fixedPoint(int* arr, int arrSize) {
    int lo = 0, hi = arrSize - 1, ans = -1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (arr[mid] == mid) {
            ans = mid;
            hi = mid - 1;
        } else if (arr[mid] < mid) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return ans;
}
