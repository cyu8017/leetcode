// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

#include <algorithm>
#include <unordered_map>
#include <vector>

class MajorityChecker {
public:
    MajorityChecker(std::vector<int>& arr) : arr(arr) {
        for (int i = 0; i < static_cast<int>(arr.size()); ++i) pos[arr[i]].push_back(i);
    }

    int query(int left, int right, int threshold) {
        int candidate = 0, count = 0;
        for (int i = left; i <= right; ++i) {
            if (count == 0) candidate = arr[i];
            count += arr[i] == candidate ? 1 : -1;
        }
        const auto& locs = pos[candidate];
        int freq = static_cast<int>(std::upper_bound(locs.begin(), locs.end(), right) -
                                    std::lower_bound(locs.begin(), locs.end(), left));
        return freq >= threshold ? candidate : -1;
    }

private:
    std::vector<int> arr;
    std::unordered_map<int, std::vector<int>> pos;
};
