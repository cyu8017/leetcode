// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

#include <algorithm>
#include <climits>
#include <map>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        first_ = firstPlayer;
        second_ = secondPlayer;
        std::vector<int> players(n);
        for (int i = 0; i < n; i++) {
            players[i] = i + 1;
        }
        auto [early, late] = dfs(players);
        return {early, late};
    }

private:
    int first_ = 0;
    int second_ = 0;
    std::map<std::vector<int>, std::pair<int, int>> memo_;

    std::pair<int, int> dfs(std::vector<int> players) {
        auto it = memo_.find(players);
        if (it != memo_.end()) {
            return it->second;
        }

        int count = static_cast<int>(players.size());
        int firstIndex = static_cast<int>(std::find(players.begin(), players.end(), first_) - players.begin());
        int secondIndex = static_cast<int>(std::find(players.begin(), players.end(), second_) - players.begin());
        if (firstIndex + secondIndex == count - 1) {
            return memo_[players] = {1, 1};
        }

        std::vector<std::vector<int>> choices;
        for (int index = 0; index < count / 2; index++) {
            int left = players[index];
            int right = players[count - 1 - index];
            if (left == first_ || left == second_) {
                choices.push_back({left});
            } else if (right == first_ || right == second_) {
                choices.push_back({right});
            } else {
                choices.push_back({left, right});
            }
        }
        if (count % 2) {
            choices.push_back({players[count / 2]});
        }

        int earliest = INT_MAX;
        int latest = 0;
        std::vector<int> picks;
        enumerate(choices, 0, picks, earliest, latest);

        return memo_[players] = {earliest, latest};
    }

    void enumerate(const std::vector<std::vector<int>>& choices, int idx, std::vector<int>& picks,
                   int& earliest, int& latest) {
        if (idx == static_cast<int>(choices.size())) {
            std::vector<int> winners = picks;
            std::sort(winners.begin(), winners.end());
            auto [early, late] = dfs(winners);
            earliest = std::min(earliest, early + 1);
            latest = std::max(latest, late + 1);
            return;
        }
        for (int player : choices[idx]) {
            picks.push_back(player);
            enumerate(choices, idx + 1, picks, earliest, latest);
            picks.pop_back();
        }
    }
};
