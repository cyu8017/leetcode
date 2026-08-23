// LeetCode 0327 - Count of Range Sum
// https://leetcode.com/problems/count-of-range-sum/

#include <vector>

class Solution {
    long long mergeSort(
        std::vector<long long>& prefix,
        std::vector<long long>& temp,
        int left,
        int right,
        int lower,
        int upper
    ) {
        if (left >= right) {
            return 0;
        }
        int mid = left + (right - left) / 2;
        long long count = mergeSort(prefix, temp, left, mid, lower, upper) +
            mergeSort(prefix, temp, mid + 1, right, lower, upper);

        int start = mid + 1;
        int end = mid + 1;
        for (int index = left; index <= mid; index++) {
            while (start <= right && prefix[start] - prefix[index] < lower) {
                start += 1;
            }
            while (end <= right && prefix[end] - prefix[index] <= upper) {
                end += 1;
            }
            count += end - start;
        }

        int tempLeft = left;
        int tempRight = mid + 1;
        int write = left;
        while (tempLeft <= mid && tempRight <= right) {
            if (prefix[tempLeft] <= prefix[tempRight]) {
                temp[write++] = prefix[tempLeft++];
            } else {
                temp[write++] = prefix[tempRight++];
            }
        }
        while (tempLeft <= mid) {
            temp[write++] = prefix[tempLeft++];
        }
        while (tempRight <= right) {
            temp[write++] = prefix[tempRight++];
        }
        for (int index = left; index <= right; index++) {
            prefix[index] = temp[index];
        }
        return count;
    }

public:
    int countRangeSum(std::vector<int>& nums, int lower, int upper) {
        std::vector<long long> prefix = {0};
        for (int num : nums) {
            prefix.push_back(prefix.back() + num);
        }
        std::vector<long long> temp(prefix.size(), 0);
        return static_cast<int>(mergeSort(prefix, temp, 0, static_cast<int>(prefix.size()) - 1, lower, upper));
    }
};
