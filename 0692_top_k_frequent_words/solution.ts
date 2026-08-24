// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

export function topKFrequent(words: string[], k: number): string[] {
    const counts = new Map();
    for (const word of words) counts.set(word, (counts.get(word) || 0) + 1);
    const ordered = Array.from(counts.keys());
    ordered.sort((a, b) => {
        const ca = counts.get(a), cb = counts.get(b);
        if (ca !== cb) return cb - ca;
        return a < b ? -1 : a > b ? 1 : 0;
    });
    return ordered.slice(0, k);
}
