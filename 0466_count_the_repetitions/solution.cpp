// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

#include <string>
#include <unordered_map>
#include <utility>

class Solution {
public:
    int getMaxRepetitions(std::string s1, int n1, std::string s2, int n2) {
        if (s2.empty()) {
            return 0;
        }

        int index = 0;
        int s2Count = 0;
        std::unordered_map<int, std::pair<int, int>> record;

        for (int repeat = 0; repeat < n1; ++repeat) {
            for (char ch : s1) {
                if (ch == s2[index]) {
                    ++index;
                    if (index == static_cast<int>(s2.size())) {
                        index = 0;
                        ++s2Count;
                    }
                }
            }
            if (record.count(index)) {
                auto [previousRepeat, previousCount] = record[index];
                int cycle = repeat - previousRepeat;
                int countCycle = s2Count - previousCount;
                int remaining = n1 - repeat - 1;
                s2Count += (remaining / cycle) * countCycle;
                if (repeat + (remaining / cycle) * cycle >= n1 - 1) {
                    break;
                }
            }
            record[index] = {repeat, s2Count};
        }

        return s2Count / n2;
    }
};
