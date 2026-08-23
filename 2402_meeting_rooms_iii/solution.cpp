// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    int mostBooked(int n, std::vector<std::vector<int>>& meetings) {
        std::sort(meetings.begin(), meetings.end(), [](const auto& a, const auto& b) {
            return a[0] < b[0];
        });
        std::priority_queue<long long, std::vector<long long>, std::greater<long long>> free;
        for (int i = 0; i < n; i++) free.push(i);
        using P = std::pair<long long, long long>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> busy;
        std::vector<int> cnt(n);
        for (auto& m : meetings) {
            long long start = m[0], end = m[1];
            while (!busy.empty() && busy.top().first <= start) {
                free.push(busy.top().second);
                busy.pop();
            }
            long long dur = end - start;
            long long room, begin;
            if (!free.empty()) {
                room = free.top();
                free.pop();
                begin = start;
            } else {
                auto top = busy.top();
                busy.pop();
                begin = top.first;
                room = top.second;
            }
            busy.push({begin + dur, room});
            cnt[room]++;
        }
        int ans = 0;
        for (int i = 1; i < n; i++) {
            if (cnt[i] > cnt[ans]) ans = i;
        }
        return ans;
    }
};
