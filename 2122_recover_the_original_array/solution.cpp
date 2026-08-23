// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

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
    vector<int> recoverArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            int diff = nums[i] - nums[0];
            if (diff == 0 || diff % 2) continue;
            int k = diff / 2;
            vector<char> used(n);
            used[0] = used[i] = 1;
            vector<int> ans{(nums[0] + nums[i]) / 2};
            int l = 0, r = i;
            bool ok = true;
            while ((int)ans.size() < n / 2) {
                while (l < n && used[l]) l++;
                if (l == n) { ok = false; break; }
                int need = nums[l] + 2 * k;
                while (r < n && (used[r] || nums[r] < need)) r++;
                if (r == n || nums[r] != need) { ok = false; break; }
                used[l] = used[r] = 1;
                ans.push_back(nums[l] + k);
            }
            if (ok) return ans;
        }
        return {};
    }
};
