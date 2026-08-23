// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

var minSplitMerge = function(nums1, nums2) {
    const n = nums1.length;
    const toArr = (nums) => {
        const t = new Array(6).fill(0);
        for (let i = 0; i < n; i++) t[i] = nums[i];
        return t;
    };
    const key = (a) => a.join(',');
    const start = toArr(nums1);
    const target = toArr(nums2);
    const vis = new Set([key(start)]);
    let q = [start];
    for (let ans = 0; ; ans++) {
        const nq = [];
        for (const cur of q) {
            if (key(cur) === key(target)) return ans;
            for (let l = 0; l < n; l++) {
                for (let r = l; r < n; r++) {
                    const remain = [];
                    const sub = [];
                    for (let i = 0; i < l; i++) remain.push(cur[i]);
                    for (let i = r + 1; i < n; i++) remain.push(cur[i]);
                    for (let i = l; i <= r; i++) sub.push(cur[i]);
                    for (let pos = 0; pos <= remain.length; pos++) {
                        const nxtSlice = remain.slice(0, pos).concat(sub).concat(remain.slice(pos));
                        const nxt = toArr(nxtSlice);
                        const k = key(nxt);
                        if (!vis.has(k)) {
                            vis.add(k);
                            nq.push(nxt);
                        }
                    }
                }
            }
        }
        q = nq;
    }
};
