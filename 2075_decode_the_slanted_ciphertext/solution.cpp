// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

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
    string decodeCiphertext(string encodedText, int rows) {
        if (rows == 1) return encodedText;
        int cols = (int)encodedText.size() / rows;
        string b;
        for (int c = 0; c < cols; c++)
            for (int r = 0; r < rows && c + r < cols; r++)
                b.push_back(encodedText[r * cols + c + r]);
        while (!b.empty() && b.back() == ' ') b.pop_back();
        return b;
    }
};
