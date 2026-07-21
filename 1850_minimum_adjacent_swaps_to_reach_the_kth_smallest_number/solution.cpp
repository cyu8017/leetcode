// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int getMinSwaps(std::string num, int k) {
        std::vector<char> target(num.begin(), num.end());
        for (int i = 0; i < k; ++i) {
            nextPermutation(target);
        }
        std::vector<char> source(num.begin(), num.end());
        int swaps = 0;
        for (int i = 0; i < static_cast<int>(source.size()); ++i) {
            if (source[i] == target[i]) {
                continue;
            }
            int j = i;
            while (source[j] != target[i]) {
                ++j;
            }
            while (j > i) {
                std::swap(source[j], source[j - 1]);
                ++swaps;
                --j;
            }
        }
        return swaps;
    }

private:
    void nextPermutation(std::vector<char>& arr) {
        int i = static_cast<int>(arr.size()) - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) {
            --i;
        }
        if (i < 0) {
            std::reverse(arr.begin(), arr.end());
            return;
        }
        int j = static_cast<int>(arr.size()) - 1;
        while (arr[j] <= arr[i]) {
            --j;
        }
        std::swap(arr[i], arr[j]);
        std::reverse(arr.begin() + i + 1, arr.end());
    }
};
