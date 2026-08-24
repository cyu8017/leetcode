// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

export function robotWithString(s: string): string {
    const n = s.length;
    const minSuf = Array(n + 1);
    minSuf[n] = String.fromCharCode('z'.charCodeAt(0) + 1);
    for (let i = n - 1; i >= 0; i--)
        minSuf[i] = s[i] < minSuf[i + 1] ? s[i] : minSuf[i + 1];
    const stack = [];
    const ans = [];
    for (let i = 0; i < n; i++) {
        stack.push(s[i]);
        while (stack.length && stack[stack.length - 1] <= minSuf[i + 1])
            ans.push(stack.pop());
    }
    while (stack.length) ans.push(stack.pop());
    return ans.join('');
}
