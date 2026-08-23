// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

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
    int minMovesToMakePalindrome(string s) {
        string b = s;
        int ans = 0;
        while (b.size() > 1) {
            int j = (int)b.size() - 1;
            while (j > 0 && b[j] != b[0]) j--;
            if (j == 0) {
                ans += (int)b.size() / 2;
                b.erase(b.begin());
                continue;
            }
            ans += (int)b.size() - 1 - j;
            b.erase(b.begin() + j);
            b.erase(b.begin());
            b.pop_back();
        }
        return ans;
    }
};
