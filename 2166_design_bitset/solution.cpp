// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

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

class Bitset {
    vector<char> bits;
    int ones = 0;
    bool flipped = false;
    int size;
public:
    Bitset(int size) : bits(size, 0), size(size) {}
    void fix(int idx) {
        char target = flipped ? 0 : 1;
        if (bits[idx] != target) {
            bits[idx] = target;
            ones += flipped ? -1 : 1;
        }
    }
    void unfix(int idx) {
        char target = flipped ? 1 : 0;
        if (bits[idx] != target) {
            bits[idx] = target;
            ones += flipped ? 1 : -1;
        }
    }
    void flip() {
        flipped = !flipped;
        ones = size - ones;
    }
    bool all() { return ones == size; }
    bool one() { return ones > 0; }
    int count() { return ones; }
    string toString() {
        string b(size, '0');
        for (int i = 0; i < size; i++) {
            char v = bits[i];
            if (flipped) v ^= 1;
            b[i] = '0' + v;
        }
        return b;
    }
};
