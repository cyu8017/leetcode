// LeetCode 0355 - Design Twitter
// https://leetcode.com/problems/design-twitter/

#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

class Twitter {
    int time_ = 0;
    std::unordered_map<int, std::vector<std::pair<int, int>>> tweets_;
    std::unordered_map<int, std::unordered_set<int>> following_;

public:
    Twitter() {}

    void postTweet(int userId, int tweetId) {
        tweets_[userId].push_back({++time_, tweetId});
    }

    std::vector<int> getNewsFeed(int userId) {
        std::vector<std::pair<int, int>> heap;
        std::unordered_set<int> users = following_[userId];
        users.insert(userId);

        for (int uid : users) {
            const auto& timeline = tweets_[uid];
            int start = static_cast<int>(timeline.size()) - 10;
            if (start < 0) {
                start = 0;
            }
            for (int index = start; index < static_cast<int>(timeline.size()); ++index) {
                heap.push_back({-timeline[index].first, timeline[index].second});
            }
        }

        std::sort(heap.begin(), heap.end());
        std::vector<int> feed;
        for (size_t index = 0; index < heap.size() && feed.size() < 10; ++index) {
            feed.push_back(heap[index].second);
        }

        return feed;
    }

    void follow(int followerId, int followeeId) {
        following_[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        following_[followerId].erase(followeeId);
    }
};
