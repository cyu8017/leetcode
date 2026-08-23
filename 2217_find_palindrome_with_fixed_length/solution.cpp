// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

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
    vector<long long> kthPalindrome(vector<int>& queries, int intLength) {
        int half = (intLength + 1) / 2;
        int start = 1;
        for (int i = 1; i < half; i++) start *= 10;
        int total = start * 9;
        vector<long long> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int q = queries[i];
            if (q > total) { ans[i] = -1; continue; }
            int left = start + q - 1;
            long long pal = left;
            int x = left;
            if (intLength % 2) x /= 10;
            while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
            ans[i] = pal;
        }
        return ans;
    }
};
