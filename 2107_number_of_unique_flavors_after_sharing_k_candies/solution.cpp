// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

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
    int shareCandies(vector<int>& candies, int k) {
        int n = (int)candies.size();
        unordered_map<int, int> freq;
        for (int c : candies) freq[c]++;
        if (k == 0) return (int)freq.size();
        for (int i = 0; i < k; i++) {
            if (--freq[candies[i]] == 0) freq.erase(candies[i]);
        }
        int ans = (int)freq.size();
        for (int i = k; i < n; i++) {
            freq[candies[i - k]]++;
            if (--freq[candies[i]] == 0) freq.erase(candies[i]);
            ans = max(ans, (int)freq.size());
        }
        return ans;
    }
};
