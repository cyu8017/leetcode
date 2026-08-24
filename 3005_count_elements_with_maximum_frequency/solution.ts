// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

export function maxFrequencyElements(nums: any): any {
    const cnt = new Array(101).fill(0);
    for (const x of nums) cnt[x]++;
    let mx = -1, ans = 0;
    for (const x of cnt) {
        if (mx < x) {
            mx = x;
            ans = x;
        } else if (mx === x) {
            ans += x;
        }
    }
    return ans;
}
