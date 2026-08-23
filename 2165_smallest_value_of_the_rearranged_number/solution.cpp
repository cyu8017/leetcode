// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

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
    long long smallestNumber(long long num) {
        bool neg = num < 0;
        if (neg) num = -num;
        if (num == 0) return 0;
        string digits;
        while (num > 0) { digits.push_back('0' + num % 10); num /= 10; }
        if (neg) {
            sort(digits.begin(), digits.end(), greater<char>());
            long long ans = 0;
            for (char d : digits) ans = ans * 10 + (d - '0');
            return -ans;
        }
        sort(digits.begin(), digits.end());
        if (digits[0] == '0') {
            for (int i = 1; i < (int)digits.size(); i++) {
                if (digits[i] != '0') { swap(digits[0], digits[i]); break; }
            }
        }
        long long ans = 0;
        for (char d : digits) ans = ans * 10 + (d - '0');
        return ans;
    }
};
