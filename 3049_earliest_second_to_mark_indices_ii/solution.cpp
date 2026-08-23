// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
    static std::unordered_map<int, int> getSecondToIndex(const std::vector<int>& nums, const std::vector<int>& changeIndices) {
        std::unordered_map<int, int> indexToFirstSecond;
        for (int second = 0; second < (int)changeIndices.size(); second++) {
            int index = changeIndices[second] - 1;
            if (nums[index] > 0 && !indexToFirstSecond.count(index))
                indexToFirstSecond[index] = second;
        }
        std::unordered_map<int, int> secondToIndex;
        for (auto& [index, second] : indexToFirstSecond) secondToIndex[second] = index;
        return secondToIndex;
    }
    static bool canMark(const std::vector<int>& nums, const std::unordered_map<int, int>& secondToIndex, int maxSecond, long long numsSum) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> h;
        int marks = 0;
        for (int second = maxSecond - 1; second >= 0; second--) {
            auto it = secondToIndex.find(second);
            if (it != secondToIndex.end()) {
                h.push(nums[it->second]);
                if (marks == 0) {
                    h.pop();
                    marks++;
                } else {
                    marks--;
                }
            } else {
                marks++;
            }
        }
        int heapSize = (int)h.size();
        long long heapSum = 0;
        while (!h.empty()) {
            heapSum += h.top();
            h.pop();
        }
        long long decrementAndMarkCost = numsSum - heapSum + (long long)(nums.size() - heapSize);
        long long zeroAndMarkCost = (long long)heapSize + heapSize;
        return decrementAndMarkCost + zeroAndMarkCost <= maxSecond;
    }
public:
    int earliestSecondToMarkIndices(std::vector<int>& nums, std::vector<int>& changeIndices) {
        auto secondToIndex = getSecondToIndex(nums, changeIndices);
        long long numsSum = 0;
        for (int v : nums) numsSum += v;
        int l = 0, r = (int)changeIndices.size() + 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (canMark(nums, secondToIndex, m, numsSum)) r = m;
            else l = m + 1;
        }
        return l <= (int)changeIndices.size() ? l : -1;
    }
};
