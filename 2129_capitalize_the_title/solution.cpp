// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

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
    string capitalizeTitle(string title) {
        stringstream ss(title);
        string w, ans;
        while (ss >> w) {
            for (char& c : w) c = tolower(c);
            if (w.size() > 2) w[0] = toupper(w[0]);
            if (!ans.empty()) ans += ' ';
            ans += w;
        }
        return ans;
    }
};
