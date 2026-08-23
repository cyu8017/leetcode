// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<long long> numberOfPairs(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<std::vector<int>>& queries) {
        const int blockSize = 225;
        int n = (int)nums2.size();
        int blocks = (n + blockSize - 1) / blockSize;
        std::vector<int> lazy(blocks, 0);
        std::vector<std::unordered_map<int, int>> freq(blocks);
        auto rebuild = [&](int b) {
            freq[b].clear();
            int end = std::min((b + 1) * blockSize, n);
            for (int i = b * blockSize; i < end; i++) freq[b][nums2[i]]++;
        };
        auto push = [&](int b) {
            if (lazy[b] != 0) {
                int end = std::min((b + 1) * blockSize, n);
                for (int i = b * blockSize; i < end; i++) nums2[i] += lazy[b];
                lazy[b] = 0;
            }
        };
        for (int b = 0; b < blocks; b++) rebuild(b);
        std::unordered_map<int, int> fixed;
        for (int x : nums1) fixed[x]++;
        std::vector<long long> answer;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int l = q[1], r = q[2], delta = q[3];
                int first = l / blockSize, last = r / blockSize;
                if (first == last) {
                    push(first);
                    for (int i = l; i <= r; i++) nums2[i] += delta;
                    rebuild(first);
                    continue;
                }
                push(first);
                for (int i = l; i < (first + 1) * blockSize; i++) nums2[i] += delta;
                rebuild(first);
                push(last);
                for (int i = last * blockSize; i <= r; i++) nums2[i] += delta;
                rebuild(last);
                for (int b = first + 1; b < last; b++) lazy[b] += delta;
            } else {
                long long total = 0;
                for (auto& [a, countA] : fixed) {
                    int target = q[1] - a;
                    for (int b = 0; b < blocks; b++) {
                        auto it = freq[b].find(target - lazy[b]);
                        if (it != freq[b].end()) total += (long long)countA * it->second;
                    }
                }
                answer.push_back(total);
            }
        }
        return answer;
    }
};
