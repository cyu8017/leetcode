// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

#include <queue>
#include <vector>

class Solution {
    struct Worker {
        int idx, efficiency, leftToRight, pickOld, rightToLeft, putNew;
    };
    struct WaitCmp {
        bool operator()(const Worker& a, const Worker& b) const {
            if (a.efficiency != b.efficiency) return a.efficiency < b.efficiency;
            return a.idx < b.idx;
        }
    };
    struct Event {
        int time;
        Worker w;
        int side;
        bool operator>(const Event& o) const { return time > o.time; }
    };
public:
    int findCrossingTime(int n, int k, std::vector<std::vector<int>>& time) {
        std::priority_queue<Worker, std::vector<Worker>, WaitCmp> left, right;
        for (int i = 0; i < k; i++) {
            left.push({i, time[i][0] + time[i][2], time[i][0], time[i][1], time[i][2], time[i][3]});
        }
        std::priority_queue<Event, std::vector<Event>, std::greater<Event>> events;
        int cur = 0, remain = n, done = 0, bridgeFree = 0;
        while (done < n) {
            while (!events.empty() && events.top().time <= cur) {
                Event e = events.top();
                events.pop();
                if (e.side == 0) left.push(e.w);
                else right.push(e.w);
            }
            if (cur < bridgeFree) {
                cur = bridgeFree;
                continue;
            }
            if (!right.empty()) {
                Worker w = right.top();
                right.pop();
                cur += w.rightToLeft;
                bridgeFree = cur;
                events.push({cur + w.putNew, w, 0});
                done++;
                continue;
            }
            if (!left.empty() && remain > 0) {
                Worker w = left.top();
                left.pop();
                cur += w.leftToRight;
                bridgeFree = cur;
                remain--;
                events.push({cur + w.pickOld, w, 1});
                continue;
            }
            if (events.empty()) break;
            cur = events.top().time;
        }
        return cur;
    }
};
