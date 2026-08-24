// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

export function minimumOperations(nums: any): any {
    let list = nums.slice();
    let ops = 0;
    while (true) {
        const seen = new Set();
        let dup = false;
        for (const x of list) {
            if (seen.has(x)) { dup = true; break; }
            seen.add(x);
        }
        if (!dup) return ops;
        if (list.length <= 3) return ops + 1;
        list = list.slice(3);
        ops++;
    }
}
