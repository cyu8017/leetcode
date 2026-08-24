// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/

export function isAdjacentDiffAtMostTwo(s: any): any {
        for (let i = 1; i < s.length; i++) {
            if (Math.abs(s[i - 1] - s[i]) > 2) return false;
        }
        return true;
    
}
