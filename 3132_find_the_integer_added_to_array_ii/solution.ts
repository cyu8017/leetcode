// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

export function minimumAddedInteger(nums1: number[], nums2: number[]): number {
    nums1 = nums1.slice().sort((a, b) => a - b);
    nums2 = nums2.slice().sort((a, b) => a - b);
    const ok = (x) => {
        let i = 0, j = 0, cnt = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums2[j] - nums1[i] !== x) cnt++;
            else j++;
            i++;
        }
        return cnt <= 2;
    };
    let ans = 1 << 30;
    for (let t = 0; t < 3; t++) {
        const x = nums2[0] - nums1[t];
        if (ok(x)) ans = Math.min(ans, x);
    }
    return ans;
}
