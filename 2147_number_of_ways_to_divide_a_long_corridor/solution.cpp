// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

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
    int numberOfWays(string corridor) {
        const int MOD = 1000000007;
        vector<int> seats;
        for (int i = 0; i < (int)corridor.size(); i++)
            if (corridor[i] == 'S') seats.push_back(i);
        if (seats.empty() || seats.size() % 2) return 0;
        long long ans = 1;
        for (int i = 2; i < (int)seats.size(); i += 2)
            ans = ans * (seats[i] - seats[i - 1]) % MOD;
        return (int)ans;
    }
};
