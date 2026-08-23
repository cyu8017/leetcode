// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

#include <cstdlib>
#include <string>
#include <unordered_map>
#include <utility>

class Solution {
    static std::unordered_map<char, std::pair<int, int>> buildPos() {
        std::unordered_map<char, std::pair<int, int>> pos;
        const char* keys[] = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; keys[i][j]; j++) pos[keys[i][j]] = {i, j};
        }
        return pos;
    }

public:
    int totalDistance(std::string s) {
        static auto pos = buildPos();
        char pre = 'a';
        int ans = 0;
        for (char cur : s) {
            auto p1 = pos[pre], p2 = pos[cur];
            ans += std::abs(p1.first - p2.first) + std::abs(p1.second - p2.second);
            pre = cur;
        }
        return ans;
    }
};
