// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

class Solution {
public:
    std::string largestTimeFromDigits(std::vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        std::string best;
        do {
            int hours = 10 * arr[0] + arr[1];
            int minutes = 10 * arr[2] + arr[3];
            if (hours < 24 && minutes < 60) {
                char buf[6];
                std::snprintf(buf, sizeof(buf), "%02d:%02d", hours, minutes);
                std::string cand(buf);
                if (cand > best) best = cand;
            }
        } while (std::next_permutation(arr.begin(), arr.end()));
        return best;
    }
};
