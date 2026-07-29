// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

#include <unordered_set>
#include <vector>

class Solution {
public:
    bool canVisitAllRooms(std::vector<std::vector<int>>& rooms) {
        std::unordered_set<int> seen{0};
        std::vector<int> stack{0};
        while (!stack.empty()) {
            int room = stack.back();
            stack.pop_back();
            for (int key : rooms[room]) {
                if (!seen.count(key)) {
                    seen.insert(key);
                    stack.push_back(key);
                }
            }
        }
        return static_cast<int>(seen.size()) == static_cast<int>(rooms.size());
    }
};
