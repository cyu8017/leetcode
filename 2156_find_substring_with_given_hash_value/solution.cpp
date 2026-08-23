// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

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
    string subStrHash(string s, int power, int modulo, int k, int hashValue) {
        int n = s.size();
        long long pk = 1;
        for (int i = 0; i < k - 1; i++) pk = pk * power % modulo;
        long long h = 0;
        int ans = 0;
        for (int i = n - 1; i >= n - k; i--)
            h = (h * power + (s[i] - 'a' + 1)) % modulo;
        if (h == hashValue) ans = n - k;
        for (int i = n - k - 1; i >= 0; i--) {
            h = (h - (s[i + k] - 'a' + 1) * pk % modulo + modulo) % modulo;
            h = (h * power + (s[i] - 'a' + 1)) % modulo;
            if (h == hashValue) ans = i;
        }
        return s.substr(ans, k);
    }
};
