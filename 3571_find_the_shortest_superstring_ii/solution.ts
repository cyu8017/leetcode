// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

export function shortestSuperstring(s1: any, s2: any): any {
    if (s1.length > s2.length) return shortestSuperstring(s2, s1);
    const m = s1.length;
    if (s2.includes(s1)) return s2;
    for (let i = 0; i < m; i++) {
        if (s2.startsWith(s1.substring(i))) return s1.substring(0, i) + s2;
        const len = m - i;
        if (s2.length >= len && s2.substring(s2.length - len) === s1.substring(0, len))
            return s2 + s1.substring(m - i);
    }
    return s1 + s2;
}
