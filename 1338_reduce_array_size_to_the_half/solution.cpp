#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minSetSize(std::vector<int>& arr) {
        std::unordered_map<int, int> freq;
        for (int x : arr) ++freq[x];
        std::vector<int> counts;
        for (auto& [_, c] : freq) counts.push_back(c);
        std::sort(counts.begin(), counts.end(), std::greater<int>());
        int removed = 0;
        for (int i = 0; i < (int)counts.size(); ++i) {
            removed += counts[i];
            if (removed * 2 >= (int)arr.size()) return i + 1;
        }
        return 0;
    }
};
