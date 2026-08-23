// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

#include <algorithm>
#include <vector>

class Solution {
    bool rotationMatches(const std::vector<int>& block, const std::vector<int>& target) {
        int k = (int)block.size();
        std::vector<int> prefix(k, 0);
        for (int i = 1; i < k; i++) {
            int j = prefix[i - 1];
            while (j > 0 && target[i] != target[j]) j = prefix[j - 1];
            if (target[i] == target[j]) j++;
            prefix[i] = j;
        }
        int matched = 0;
        for (int i = 0; i < 2 * k - 1; i++) {
            int x = block[i % k];
            while (matched > 0 && x != target[matched]) matched = prefix[matched - 1];
            if (x == target[matched]) matched++;
            if (matched == k) return true;
        }
        return false;
    }

public:
    int sumOfSortableIntegers(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        std::vector<int> divisors;
        for (int d = 1; d * d <= n; d++) {
            if (n % d == 0) {
                divisors.push_back(d);
                if (d * d != n) divisors.push_back(n / d);
            }
        }
        int answer = 0;
        for (int k : divisors) {
            bool ok = true;
            for (int start = 0; start < n; start += k) {
                std::vector<int> block(nums.begin() + start, nums.begin() + start + k);
                std::vector<int> target(sorted.begin() + start, sorted.begin() + start + k);
                if (!rotationMatches(block, target)) {
                    ok = false;
                    break;
                }
            }
            if (ok) answer += k;
        }
        return answer;
    }
};
