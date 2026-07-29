// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

#include <algorithm>
#include <climits>
#include <utility>
#include <vector>

class SnapshotArray {
public:
    SnapshotArray(int length) : snapId(0), data(length, {{0, 0}}) {}

    void set(int index, int val) {
        auto& hist = data[index];
        if (hist.back().first == snapId) hist.back().second = val;
        else hist.emplace_back(snapId, val);
    }

    int snap() {
        return snapId++;
    }

    int get(int index, int snap_id) {
        const auto& hist = data[index];
        auto it = std::upper_bound(hist.begin(), hist.end(), std::make_pair(snap_id, INT_MAX));
        --it;
        return it->second;
    }

private:
    int snapId;
    std::vector<std::vector<std::pair<int, int>>> data;
};
