// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

function expand(s: string): string[] {
    const groups: string[][] = [];
    let i = 0;
    while (i < s.length) {
        if (s[i] === "{") {
            const j = s.indexOf("}", i);
            groups.push(s.slice(i + 1, j).split(",").sort());
            i = j + 1;
        } else {
            groups.push([s[i]]);
            i++;
        }
    }
    let ans = [""];
    for (const group of groups) {
        const next: string[] = [];
        for (const prefix of ans) {
            for (const ch of group) next.push(prefix + ch);
        }
        ans = next;
    }
    return ans;
}
