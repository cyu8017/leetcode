// LeetCode 0416 - Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/

#include <numeric>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        if (total % 2) {
            return false;
        }

        int target = total / 2;
        unordered_set<int> possible = {0};

        for (int value : nums) {
            unordered_set<int> next;
            for (int amount : possible) {
                next.insert(amount);
                if (amount + value <= target) {
                    next.insert(amount + value);
                }
            }
            possible = move(next);
            if (possible.count(target)) {
                return true;
            }
        }

        return possible.count(target);
    }
};
