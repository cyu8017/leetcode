// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

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
    int countEven(int num) {
        int ans = 0;
        for (int x = 1; x <= num; x++) {
            int s = 0, y = x;
            while (y) { s += y % 10; y /= 10; }
            if (s % 2 == 0) ans++;
        }
        return ans;
    }
};
