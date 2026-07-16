// LeetCode 0353 - Design Snake Game
// https://leetcode.com/problems/design-snake-game/

#include <deque>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

class SnakeGame {
    int width_;
    int height_;
    std::vector<std::vector<int>> food_;
    int foodIndex_ = 0;
    int score_ = 0;
    std::deque<std::pair<int, int>> snake_;
    std::unordered_set<std::string> body_;

    static std::string key(int row, int col) {
        return std::to_string(row) + "," + std::to_string(col);
    }

public:
    SnakeGame(int width, int height, std::vector<std::vector<int>>& food)
        : width_(width), height_(height), food_(food) {
        snake_.push_back({0, 0});
        body_.insert(key(0, 0));
    }

    int move(std::string direction) {
        int row = snake_.front().first;
        int col = snake_.front().second;

        if (direction == "U") {
            row -= 1;
        } else if (direction == "D") {
            row += 1;
        } else if (direction == "L") {
            col -= 1;
        } else {
            col += 1;
        }

        if (row < 0 || row >= height_ || col < 0 || col >= width_) {
            return -1;
        }

        bool willEat = foodIndex_ < static_cast<int>(food_.size())
            && row == food_[foodIndex_][0]
            && col == food_[foodIndex_][1];

        if (!willEat) {
            auto tail = snake_.back();
            snake_.pop_back();
            body_.erase(key(tail.first, tail.second));
        }

        std::string headKey = key(row, col);
        if (body_.count(headKey)) {
            return -1;
        }

        snake_.push_front({row, col});
        body_.insert(headKey);

        if (willEat) {
            score_ += 1;
            foodIndex_ += 1;
        }

        return score_;
    }
};
