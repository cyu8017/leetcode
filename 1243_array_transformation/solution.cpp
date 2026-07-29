// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

#include <vector>

class Solution {
public:
    std::vector<int> transformArray(std::vector<int> arr) {
        while (true) {
            std::vector<int> nxt = arr;
            for (int i = 1; i + 1 < static_cast<int>(arr.size()); ++i) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) {
                    ++nxt[i];
                } else if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                    --nxt[i];
                }
            }
            if (nxt == arr) {
                return arr;
            }
            arr.swap(nxt);
        }
    }
};
