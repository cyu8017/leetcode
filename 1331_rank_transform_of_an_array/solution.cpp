#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> arrayRankTransform(std::vector<int>& arr) {
        std::vector<int> sorted = arr;
        std::sort(sorted.begin(), sorted.end());
        sorted.erase(std::unique(sorted.begin(), sorted.end()), sorted.end());
        std::vector<int> answer;
        for (int x : arr)
            answer.push_back((int)(std::lower_bound(sorted.begin(), sorted.end(), x) - sorted.begin()) + 1);
        return answer;
    }
};
