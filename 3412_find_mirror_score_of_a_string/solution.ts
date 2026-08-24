// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

export function calculateScore(s: any): any {
    const stacks = Array.from({ length: 26 }, () => []);
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        const ci = s.charCodeAt(i) - 97;
        const mir = 25 - ci;
        if (stacks[mir].length) {
            const j = stacks[mir].pop();
            ans += i - j;
        } else {
            stacks[ci].push(i);
        }
    }
    return ans;
}
