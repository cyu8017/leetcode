// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

export function equationsPossible(equations: string[]): boolean {
    const parent = Array.from({length: 26}, (_, i) => i);
    const find = (x) => parent[x] === x ? x : (parent[x] = find(parent[x]));
    for (const eq of equations) {
        if (eq[1] === '=') parent[find(eq.charCodeAt(0) - 97)] = find(eq.charCodeAt(3) - 97);
    }
    for (const eq of equations) {
        if (eq[1] === '!' && find(eq.charCodeAt(0) - 97) === find(eq.charCodeAt(3) - 97)) return false;
    }
    return true;
}
