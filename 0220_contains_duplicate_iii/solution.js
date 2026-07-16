// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

/**
 * @param {number[]} nums
 * @param {number} indexDiff
 * @param {number} valueDiff
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, indexDiff, valueDiff) {
    if (indexDiff <= 0 || valueDiff < 0) {
        return false;
    }
    const width = valueDiff + 1;
    const buckets = new Map();

    const bucketId = (num) => (
        num >= 0 ? Math.floor(num / width) : Math.floor((num + 1) / width) - 1
    );

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const bucket = bucketId(num);
        if (buckets.has(bucket)) {
            return true;
        }
        if (buckets.has(bucket - 1) && Math.abs(num - buckets.get(bucket - 1)) <= valueDiff) {
            return true;
        }
        if (buckets.has(bucket + 1) && Math.abs(num - buckets.get(bucket + 1)) <= valueDiff) {
            return true;
        }
        if (buckets.size >= indexDiff) {
            const old = nums[i - indexDiff];
            buckets.delete(bucketId(old));
        }
        buckets.set(bucket, num);
    }
    return false;
};
