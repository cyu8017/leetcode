// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int garbageCollection(std::vector<std::string>& garbage, std::vector<int>& travel) {
        int ans = 0;
        std::unordered_map<char, int> last;
        for (int i = 0; i < (int)garbage.size(); i++) {
            ans += (int)garbage[i].size();
            for (char c : garbage[i]) last[c] = i;
        }
        std::vector<int> pref(travel.size() + 1);
        for (int i = 0; i < (int)travel.size(); i++) pref[i + 1] = pref[i] + travel[i];
        for (char typ : {'M', 'P', 'G'}) {
            ans += pref[last[typ]];
        }
        return ans;
    }
};
