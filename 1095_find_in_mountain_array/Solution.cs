// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

public class MountainArray {
    public virtual int Get(int index) {
        return 0;
    }

    public virtual int Length() {
        return 0;
    }
}

public class Solution {
    public int FindInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.Length();
        int lo = 0, hi = n - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mountainArr.Get(mid) < mountainArr.Get(mid + 1)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        int peak = lo;
        lo = 0;
        hi = peak;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int val = mountainArr.Get(mid);
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
            int mid = (lo + hi) / 2;
            int val = mountainArr.Get(mid);
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
}
