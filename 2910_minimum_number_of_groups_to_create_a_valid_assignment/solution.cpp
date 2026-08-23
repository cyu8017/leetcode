// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minGroupsForValidAssignment(std::vector<int>& balls) {
        std::unordered_map<int, int> freq;
        for (int b : balls) freq[b]++;
        std::vector<int> counts;
        int minF = 1 << 30;
        for (auto& [_, f] : freq) {
            counts.push_back(f);
            if (f < minF) minF = f;
        }
        for (int size = minF; size >= 1; size--) {
            bool ok = true;
            int groups = 0;
            for (int c : counts) {
                int rem = c % (size + 1);
                int g2 = c / (size + 1);
                if (rem == 0) groups += g2;
                else if (size - rem <= g2) groups += g2 + 1;
                else {
                    ok = false;
                    break;
                }
            }
            if (ok) return groups;
        }
        return (int)balls.size();
    }
};
