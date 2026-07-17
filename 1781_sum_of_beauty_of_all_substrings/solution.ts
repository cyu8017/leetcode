// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

function beautySum(s: string): number {
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        const freq = new Array(26).fill(0);
        for (let j = i; j < s.length; j++) {
            freq[s.charCodeAt(j) - 97]++;
            let lo = Infinity;
            let hi = 0;
            for (const count of freq) {
                if (count > 0) {
                    if (count < lo) lo = count;
                    if (count > hi) hi = count;
                }
            }
            ans += hi - lo;
        }
    }
    return ans;
}
