// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

export function minimumChairs(s: string): number {
    let cnt = 0, left = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === 'E') {
            if (left > 0) left--;
            else cnt++;
        } else left++;
    }
    return cnt;
}
