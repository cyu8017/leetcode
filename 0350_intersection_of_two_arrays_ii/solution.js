// LeetCode 0350 - Intersection of Two Arrays II
var intersect = function(nums1, nums2) {
    const counts = new Map();
    for (const num of nums1) {
        counts.set(num, (counts.get(num) || 0) + 1);
    }

    const result = [];
    for (const num of nums2) {
        if ((counts.get(num) || 0) > 0) {
            result.push(num);
            counts.set(num, counts.get(num) - 1);
        }
    }

    return result;
};
