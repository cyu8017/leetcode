// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort_integers_by_binary_reflection/

var sortByReflection = function(nums) {
    const f = (x) => {
        let y = 0;
        while (x !== 0) {
            y = (y << 1) | (x & 1);
            x >>= 1;
        }
        return y;
    };
    const arr = nums.slice();
    arr.sort((a, b) => {
        const fa = f(a), fb = f(b);
        if (fa !== fb) return fa - fb;
        return a - b;
    });
    for (let i = 0; i < nums.length; i++) nums[i] = arr[i];
    return nums;
};
