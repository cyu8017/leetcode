// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

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
    int wateringPlants(vector<int>& plants, int capacity) {
        int ans = 0, cur = capacity;
        for (int i = 0; i < (int)plants.size(); i++) {
            if (cur < plants[i]) { ans += i * 2; cur = capacity; }
            cur -= plants[i];
            ans++;
        }
        return ans;
    }
};
