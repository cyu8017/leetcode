#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class TweetCounts {
    std::unordered_map<std::string, std::vector<int>> times;
public:
    TweetCounts() {}

    void recordTweet(std::string tweetName, int time) {
        auto& v = times[tweetName];
        v.insert(std::upper_bound(v.begin(), v.end(), time), time);
    }

    std::vector<int> getTweetCountsPerFrequency(std::string freq, std::string tweetName, int startTime, int endTime) {
        int size = freq == "minute" ? 60 : freq == "hour" ? 3600 : 86400;
        auto& t = times[tweetName];
        std::vector<int> answer;
        for (int start = startTime; start <= endTime; start += size) {
            int end = std::min(endTime, start + size - 1);
            answer.push_back((int)(std::upper_bound(t.begin(), t.end(), end) - std::lower_bound(t.begin(), t.end(), start)));
        }
        return answer;
    }
};
