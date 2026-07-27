// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

#include <vector>

class MountainArray {
public:
    MountainArray(const std::vector<int>& arr) : arr_(arr) {}

    int get(int index) const { return arr_[index]; }

    int length() const { return static_cast<int>(arr_.size()); }

private:
    std::vector<int> arr_;
};

class Solution {
public:
    int findInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.length();
        int lo = 0;
        int hi = n - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
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
            int val = mountainArr.get(mid);
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
            int val = mountainArr.get(mid);
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
};
