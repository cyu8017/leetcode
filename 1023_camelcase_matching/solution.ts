// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

function camelMatch(queries: string[], pattern: string): boolean[] {
    const matches = (q: string): boolean => {
        let i = 0;
        for (const ch of q) {
            if (i < pattern.length && ch === pattern[i]) i++;
            else if (ch >= 'A' && ch <= 'Z') return false;
        }
        return i === pattern.length;
    };
    return queries.map(matches);
}
