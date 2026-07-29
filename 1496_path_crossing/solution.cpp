#include <set>
#include <string>
#include <utility>

class Solution {
public:
    bool isPathCrossing(std::string path) {
        int x = 0, y = 0;
        std::set<std::pair<int,int>> seen{{0, 0}};
        for (char c : path) {
            if (c == 'N') ++y;
            else if (c == 'S') --y;
            else if (c == 'E') ++x;
            else --x;
            if (seen.count({x, y})) return true;
            seen.insert({x, y});
        }
        return false;
    }
};
