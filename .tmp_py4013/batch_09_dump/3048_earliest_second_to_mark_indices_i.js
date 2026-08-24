// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

var earliestSecondToMarkIndices = function(nums, changeIndices) {
    const n = nums.length;
    const m = changeIndices.length;
    function ok(t) {
        const last = new Array(n + 1).fill(0);
        for (let s = 0; s < t; s++) last[changeIndices[s]] = s;
        let decrement = 0, marked = 0;
        for (let s = 0; s < t; s++) {
            const i = changeIndices[s];
            if (last[i] === s) {
                if (decrement < nums[i - 1]) return false;
                decrement -= nums[i - 1];
                marked++;
            } else {
                decrement++;
            }
        }
        return marked === n;
    }
    let l = 0, r = m + 1;
    while (l < r) {
        const mid = (l + r) >> 1;
        if (ok(mid)) r = mid;
        else l = mid + 1;
    }
    return l > m ? -1 : l;
};
