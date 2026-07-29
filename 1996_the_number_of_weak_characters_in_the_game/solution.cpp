// LeetCode 1996 - The Number of Weak Characters in the Game
#include <algorithm>
#include <vector>

class Solution {
public:
    int numberOfWeakCharacters(std::vector<std::vector<int>>& properties) {
        std::sort(properties.begin(), properties.end(), [](auto& a, auto& b) {
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] > b[1];
        });
        int ans = 0, maxDef = 0;
        for (int i = (int)properties.size() - 1; i >= 0; i--) {
            if (properties[i][1] < maxDef) ans++;
            else maxDef = properties[i][1];
        }
        return ans;
    }
};
