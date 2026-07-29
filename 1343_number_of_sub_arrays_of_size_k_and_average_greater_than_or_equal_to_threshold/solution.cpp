#include <vector>

class Solution {
public:
    int numOfSubarrays(std::vector<int>& arr, int k, int threshold) {
        long long window = 0;
        for (int i = 0; i < k; ++i) window += arr[i];
        int answer = window >= 1LL * k * threshold;
        for (int i = k; i < (int)arr.size(); ++i) {
            window += arr[i] - arr[i - k];
            answer += window >= 1LL * k * threshold;
        }
        return answer;
    }
};
