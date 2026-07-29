// LeetCode 1534 - Count Good Triplets
// https://leetcode.com/problems/count-good-triplets/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int countGoodTriplets(std::vector<int>& arr, int a, int b, int c) {
        int answer = 0;
        int n = static_cast<int>(arr.size());
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (std::abs(arr[i] - arr[j]) > a) {
                    continue;
                }
                for (int k = j + 1; k < n; ++k) {
                    if (std::abs(arr[j] - arr[k]) <= b && std::abs(arr[i] - arr[k]) <= c) {
                        answer += 1;
                    }
                }
            }
        }
        return answer;
    }
};
