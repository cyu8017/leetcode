// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

export function minOrAfterOperations(nums: any, k: any): any {
    let ans = 0, rans = 0;
    for (let i = 29; i >= 0; i--) {
        const test = ans + (1 << i);
        let cnt = 0, val = 0;
        for (const num of nums) {
            if (val === 0) val = test & num;
            else val &= test & num;
            if (val !== 0) cnt++;
        }
        if (cnt > k) rans += (1 << i);
        else ans += (1 << i);
    }
    return rans;
}
