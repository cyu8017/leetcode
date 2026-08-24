// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

export function findAndReplacePattern(words: string[], pattern: string): string[] {
    const match = (w, p) => {
        const m1 = new Map(), m2 = new Map();
        for (let i = 0; i < w.length; i++) {
            const a = w[i], b = p[i];
            if (!m1.has(a)) m1.set(a, b);
            if (!m2.has(b)) m2.set(b, a);
            if (m1.get(a) !== b || m2.get(b) !== a) return false;
        }
        return true;
    };
    return words.filter((w) => match(w, pattern));
}
