// LeetCode 0324 - Wiggle Sort II
var wiggleSort = function(nums) {
    const sorted = [...nums].sort((a, b) => a - b);
    let left = Math.floor((nums.length - 1) / 2);
    let right = nums.length - 1;
    for (let index = 0; index < nums.length; index += 1) {
        if (index % 2 === 0) nums[index] = sorted[left--];
        else nums[index] = sorted[right--];
    }
};
