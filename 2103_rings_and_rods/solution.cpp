// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

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
    int countPoints(string rings) {
        int mask[10] = {};
        for (int i = 0; i < (int)rings.size(); i += 2) {
            char c = rings[i];
            int r = rings[i + 1] - '0';
            int bit = c == 'R' ? 1 : c == 'G' ? 2 : 4;
            mask[r] |= bit;
        }
        int ans = 0;
        for (int m : mask) if (m == 7) ans++;
        return ans;
    }
};
