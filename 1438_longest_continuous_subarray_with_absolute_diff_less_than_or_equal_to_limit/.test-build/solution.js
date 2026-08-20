"use strict";
function longestSubarray(nums, limit) {
    const minq = [], maxq = [];
    let left = 0, answer = 0;
    for (let right = 0; right < nums.length; right++) {
        while (minq.length && nums[minq[minq.length - 1]] > nums[right])
            minq.pop();
        minq.push(right);
        while (maxq.length && nums[maxq[maxq.length - 1]] < nums[right])
            maxq.pop();
        maxq.push(right);
        while (nums[maxq[0]] - nums[minq[0]] > limit) {
            if (minq[0] === left)
                minq.shift();
            if (maxq[0] === left)
                maxq.shift();
            left++;
        }
        answer = Math.max(answer, right - left + 1);
    }
    return answer;
}
