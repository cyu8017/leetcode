// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum_operations_to_make_binary_palindrome/

export function minOperations(nums: any): any {
    const PALS = [];
    const N = 1 << 14;
    const isPalindrome = (s) => {
        const m = s.length;
        for (let i = 0; i < Math.floor(m / 2); i++) if (s[i] !== s[m - 1 - i]) return false;
        return true;
    };
    for (let i = 0; i < N; i++) {
        let sb = '';
        let x = i;
        if (x === 0) sb = '0';
        else {
            while (x > 0) {
                sb += String.fromCharCode(48 + (x & 1));
                x >>= 1;
            }
            sb = sb.split('').reverse().join('');
        }
        if (isPalindrome(sb)) PALS.push(i);
    }
    const lowerBound = (x) => {
        let lo = 0, hi = PALS.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (PALS[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const ans = new Array(nums.length);
    for (let k = 0; k < nums.length; k++) {
        const x = nums[k];
        const it = lowerBound(x);
        let t = Number.MAX_SAFE_INTEGER;
        if (it < PALS.length) t = PALS[it] - x;
        if (it > 0) t = Math.min(t, x - PALS[it - 1]);
        ans[k] = t;
    }
    return ans;
}
