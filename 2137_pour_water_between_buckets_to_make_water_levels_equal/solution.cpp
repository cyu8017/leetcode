// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

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
    double equalizeWater(vector<int>& buckets, int loss) {
        double lo = 0, hi = 0;
        for (int b : buckets) hi = max(hi, (double)b);
        auto can = [&](double x) {
            double have = 0, need = 0;
            for (int b : buckets) {
                if (b >= x) have += b - x;
                else need += x - b;
            }
            return have * (1.0 - loss / 100.0) >= need;
        };
        for (int iter = 0; iter < 60; iter++) {
            double mid = (lo + hi) / 2;
            if (can(mid)) lo = mid;
            else hi = mid;
        }
        return lo;
    }
};
