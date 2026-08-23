// LeetCode 0401 - Binary Watch
// https://leetcode.com/problems/binary-watch/

#include <cstdio>
#include <string>
#include <vector>

class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> result;

        for (int hour = 0; hour < 12; ++hour) {
            for (int minute = 0; minute < 60; ++minute) {
                if (popcount(hour) + popcount(minute) == turnedOn) {
                    char buffer[6];
                    snprintf(buffer, sizeof(buffer), "%d:%02d", hour, minute);
                    result.emplace_back(buffer);
                }
            }
        }

        return result;
    }

private:
    static int popcount(int value) {
        int count = 0;
        while (value) {
            count += value & 1;
            value >>= 1;
        }
        return count;
    }
};
