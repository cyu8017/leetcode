#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    double average(std::vector<int>& salary) {
        int mn = *std::min_element(salary.begin(), salary.end());
        int mx = *std::max_element(salary.begin(), salary.end());
        long long sum = std::accumulate(salary.begin(), salary.end(), 0LL);
        return (double)(sum - mn - mx) / (salary.size() - 2);
    }
};
