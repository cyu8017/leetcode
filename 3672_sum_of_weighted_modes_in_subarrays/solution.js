// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

var modeWeight = function(nums, k) {
    const cnt = new Map();
    const pq = [];
    const push = (freq, val) => {
        pq.push([freq, -val]);
        pq.sort((a, b) => a[0] !== b[0] ? b[0] - a[0] : a[1] - b[1]);
    };
    const getMode = () => {
        while (true) {
            const top = pq[0];
            const freq = top[0], val = -top[1];
            if ((cnt.get(val) || 0) === freq) return freq * val;
            pq.shift();
        }
    };
    for (let i = 0; i < k; i++) {
        const x = nums[i];
        cnt.set(x, (cnt.get(x) || 0) + 1);
        push(cnt.get(x), x);
    }
    let ans = getMode();
    for (let i = k; i < nums.length; i++) {
        const x = nums[i], y = nums[i - k];
        cnt.set(x, (cnt.get(x) || 0) + 1);
        cnt.set(y, (cnt.get(y) || 0) - 1);
        push(cnt.get(x), x);
        push(cnt.get(y), y);
        ans += getMode();
    }
    return ans;
};
