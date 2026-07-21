// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

function numDifferentIntegers(word: string): number {
    const seen = new Set<string>();
    const matches = word.match(/\d+/g) || [];
    for (const m of matches) {
        seen.add(BigInt(m).toString());
    }
    return seen.size;
}
