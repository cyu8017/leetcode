// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

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

class Robot {
    int w, h, peri, pos = 0;
    bool moved = false;
    tuple<int,int,string> getPosDir() {
        int p = pos;
        if (p == 0) {
            if (!moved) return {0, 0, "East"};
            return {0, 0, "South"};
        }
        if (p <= w - 1) return {p, 0, "East"};
        p -= w - 1;
        if (p <= h - 1) return {w - 1, p, "North"};
        p -= h - 1;
        if (p <= w - 1) return {w - 1 - p, h - 1, "West"};
        p -= w - 1;
        return {0, h - 1 - p, "South"};
    }
public:
    Robot(int width, int height) : w(width), h(height), peri(2 * (width + height) - 4) {}
    void step(int num) {
        moved = true;
        pos = (pos + num) % peri;
    }
    vector<int> getPos() {
        auto [x, y, d] = getPosDir();
        return {x, y};
    }
    string getDir() {
        auto [x, y, d] = getPosDir();
        return d;
    }
};
