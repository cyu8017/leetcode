// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <algorithm>

class Router {
    int lim;
    std::unordered_set<long long> vis;
    std::deque<std::array<int, 3>> q;
    std::unordered_map<int, int> idx;
    std::unordered_map<int, std::vector<int>> d;
    long long f(int a, int b, int c) {
        return ((long long)a << 46) | ((long long)b << 29) | (long long)c;
    }
public:
    Router(int memoryLimit) : lim(memoryLimit) {}

    bool addPacket(int source, int destination, int timestamp) {
        long long x = f(source, destination, timestamp);
        if (vis.count(x)) return false;
        vis.insert(x);
        if ((int)q.size() >= lim) forwardPacket();
        q.push_back({source, destination, timestamp});
        d[destination].push_back(timestamp);
        return true;
    }

    std::vector<int> forwardPacket() {
        if (q.empty()) return {};
        auto packet = q.front(); q.pop_front();
        int s = packet[0], dest = packet[1], t = packet[2];
        vis.erase(f(s, dest, t));
        idx[dest]++;
        return {s, dest, t};
    }

    int getCount(int destination, int startTime, int endTime) {
        auto& ls = d[destination];
        int k = idx[destination];
        auto it1 = std::lower_bound(ls.begin() + k, ls.end(), startTime);
        auto it2 = std::lower_bound(ls.begin() + k, ls.end(), endTime + 1);
        return (int)(it2 - it1);
    }
};
