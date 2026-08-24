// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

export function countPrefixSuffixPairs(words: any): any {
    let ans = 0;
    for (let i = 0; i < words.length; i++) {
        const s = words[i];
        for (let j = i + 1; j < words.length; j++) {
            const t = words[j];
            if (t.length >= s.length && t.startsWith(s) && t.endsWith(s))
                ans++;
        }
    }
    return ans;
}
