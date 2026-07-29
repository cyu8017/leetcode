// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

#include <map>
#include <vector>

class Solution {
public:
    bool isNStraightHand(std::vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize) {
            return false;
        }
        std::map<int, int> count;
        for (int x : hand) {
            ++count[x];
        }
        for (auto it = count.begin(); it != count.end(); ++it) {
            int start = it->first;
            while (count[start] > 0) {
                for (int x = start; x < start + groupSize; ++x) {
                    if (count[x] == 0) {
                        return false;
                    }
                    --count[x];
                }
            }
        }
        return true;
    }
};
