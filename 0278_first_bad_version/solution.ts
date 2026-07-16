// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

export class Solution {
    firstBadVersion(this: Solution & { isBadVersion(version: number): boolean }, n: number): number {
        let left = 1;
        let right = n;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (this.isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}

export function isBadVersion(_version: number): boolean {
    return false;
}

const solution = new Solution();
export const firstBadVersion = solution.firstBadVersion.bind(
    Object.assign(solution, { isBadVersion }),
);
