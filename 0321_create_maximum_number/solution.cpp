// LeetCode 0321 - Create Maximum Number
// https://leetcode.com/problems/create-maximum-number/

#include <algorithm>
#include <vector>

class Solution {
    std::vector<int> pickMax(const std::vector<int>& values, int count) {
        int drop = static_cast<int>(values.size()) - count;
        std::vector<int> stack;
        for (int value : values) {
            while (drop > 0 && !stack.empty() && stack.back() < value) {
                stack.pop_back();
                drop -= 1;
            }
            stack.push_back(value);
        }
        stack.resize(count);
        return stack;
    }

    bool suffixGreater(
        const std::vector<int>& first,
        int left,
        const std::vector<int>& second,
        int right
    ) {
        while (left < static_cast<int>(first.size()) && right < static_cast<int>(second.size())) {
            if (first[left] != second[right]) {
                return first[left] > second[right];
            }
            left += 1;
            right += 1;
        }
        return static_cast<int>(first.size()) - left >
            static_cast<int>(second.size()) - right;
    }

    std::vector<int> merge(const std::vector<int>& first, const std::vector<int>& second) {
        std::vector<int> result;
        int left = 0;
        int right = 0;
        while (left < static_cast<int>(first.size()) && right < static_cast<int>(second.size())) {
            if (suffixGreater(first, left, second, right)) {
                result.push_back(first[left++]);
            } else {
                result.push_back(second[right++]);
            }
        }
        while (left < static_cast<int>(first.size())) {
            result.push_back(first[left++]);
        }
        while (right < static_cast<int>(second.size())) {
            result.push_back(second[right++]);
        }
        return result;
    }

public:
    std::vector<int> maxNumber(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        std::vector<int> best;
        int minFirst = std::max(0, k - static_cast<int>(nums2.size()));
        int maxFirst = std::min(k, static_cast<int>(nums1.size()));
        for (int takeFirst = minFirst; takeFirst <= maxFirst; takeFirst++) {
            int takeSecond = k - takeFirst;
            std::vector<int> candidate = merge(
                pickMax(nums1, takeFirst),
                pickMax(nums2, takeSecond)
            );
            if (candidate > best) {
                best = candidate;
            }
        }
        return best;
    }
};
