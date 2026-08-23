// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

using System.Collections.Generic;

public class Solution {
    public bool ContainsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        if (indexDiff <= 0 || valueDiff < 0) {
            return false;
        }
        long width = (long)valueDiff + 1;
        var buckets = new Dictionary<long, long>();

        for (int i = 0; i < nums.Length; i++) {
            long num = nums[i];
            long bucket = BucketId(num, width);
            if (buckets.ContainsKey(bucket)) {
                return true;
            }
            if (buckets.TryGetValue(bucket - 1, out long prev) && System.Math.Abs(num - prev) <= valueDiff) {
                return true;
            }
            if (buckets.TryGetValue(bucket + 1, out long next) && System.Math.Abs(num - next) <= valueDiff) {
                return true;
            }
            if (buckets.Count >= indexDiff) {
                buckets.Remove(BucketId(nums[i - indexDiff], width));
            }
            buckets[bucket] = num;
        }
        return false;
    }

    private static long BucketId(long num, long width) {
        return num >= 0 ? num / width : (num + 1) / width - 1;
    }
}
