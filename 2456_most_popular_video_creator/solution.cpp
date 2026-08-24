// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> mostPopularCreator(std::vector<std::string>& creators, std::vector<std::string>& ids, std::vector<int>& views) {
        struct Info {
            long long total = 0;
            std::string bestID;
            int bestViews = 0;
        };
        std::unordered_map<std::string, Info> mp;
        long long maxTotal = 0;
        for (int i = 0; i < (int)creators.size(); i++) {
            auto& inf = mp[creators[i]];
            if (inf.bestID.empty() && inf.total == 0 && inf.bestViews == 0) {
                // first insert may still have empty bestID if views handled below
            }
            if (inf.total == 0 && inf.bestID.empty()) {
                inf.bestID = ids[i];
                inf.bestViews = views[i];
            }
            inf.total += views[i];
            if (views[i] > inf.bestViews || (views[i] == inf.bestViews && ids[i] < inf.bestID)) {
                inf.bestViews = views[i];
                inf.bestID = ids[i];
            }
            if (inf.total > maxTotal) maxTotal = inf.total;
        }
        // fix first-insert: when map default-constructs, bestID empty - handled by setting on first use
        // Re-run first assignment properly:
        mp.clear();
        maxTotal = 0;
        for (int i = 0; i < (int)creators.size(); i++) {
            auto it = mp.find(creators[i]);
            if (it == mp.end()) {
                mp[creators[i]] = Info{views[i], ids[i], views[i]};
            } else {
                it->second.total += views[i];
                if (views[i] > it->second.bestViews || (views[i] == it->second.bestViews && ids[i] < it->second.bestID)) {
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
