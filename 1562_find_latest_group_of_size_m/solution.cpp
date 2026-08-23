// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int findLatestStep(std::vector<int>& arr, int m) {
        if (m == static_cast<int>(arr.size())) {
            return m;
        }
        std::unordered_map<int, int> lengths;
        int answer = -1;
        for (int step = 1; step <= static_cast<int>(arr.size()); ++step) {
            const int x = arr[step - 1];
            const int left = lengths.count(x - 1) ? lengths[x - 1] : 0;
            const int right = lengths.count(x + 1) ? lengths[x + 1] : 0;
            const int size = left + 1 + right;
            lengths[x - left] = size;
            lengths[x + right] = size;
            if (left == m || right == m) {
                answer = step - 1;
            }
        }
        return answer;
    }
};
