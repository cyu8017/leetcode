// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

export function countCompleteDayPairs(hours: any): any {
    const cnt = new Array(24).fill(0);
    let ans = 0;
    for (const x of hours) {
        ans += cnt[(24 - x % 24) % 24];
        cnt[x % 24]++;
    }
    return ans;
}
