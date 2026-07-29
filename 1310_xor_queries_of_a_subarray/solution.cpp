#include <vector>

class Solution {
public:
    std::vector<int> xorQueries(std::vector<int>& arr, std::vector<std::vector<int>>& queries) {
        std::vector<int> prefix(1, 0);
        for (int value : arr) prefix.push_back(prefix.back() ^ value);
        std::vector<int> answer;
        for (auto& q : queries) answer.push_back(prefix[q[1] + 1] ^ prefix[q[0]]);
        return answer;
    }
};
