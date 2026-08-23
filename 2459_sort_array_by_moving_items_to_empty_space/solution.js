// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

/**
 * @param {number[]} nums
 * @return {number}
 */
var sortArray = function(nums) {
    const solveOne = (startZero) => {
        const n = nums.length;
        const arr = nums.slice();
        const pos = new Map();
        for (let i = 0; i < n; i++) pos.set(arr[i], i);
        let ops = 0;
        while (true) {
            const empty = pos.get(0);
            const should = startZero ? empty : (empty === n - 1 ? 0 : empty + 1);
            if (arr[empty] === should) {
                let found = -1;
                for (let i = 0; i < n; i++) {
                    const want = startZero ? i : (i === n - 1 ? 0 : i + 1);
                    if (arr[i] !== want) { found = i; break; }
                }
                if (found === -1) return ops;
                const v = arr[found];
                arr[empty] = arr[found];
                arr[found] = 0;
                pos.set(0, found);
                pos.set(v, empty);
                ops++;
                continue;
            }
            const j = pos.get(should);
            const vv = arr[j];
            arr[empty] = arr[j];
            arr[j] = 0;
            pos.set(0, j);
            pos.set(vv, empty);
            ops++;
        }
    };
    return Math.min(solveOne(true), solveOne(false));
};
