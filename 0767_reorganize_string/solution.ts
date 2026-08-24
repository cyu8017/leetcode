// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

export function reorganizeString(s: string): string {
    const freq = new Array(26).fill(0);
    for (const ch of s) freq[ch.charCodeAt(0) - 97]++;
    const heap = [];
    for (let i = 0; i < 26; i++) {
        if (freq[i] > 0) heap.push([freq[i], i]);
    }
    heap.sort((a, b) => b[0] - a[0]);
    if (heap.length > 0 && heap[0][0] > Math.floor((s.length + 1) / 2)) return '';
    let result = '';
    while (heap.length >= 2) {
        heap.sort((a, b) => b[0] - a[0]);
        const x = heap.shift();
        const y = heap.shift();
        result += String.fromCharCode(97 + x[1]);
        result += String.fromCharCode(97 + y[1]);
        if (--x[0] > 0) heap.push(x);
        if (--y[0] > 0) heap.push(y);
    }
    if (heap.length > 0) result += String.fromCharCode(97 + heap[0][1]);
    return result;
}
