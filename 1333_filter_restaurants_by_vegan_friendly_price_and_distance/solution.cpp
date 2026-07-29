#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> filterRestaurants(std::vector<std::vector<int>>& restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        std::vector<std::vector<int>> filtered;
        for (auto& r : restaurants) {
            if ((!veganFriendly || r[2]) && r[3] <= maxPrice && r[4] <= maxDistance)
                filtered.push_back(r);
        }
        std::sort(filtered.begin(), filtered.end(), [](auto& a, auto& b) {
            if (a[1] != b[1]) return a[1] > b[1];
            return a[0] > b[0];
        });
        std::vector<int> answer;
        for (auto& r : filtered) answer.push_back(r[0]);
        return answer;
    }
};
