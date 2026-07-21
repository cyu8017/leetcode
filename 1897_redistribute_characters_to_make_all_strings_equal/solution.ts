// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

function makeEqual(words: string[]): boolean {
    const counts = new Map<string, number>();
    for (const word of words) {
        for (const ch of word) {
            counts.set(ch, (counts.get(ch) || 0) + 1);
        }
    }
    const n = words.length;
    for (const total of counts.values()) {
        if (total % n !== 0) return false;
    }
    return true;
}
