// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

#include <string>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>

class VideoSharingPlatform {
    int nextID = 0;
    std::priority_queue<int, std::vector<int>, std::greater<int>> free;
    std::unordered_map<int, std::string> videos;
    std::unordered_map<int, int> views, likes, dislikes;
public:
    VideoSharingPlatform() {}

    int upload(std::string video) {
        int id;
        if (!free.empty()) { id = free.top(); free.pop(); }
        else id = nextID++;
        videos[id] = video;
        views[id] = likes[id] = dislikes[id] = 0;
        return id;
    }

    void remove(int videoId) {
        if (!videos.count(videoId)) return;
        videos.erase(videoId);
        views.erase(videoId);
        likes.erase(videoId);
        dislikes.erase(videoId);
        free.push(videoId);
    }

    std::string watch(int videoId, int startMinute, int endMinute) {
        auto it = videos.find(videoId);
        if (it == videos.end()) return "-1";
        views[videoId]++;
        const std::string& v = it->second;
        if (startMinute >= (int)v.size()) return "";
        endMinute = std::min(endMinute, (int)v.size() - 1);
        return v.substr(startMinute, endMinute - startMinute + 1);
    }

    void like(int videoId) {
        if (videos.count(videoId)) likes[videoId]++;
    }

    void dislike(int videoId) {
        if (videos.count(videoId)) dislikes[videoId]++;
    }

    std::vector<int> getLikesAndDislikes(int videoId) {
        if (!videos.count(videoId)) return {-1};
        return {likes[videoId], dislikes[videoId]};
    }

    int getViews(int videoId) {
        if (!videos.count(videoId)) return -1;
        return views[videoId];
    }
};
