// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumWhiteTiles(std::vector<std::vector<int>>& tiles, int carpetLen) {
        std::sort(tiles.begin(), tiles.end());
        int n = (int)tiles.size();
        std::vector<int> pref(n + 1);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1);
        int ans = 0, j = 0;
        for (int i = 0; i < n; ++i) {
            int end = tiles[i][0] + carpetLen - 1;
            while (j < n && tiles[j][0] <= end) j++;
            int cover = pref[j] - pref[i];
            if (j > 0 && tiles[j - 1][1] > end) cover -= tiles[j - 1][1] - end;
            ans = std::max(ans, cover);
        }
        return ans;
    }
};
