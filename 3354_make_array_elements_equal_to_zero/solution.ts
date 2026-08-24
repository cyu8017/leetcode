// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

export function countValidSelections(nums: any): any {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] !== 0) continue;
        for (const dir of [-1, 1]) {
            const a = nums.slice();
            let cur = i, d = dir;
            while (cur >= 0 && cur < n) {
                if (a[cur] === 0) cur += d;
                else {
                    a[cur]--;
                    d = -d;
                    cur += d;
                }
            }
            let ok = true;
            for (const v of a) if (v !== 0) { ok = false; break; }
            if (ok) ans++;
        }
    }
    return ans;
}
