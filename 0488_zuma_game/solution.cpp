// LeetCode 0488 - Zuma Game

// https://leetcode.com/problems/zuma-game/



#include <algorithm>

#include <string>

#include <unordered_map>



class Solution {

    std::unordered_map<std::string, int> memo_;



    std::string shrink(std::string s) {

        int index = 0;

        while (index < static_cast<int>(s.size())) {

            int end = index;

            while (end < static_cast<int>(s.size()) && s[end] == s[index]) {

                ++end;

            }

            if (end - index >= 3) {

                return shrink(s.substr(0, index) + s.substr(end));

            }

            index = end;

        }

        return s;

    }



    int dfs(std::string board, std::string hand) {

        const std::string key = board + "#" + hand;

        const auto found = memo_.find(key);

        if (found != memo_.end()) {

            return found->second;

        }

        board = shrink(board);

        if (board.empty()) {

            return memo_[key] = 0;

        }

        int best = 1000000000;

        for (int insert = 0; insert <= static_cast<int>(board.size()); ++insert) {

            for (int pick = 0; pick < static_cast<int>(hand.size()); ++pick) {

                const char color = hand[pick];

                if (insert < static_cast<int>(board.size()) && board[insert] == color) {

                    // allowed

                } else if (insert > 0 && board[insert - 1] == color) {

                    // allowed

                } else {

                    continue;

                }

                const std::string nextBoard = shrink(board.substr(0, insert) + color + board.substr(insert));

                if (nextBoard == board) {

                    continue;

                }

                const std::string nextHand = hand.substr(0, pick) + hand.substr(pick + 1);

                const int steps = dfs(nextBoard, nextHand);

                if (steps != 1000000000) {

                    best = std::min(best, steps + 1);

                }

            }

        }

        return memo_[key] = best;

    }



public:

    int findMinStep(std::string board, std::string hand) {
        const int result = dfs(board, hand);

        return result == 1000000000 ? -1 : result;

    }

};


