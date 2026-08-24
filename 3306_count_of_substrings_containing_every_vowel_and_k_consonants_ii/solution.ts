// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

function isVowel(c: any): any {
    return c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u';
}function atLeast(word: any, k: any): any {
    const cnt = new Map();
    let cons = 0, l = 0, ans = 0;
    for (let r = 0; r < word.length; r++) {
        const c = word[r];
        if (isVowel(c)) cnt.set(c, (cnt.get(c) || 0) + 1);
        else cons++;
        while (cnt.size === 5 && cons >= k) {
            ans += word.length - r;
            const c2 = word[l];
            if (isVowel(c2)) {
                const nv = cnt.get(c2) - 1;
                if (nv === 0) cnt.delete(c2);
                else cnt.set(c2, nv);
            } else cons--;
            l++;
        }
    }
    return ans;
}export function countOfSubstrings(word: any, k: any): any {
    return atLeast(word, k) - atLeast(word, k + 1);
}
