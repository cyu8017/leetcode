// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

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
    long long singleDivisorTriplet(vector<int>& nums) {
        long long freq[101] = {};
        for (int x : nums) freq[x]++;
        long long ans = 0;
        for (int a = 1; a <= 100; a++) {
            if (!freq[a]) continue;
            for (int b = a; b <= 100; b++) {
                if (!freq[b]) continue;
                for (int c = b; c <= 100; c++) {
                    if (!freq[c]) continue;
                    int s = a + b + c, cnt = 0;
                    if (s % a == 0) cnt++;
                    if (s % b == 0) cnt++;
                    if (s % c == 0) cnt++;
                    if (cnt != 1) continue;
                    if (a == b && b == c) ans += freq[a] * (freq[a] - 1) * (freq[a] - 2);
                    else if (a == b) ans += freq[a] * (freq[a] - 1) * freq[c] * 3;
                    else if (b == c) ans += freq[b] * (freq[b] - 1) * freq[a] * 3;
                    else if (a == c) ans += freq[a] * (freq[a] - 1) * freq[b] * 3;
                    else ans += freq[a] * freq[b] * freq[c] * 6;
                }
            }
        }
        return ans;
    }
};
