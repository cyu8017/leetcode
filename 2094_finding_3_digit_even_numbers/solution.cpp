// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

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
    vector<int> findEvenNumbers(vector<int>& digits) {
        int freq[10] = {};
        for (int d : digits) freq[d]++;
        vector<int> ans;
        for (int x = 100; x <= 998; x += 2) {
            int a = x / 100, b = (x / 10) % 10, c = x % 10;
            freq[a]--; freq[b]--; freq[c]--;
            if (freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0) ans.push_back(x);
            freq[a]++; freq[b]++; freq[c]++;
        }
        return ans;
    }
};
