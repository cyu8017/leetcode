// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Leaderboard {
public:
    Leaderboard() = default;

    void addScore(int playerId, int score) {
        scores[playerId] += score;
    }

    int top(int K) {
        std::vector<int> values;
        values.reserve(scores.size());
        for (const auto& [_, score] : scores) {
            values.push_back(score);
        }
        std::sort(values.begin(), values.end(), std::greater<int>());
        int sum = 0;
        for (int i = 0; i < K && i < static_cast<int>(values.size()); ++i) {
            sum += values[i];
        }
        return sum;
    }

    void reset(int playerId) {
        scores.erase(playerId);
    }

private:
    std::unordered_map<int, int> scores;
};
