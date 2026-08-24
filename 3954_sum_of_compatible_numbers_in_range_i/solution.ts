// LeetCode 3954 - Sum Of Compatible Numbers In Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

export function sumOfGoodIntegers(n: any, k: any): any {
        let start = Math.max(1, n - k);
        let end = n + k;
        let ans = 0;
        for (let x = start; x <= end; x++) {
            if ((n & x) == 0) ans += x;
        }
        return ans;
    
}
