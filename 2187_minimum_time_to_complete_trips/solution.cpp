// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

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
    long long minimumTime(vector<int>& time, int totalTrips) {
        int mn = *min_element(time.begin(), time.end());
        long long lo = 1, hi = 1LL * mn * totalTrips;
        auto can = [&](long long mid) {
            long long trips = 0;
            for (int t : time) {
                trips += mid / t;
                if (trips >= totalTrips) return true;
            }
            return false;
        };
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
