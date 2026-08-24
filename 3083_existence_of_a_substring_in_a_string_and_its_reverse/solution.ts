// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

export function isSubstringPresent(s: string): boolean {
    const st = Array.from({ length: 26 }, () => new Array(26).fill(false));
    for (let i = 0; i + 1 < s.length; i++)
        st[s.charCodeAt(i + 1) - 97][s.charCodeAt(i) - 97] = true;
    for (let i = 0; i + 1 < s.length; i++)
        if (st[s.charCodeAt(i) - 97][s.charCodeAt(i + 1) - 97]) return true;
    return false;
}
