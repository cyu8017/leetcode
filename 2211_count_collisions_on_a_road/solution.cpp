// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

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
    int countCollisions(string directions) {
        int i = 0, j = (int)directions.size() - 1;
        while (i < (int)directions.size() && directions[i] == 'L') i++;
        while (j >= 0 && directions[j] == 'R') j--;
        int ans = 0;
        for (int k = i; k <= j; k++) if (directions[k] != 'S') ans++;
        return ans;
    }
};
