// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

#include <map>
#include <unordered_map>
#include <vector>

class RideSharingSystem {
    int t = 0;
    std::map<int, int> riders;
    std::map<int, int> drivers;
    std::unordered_map<int, int> d;

public:
    RideSharingSystem() {}

    void addRider(int riderId) {
        d[riderId] = t;
        riders[t] = riderId;
        t++;
    }

    void addDriver(int driverId) {
        drivers[t] = driverId;
        t++;
    }

    std::vector<int> matchDriverWithRider() {
        if (riders.empty() || drivers.empty()) return {-1, -1};
        auto dit = drivers.begin();
        auto rit = riders.begin();
        int driverId = dit->second, riderId = rit->second;
        drivers.erase(dit);
        riders.erase(rit);
        return {driverId, riderId};
    }

    void cancelRider(int riderId) {
        auto it = d.find(riderId);
        if (it == d.end()) return;
        riders.erase(it->second);
    }
};
