// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

#include <vector>

class Solution {
public:
    int magicalString(int n) {
        if (n == 0) {
            return 0;
        }
        std::vector<int> seq = {1, 2, 2};
        int index = 2;
        while (static_cast<int>(seq.size()) < n) {
            if (seq[index] == 1) {
                seq.push_back(seq.back() == 2 ? 1 : 2);
            } else {
                const int value = seq.back() == 2 ? 1 : 2;
                seq.push_back(value);
                seq.push_back(value);
            }
            ++index;
        }
        int ones = 0;
        for (int i = 0; i < n; ++i) {
            if (seq[i] == 1) {
                ++ones;
            }
        }
        return ones;
    }
};
