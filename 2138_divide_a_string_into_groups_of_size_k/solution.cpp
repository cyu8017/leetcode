// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

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
    vector<string> divideString(string s, int k, char fill) {
        vector<string> ans;
        for (int i = 0; i < (int)s.size(); i += k) {
            if (i + k <= (int)s.size()) ans.push_back(s.substr(i, k));
            else {
                string chunk = s.substr(i);
                while ((int)chunk.size() < k) chunk.push_back(fill);
                ans.push_back(chunk);
            }
        }
        return ans;
    }
};
