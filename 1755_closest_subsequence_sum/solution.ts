// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

function minAbsDifference(nums: number[], goal: number): number {
    const n = nums.length;
    const left = nums.slice(0, n >> 1);
    const right = nums.slice(n >> 1);

    const sums = (arr: number[]): number[] => {
        let vals = [0];
        for (const x of arr) {
            const next = new Array<number>(vals.length);
            for (let v = 0; v < vals.length; v++) {
                next[v] = vals[v] + x;
            }
            vals = vals.concat(next);
        }
        return vals.sort((p, q) => p - q);
    };

    const a = sums(left);
    const b = sums(right);
    let best = Infinity;
    let j = b.length - 1;
    for (const x of a) {
        while (j > 0 && Math.abs(x + b[j] - goal) >= Math.abs(x + b[j - 1] - goal)) {
            j--;
        }
        best = Math.min(best, Math.abs(x + b[j] - goal));
    }
    return best;
}
