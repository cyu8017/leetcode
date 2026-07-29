#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> processQueries(std::vector<int>& queries, int m) {
        std::vector<int> values(m);
        for (int i = 0; i < m; ++i) values[i] = i + 1;
        std::vector<int> answer;
        for (int query : queries) {
            auto it = std::find(values.begin(), values.end(), query);
            int index = (int)(it - values.begin());
            answer.push_back(index);
            values.erase(it);
            values.insert(values.begin(), query);
        }
        return answer;
    }
};
