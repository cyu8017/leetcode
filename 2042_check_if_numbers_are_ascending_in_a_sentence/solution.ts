// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

export function areNumbersAscending(s: string): boolean {
    let prev = -1;
    for (const tok of s.split(" ")) {
        if (!tok) continue;
        if (tok[0] >= '0' && tok[0] <= '9') {
            const v = parseInt(tok, 10);
            if (v <= prev) return false;
            prev = v;
        }
    }
    return true;
}
