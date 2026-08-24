// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

export function vowelStrings(words: string[], left: number, right: number): number {
    const isV = (c) => c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u';
    let ans = 0;
    for (let i = left; i <= right; ++i) {
        const w = words[i];
        if (isV(w[0]) && isV(w[w.length - 1])) ans++;
    }
    return ans;
}
