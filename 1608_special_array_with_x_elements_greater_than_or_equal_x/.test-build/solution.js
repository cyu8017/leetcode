"use strict";
// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
function specialArray(nums) {
    for (let x = 0; x <= nums.length; x++) {
        let cnt = 0;
        for (const v of nums)
            if (v >= x)
                cnt++;
        if (cnt === x)
            return x;
    }
    return -1;
}
