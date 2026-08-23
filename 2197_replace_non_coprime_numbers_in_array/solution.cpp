// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

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
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        auto gcd = [](int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; };
        vector<int> stack;
        for (int x : nums) {
            while (!stack.empty()) {
                int g = gcd(stack.back(), x);
                if (g == 1) break;
                x = stack.back() / g * x;
                stack.pop_back();
            }
            stack.push_back(x);
        }
        return stack;
    }
};
