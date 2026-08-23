// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

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
    int minimumBuckets(string hamsters) {
        string b = hamsters;
        int ans = 0;
        for (int i = 0; i < (int)b.size(); i++) {
            if (b[i] != 'H') continue;
            if (i > 0 && b[i - 1] == 'B') continue;
            if (i + 1 < (int)b.size() && b[i + 1] == '.') { b[i + 1] = 'B'; ans++; }
            else if (i > 0 && b[i - 1] == '.') { b[i - 1] = 'B'; ans++; }
            else return -1;
        }
        return ans;
    }
};
