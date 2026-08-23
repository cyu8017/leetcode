// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

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
    int minSteps(int left, int right, int start) {
        if (right <= start) return start - left;
        if (left >= start) return right - start;
        return min((start - left) + (right - left), (right - start) + (right - left));
    }
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int n = (int)fruits.size();
        vector<int> pref(n + 1), pos(n);
        for (int i = 0; i < n; i++) {
            pos[i] = fruits[i][0];
            pref[i + 1] = pref[i] + fruits[i][1];
        }
        int ans = 0, j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && minSteps(pos[i], pos[j], startPos) > k) j++;
            if (j <= i) ans = max(ans, pref[i + 1] - pref[j]);
        }
        j = 0;
        for (int i = 0; i < n; i++) {
            while (j <= i && minSteps(pos[j], pos[i], startPos) > k) j++;
            ans = max(ans, pref[i + 1] - pref[j]);
        }
        return ans;
    }
};
