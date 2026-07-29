#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int findLeastNumOfUniqueInts(std::vector<int>& arr, int k) {
        std::unordered_map<int, int> freq;
        for (int x : arr) ++freq[x];
        std::vector<int> counts;
        for (auto& [_, c] : freq) counts.push_back(c);
        std::sort(counts.begin(), counts.end());
        int removed = 0;
        for (int count : counts) {
            if (k < count) break;
            k -= count;
            ++removed;
        }
        return (int)counts.size() - removed;
    }
};
