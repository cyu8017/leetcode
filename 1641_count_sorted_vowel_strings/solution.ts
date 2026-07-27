// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

function countVowelStrings(n: number): number {
    const comb = (N: number, R: number): number => {
        let num = 1, den = 1;
        for (let i = 0; i < R; i++) {
            num *= N - i;
            den *= i + 1;
        }
        return num / den;
    };
    return comb(n + 4, 4);
}
