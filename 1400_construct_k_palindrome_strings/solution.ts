// LeetCode 1400: Construct K Palindrome Strings

function canConstruct(s: any, k: any): any {
    if (s.length < k) return false;
    const count = Array(26).fill(0);
    for (const ch of s) count[ch.charCodeAt(0) - 97]++;
    return count.filter((value: any): any => value % 2).length <= k;
}
