// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

export function countDistinctIntegers(nums: number[]): number {
    const rev = (x) => {
        let r = 0;
        while (x > 0) {
            r = r * 10 + x % 10;
            x = Math.floor(x / 10);
        }
        return r;
    };
    const seen = new Set();
    for (const x of nums) {
        seen.add(x);
        seen.add(rev(x));
    }
    return seen.size;
}
