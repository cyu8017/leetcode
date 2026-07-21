// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

function countPairs(nums1: number[], nums2: number[]): number {
    const diff = nums1.map((a, i) => a - nums2[i]).sort((a, b) => a - b);
    let answer = 0;
    const n = diff.length;
    for (let i = 0; i < n; i++) {
        const target = -diff[i];
        let lo = i + 1, hi = n;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (diff[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        answer += n - lo;
    }
    return answer;
}
