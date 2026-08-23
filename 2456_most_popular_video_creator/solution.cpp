// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> mostPopularCreator(std::vector<std::string>& creators,
                                                             std::vector<std::string>& ids,
                                                             std::vector<int>& views) {
        struct Info {
            long long total = 0;
            std::string bestID;
            int bestViews = 0;
        };
        std::unordered_map<std::string, Info> mp;
        long long maxTotal = 0;
        for (int i = 0; i < (int)creators.size(); i++) {
            auto it = mp.find(creators[i]);
            if (it == mp.end()) {
                mp.emplace(creators[i], Info{views[i], ids[i], views[i]});
            } else {
                it->second.total += views[i];
                if (views[i] > it->second.bestViews ||
                    (views[i] == it->second.bestViews && ids[i] < it->second.bestID)) {
                    it->second.bestViews = views[i];
                    it->second.bestID = ids[i];
                }
            }
            if (mp[creators[i]].total > maxTotal) maxTotal = mp[creators[i]].total;
        }
        std::vector<std::vector<std::string>> ans;
        for (auto& [c, inf] : mp) {
            if (inf.total == maxTotal) ans.push_back({c, inf.bestID});
        }
        return ans;
    }
};
