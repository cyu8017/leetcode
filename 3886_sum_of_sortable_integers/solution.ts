// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

function rotationMatches(block: any, target: any): any {
    const k = block.length;
    const prefix = new Array(k).fill(0);
    for (let i = 1; i < k; i++) {
        let j = prefix[i - 1];
        while (j > 0 && target[i] !== target[j]) j = prefix[j - 1];
        if (target[i] === target[j]) j++;
        prefix[i] = j;
    }
    let matched = 0;
    for (let i = 0; i < 2 * k - 1; i++) {
        const x = block[i % k];
        while (matched > 0 && x !== target[matched]) matched = prefix[matched - 1];
        if (x === target[matched]) matched++;
        if (matched === k) return true;
    }
    return false;
}export function sumOfSortableIntegers(nums: any): any {
    const n = nums.length;
    const sorted = nums.slice().sort((a, b) => a - b);
    const divisors = [];
    for (let d = 1; d * d <= n; d++) {
        if (n % d === 0) {
            divisors.push(d);
            if (d * d !== n) divisors.push(Math.floor(n / d));
        }
    }
    let answer = 0;
    for (const k of divisors) {
        let ok = true;
        for (let start = 0; start < n; start += k) {
            const block = nums.slice(start, start + k);
            const target = sorted.slice(start, start + k);
            if (!rotationMatches(block, target)) { ok = false; break; }
        }
        if (ok) answer += k;
    }
    return answer;
}
