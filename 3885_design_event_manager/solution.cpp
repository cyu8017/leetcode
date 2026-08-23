// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

#include <set>
#include <unordered_map>
#include <utility>
#include <vector>

class EventManager {
    std::set<std::pair<int, int>> sl;
    std::unordered_map<int, int> d;

public:
    EventManager(std::vector<std::vector<int>>& events) {
        for (auto& e : events) {
            int eventId = e[0], priority = e[1];
            sl.insert({-priority, eventId});
            d[eventId] = priority;
        }
    }

    void updatePriority(int eventId, int newPriority) {
        int old = d[eventId];
        sl.erase({-old, eventId});
        sl.insert({-newPriority, eventId});
        d[eventId] = newPriority;
    }

    int pollHighest() {
        if (sl.empty()) return -1;
        auto top = *sl.begin();
        int eventId = top.second;
        sl.erase(sl.begin());
        d.erase(eventId);
        return eventId;
    }
};
