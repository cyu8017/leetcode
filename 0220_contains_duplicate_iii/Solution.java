// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        if (indexDiff <= 0 || valueDiff < 0) {
            return false;
        }
        long width = (long) valueDiff + 1;
        Map<Long, Long> buckets = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            long num = nums[i];
            long bucket = bucketId(num, width);
            if (buckets.containsKey(bucket)) {
                return true;
            }
            if (buckets.containsKey(bucket - 1)
                && Math.abs(num - buckets.get(bucket - 1)) <= valueDiff) {
                return true;
            }
            if (buckets.containsKey(bucket + 1)
                && Math.abs(num - buckets.get(bucket + 1)) <= valueDiff) {
                return true;
            }
            if (buckets.size() >= indexDiff) {
                long old = nums[i - indexDiff];
                buckets.remove(bucketId(old, width));
            }
            buckets.put(bucket, num);
        }
        return false;
    }

    private long bucketId(long num, long width) {
        return num >= 0 ? num / width : (num + 1) / width - 1;
    }
}
