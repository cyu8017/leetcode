// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

export function replicate(self: string, times: number): string {
    let res = '';
    for (let i = 0; i < times; i++) res += self;
    return res;
}
