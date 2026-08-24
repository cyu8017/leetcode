// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse_words_with_same_vowel_count/

export function reverseWords(s: any): any {
    const calc = (w) => {
        let cnt = 0;
        for (const c of w) {
            if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u') cnt++;
        }
        return cnt;
    };
    const words = s.trim().split(/\s+/);
    const cnt = calc(words[0]);
    let ans = words[0];
    for (let i = 1; i < words.length; i++) {
        let w = words[i];
        if (calc(w) === cnt) w = w.split('').reverse().join('');
        ans += ' ' + w;
    }
    return ans;
}
