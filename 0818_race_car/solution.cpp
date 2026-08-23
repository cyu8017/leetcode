// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

#include <cstdlib>
#include <queue>
#include <unordered_set>
#include <utility>

class Solution {
public:
    int racecar(int target) {
        std::queue<std::tuple<int, int, int>> queue;
        queue.push({0, 1, 0});
        std::unordered_set<long long> seen;
        auto key = [](int pos, int speed) {
            return (static_cast<long long>(pos) << 20) ^
                   (static_cast<unsigned>(speed) & 0xfffff);
        };
        seen.insert(key(0, 1));
        while (!queue.empty()) {
            auto [pos, speed, steps] = queue.front();
            queue.pop();
            if (pos == target) {
                return steps;
            }
            int nxtPos = pos + speed, nxtSpeed = speed * 2;
            if (!seen.count(key(nxtPos, nxtSpeed)) &&
                std::abs(nxtPos) < target * 2) {
                seen.insert(key(nxtPos, nxtSpeed));
                queue.push({nxtPos, nxtSpeed, steps + 1});
            }
            int revSpeed = speed > 0 ? -1 : 1;
            if (!seen.count(key(pos, revSpeed))) {
                seen.insert(key(pos, revSpeed));
                queue.push({pos, revSpeed, steps + 1});
            }
        }
        return -1;
    }
};
