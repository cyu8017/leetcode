// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

export function largestInteger(n: any, s: any): any {
        if (n * 9 < s) return -1;
        let ans = 0;
        for (let i = 0; i < n; i++) {
            let x = s < 9 ? s : 9;
            ans = ans * 10 + x;
            s -= x;
        }
        return ans;
    
}
