// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

function smallestEquivalentString(s1: string, s2: string, baseStr: string): string {
    const parent = Array.from({ length: 26 }, (_, i) => i);

    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function union(a: number, b: number): void {
        let ra = find(a);
        let rb = find(b);
        if (ra === rb) return;
        if (ra < rb) parent[rb] = ra;
        else parent[ra] = rb;
    }

    for (let i = 0; i < s1.length; i++) {
        union(s1.charCodeAt(i) - 97, s2.charCodeAt(i) - 97);
    }
    let ans = "";
    for (const c of baseStr) {
        ans += String.fromCharCode(find(c.charCodeAt(0) - 97) + 97);
    }
    return ans;
}
