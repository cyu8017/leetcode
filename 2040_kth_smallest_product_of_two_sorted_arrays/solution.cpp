// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        auto countLE = [&](long long x) {
            long long cnt = 0;
            for (int a : nums1) {
                if (a > 0) {
                    int lo = 0, hi = (int)nums2.size();
                    while (lo < hi) {
                        int mid = (lo + hi) / 2;
                        if ((long long)a * nums2[mid] <= x) lo = mid + 1;
                        else hi = mid;
                    }
                    cnt += lo;
                } else if (a < 0) {
                    int lo = 0, hi = (int)nums2.size();
                    while (lo < hi) {
                        int mid = (lo + hi) / 2;
                        if ((long long)a * nums2[mid] <= x) hi = mid;
                        else lo = mid + 1;
                    }
                    cnt += (int)nums2.size() - lo;
                } else if (x >= 0) cnt += (int)nums2.size();
            }
            return cnt;
        };
        long long lo = -1e10, hi = 1e10;
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (countLE(mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
