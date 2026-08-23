// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

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
    bool isPalBase(long long x, int base) {
        vector<int> digits;
        while (x > 0) { digits.push_back(x % base); x /= base; }
        for (int l = 0, r = (int)digits.size() - 1; l < r; l++, r--)
            if (digits[l] != digits[r]) return false;
        return true;
    }
public:
    long long kMirror(int k, int n) {
        long long ans = 0;
        int count = 0;
        for (int length = 1; count < n; length++) {
            int start = 1;
            for (int i = 1; i < (length + 1) / 2; i++) start *= 10;
            int end = start * 10;
            for (int half = start; half < end && count < n; half++) {
                long long pal = half;
                if (length % 2 == 0) {
                    int x = half;
                    while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
                } else {
                    int x = half / 10;
                    while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
                }
                if (isPalBase(pal, k)) { ans += pal; count++; }
            }
        }
        return ans;
    }
};
