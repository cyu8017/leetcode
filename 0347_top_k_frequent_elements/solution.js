// LeetCode 0347 - Top K Frequent Elements
var topKFrequent = function(nums, k) {
    const counts = new Map();
    for (const num of nums) {
        counts.set(num, (counts.get(num) || 0) + 1);
    }

    const buckets = Array.from({ length: nums.length + 1 }, () => []);
    for (const [value, count] of counts.entries()) {
        buckets[count].push(value);
    }

    const result = [];
    for (let index = buckets.length - 1; index >= 0; index -= 1) {
        for (const value of buckets[index]) {
            result.push(value);
            if (result.length === k) return result;
        }
    }

    return result;
};
