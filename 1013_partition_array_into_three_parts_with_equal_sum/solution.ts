// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

function canThreePartsEqualSum(arr: number[]): boolean {
    const total = arr.reduce((a, b) => a + b, 0);
    if (total % 3 !== 0) return false;
    const target = total / 3;
    let parts = 0, cur = 0;
    for (const x of arr) {
        cur += x;
        if (cur === target) {
            parts++;
            cur = 0;
        }
    }
    return parts >= 3;
}
