// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

export function minimumPushes(word: any): any {
    const n = word.length;
    let ans = 0, k = 1;
    for (let i = 0; i < ((n / 8) | 0); i++) {
        ans += k * 8;
        k++;
    }
    ans += k * (n % 8);
    return ans;
}
