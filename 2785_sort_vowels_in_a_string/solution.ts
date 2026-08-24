// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

export function sortVowels(s: string): string {
    const isVowel = (c) => 'aeiouAEIOU'.includes(c);
    const vowels = [];
    for (const c of s) if (isVowel(c)) vowels.push(c);
    vowels.sort();
    const arr = s.split('');
    let vi = 0;
    for (let i = 0; i < arr.length; i++) if (isVowel(arr[i])) arr[i] = vowels[vi++];
    return arr.join('');
}
