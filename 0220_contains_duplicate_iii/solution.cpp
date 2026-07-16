// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

#include <cmath>
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool containsNearbyAlmostDuplicate(std::vector<int>& nums, int indexDiff, int valueDiff) {
        if (indexDiff <= 0 || valueDiff < 0) {
            return false;
        }
        long long width = static_cast<long long>(valueDiff) + 1;
        std::unordered_map<long long, long long> buckets;

        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            long long num = nums[i];
            long long bucket = bucketId(num, width);
            if (buckets.count(bucket)) {
                return true;
            }
            if (buckets.count(bucket - 1)
                && std::llabs(num - buckets[bucket - 1]) <= valueDiff) {
                return true;
            }
            if (buckets.count(bucket + 1)
                && std::llabs(num - buckets[bucket + 1]) <= valueDiff) {
                return true;
            }
            if (static_cast<int>(buckets.size()) >= indexDiff) {
                long long old = nums[i - indexDiff];
                buckets.erase(bucketId(old, width));
            }
            buckets[bucket] = num;
        }
        return false;
    }

private:
    static long long bucketId(long long num, long long width) {
        return num >= 0 ? num / width : (num + 1) / width - 1;
    }
};
