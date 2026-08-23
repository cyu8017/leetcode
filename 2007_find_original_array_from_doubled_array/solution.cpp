// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

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
    vector<int> findOriginalArray(vector<int>& changed) {
        if (changed.size() % 2) return {};
        sort(changed.begin(), changed.end());
        unordered_map<int, int> freq;
        for (int x : changed) freq[x]++;
        vector<int> ans;
        for (int x : changed) {
            if (!freq[x]) continue;
            freq[x]--;
            if (!freq[2 * x]) return {};
            freq[2 * x]--;
            ans.push_back(x);
        }
        return ans;
    }
};
