// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

var numberOfPairs = function(nums1, nums2, queries) {
    const blockSize = 225;
    const n = nums2.length;
    const blocks = Math.floor((n + blockSize - 1) / blockSize);
    const lazy = new Array(blocks).fill(0);
    const freq = Array.from({length: blocks}, () => new Map());
    for (let b = 0; b < blocks; b++) rebuild(freq, nums2, b, blockSize, n);
    const fixed = new Map();
    for (const x of nums1) fixed.set(x, (fixed.get(x) || 0) + 1);
    const answer = [];
    for (const q of queries) {
        if (q[0] === 1) {
            const l = q[1], r = q[2], delta = q[3];
            const first = Math.floor(l / blockSize), last = Math.floor(r / blockSize);
            if (first === last) {
                push(lazy, nums2, first, blockSize, n);
                for (let i = l; i <= r; i++) nums2[i] += delta;
                rebuild(freq, nums2, first, blockSize, n);
                continue;
            }
            push(lazy, nums2, first, blockSize, n);
            for (let i = l; i < (first + 1) * blockSize; i++) nums2[i] += delta;
            rebuild(freq, nums2, first, blockSize, n);
            push(lazy, nums2, last, blockSize, n);
            for (let i = last * blockSize; i <= r; i++) nums2[i] += delta;
            rebuild(freq, nums2, last, blockSize, n);
            for (let b = first + 1; b < last; b++) lazy[b] += delta;
        } else {
            let total = 0;
            for (const [a, countA] of fixed.entries()) {
                const target = q[1] - a;
                for (let b = 0; b < blocks; b++) {
                    const c = freq[b].get(target - lazy[b]);
                    if (c != null) total += countA * c;
                }
            }
            answer.push(total);
        }
    }
    return answer;
};

function rebuild(freq, nums2, b, blockSize, n) {
    freq[b].clear();
    const end = Math.min((b + 1) * blockSize, n);
    for (let i = b * blockSize; i < end; i++) {
        freq[b].set(nums2[i], (freq[b].get(nums2[i]) || 0) + 1);
    }
}

function push(lazy, nums2, b, blockSize, n) {
    if (lazy[b] !== 0) {
        const end = Math.min((b + 1) * blockSize, n);
        for (let i = b * blockSize; i < end; i++) nums2[i] += lazy[b];
        lazy[b] = 0;
    }
}
