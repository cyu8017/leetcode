// LeetCode 2105 - Watering Plants II
// https://leetcode.com/problems/watering-plants-ii/

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
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        int i = 0, j = (int)plants.size() - 1;
        int a = capacityA, b = capacityB, ans = 0;
        while (i < j) {
            if (a < plants[i]) { ans++; a = capacityA; }
            a -= plants[i++];
            if (b < plants[j]) { ans++; b = capacityB; }
            b -= plants[j--];
        }
        if (i == j) {
            if (a >= b) { if (a < plants[i]) ans++; }
            else if (b < plants[i]) ans++;
        }
        return ans;
    }
};
