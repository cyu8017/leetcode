// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

/**
 * *********************************************************************
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * *********************************************************************
 *
 * int get(MountainArray *, int index);
 * int length(MountainArray *);
 */

typedef struct MountainArray MountainArray;
int get(MountainArray*, int index);
int length(MountainArray*);

int findInMountainArray(int target, MountainArray* mountainArr) {
    int n = length(mountainArr);
    int lo = 0, hi = n - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (get(mountainArr, mid) < get(mountainArr, mid + 1)) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    int peak = lo;
    lo = 0;
    hi = peak;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int val = get(mountainArr, mid);
        if (val == target) {
            return mid;
        }
        if (val < target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    lo = peak + 1;
    hi = n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int val = get(mountainArr, mid);
        if (val == target) {
            return mid;
        }
        if (val > target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return -1;
}
