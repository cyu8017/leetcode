// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

#include <climits>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
    int dp(int ringIndex, int keyIndex, const std::string& ring, const std::string& key,
           const std::unordered_map<char, std::vector<int>>& positions,
           std::unordered_map<std::string, int>& memo) {
        if (keyIndex == static_cast<int>(key.size())) {
            return 0;
        }
        const std::string state = std::to_string(ringIndex) + "," + std::to_string(keyIndex);
        if (memo.count(state)) {
            return memo[state];
        }

        int best = INT_MAX;
        const int ringLength = static_cast<int>(ring.size());
        for (const int pos : positions.at(key[keyIndex])) {
            const int clockwise = (pos - ringIndex + ringLength) % ringLength;
            const int counter = (ringIndex - pos + ringLength) % ringLength;
            const int steps = std::min(clockwise, counter) + 1;
            best = std::min(best, steps + dp(pos, keyIndex + 1, ring, key, positions, memo));
        }
        memo[state] = best;
        return best;
    }

public:
    int findRotateSteps(std::string ring, std::string key) {
        std::unordered_map<char, std::vector<int>> positions;
        for (int index = 0; index < static_cast<int>(ring.size()); ++index) {
            positions[ring[index]].push_back(index);
        }
        std::unordered_map<std::string, int> memo;
        return dp(0, 0, ring, key, positions, memo);
    }
};
