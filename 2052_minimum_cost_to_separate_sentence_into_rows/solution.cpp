// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

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
    int minimumCost(string sentence, int k) {
        vector<string> words;
        stringstream ss(sentence);
        string w;
        while (ss >> w) words.push_back(w);
        int n = (int)words.size();
        const long long INF = 1e18;
        vector<long long> dp(n + 1, INF);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            int length = -1;
            for (int j = i; j < n; j++) {
                length += 1 + (int)words[j].size();
                if (length > k) break;
                long long cost = 0;
                if (j < n - 1) {
                    long long extra = k - length;
                    cost = extra * extra;
                }
                dp[i] = min(dp[i], cost + dp[j + 1]);
            }
        }
        return (int)dp[0];
    }
};
