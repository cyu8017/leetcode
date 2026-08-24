// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

export function recoverArray(nums: number[]): number[] {
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length;
    for (let i = 1; i < n; i++) {
        const diff = nums[i] - nums[0];
        if (diff === 0 || diff % 2 !== 0) continue;
        const k = diff / 2;
        const used = new Array(n).fill(false);
        used[0] = used[i] = true;
        const ans = [(nums[0] + nums[i]) / 2];
        let l = 0, r = i;
        let ok = true;
        while (ans.length < n / 2) {
            while (l < n && used[l]) l++;
            if (l === n) { ok = false; break; }
            const need = nums[l] + 2 * k;
            while (r < n && (used[r] || nums[r] < need)) r++;
            if (r === n || nums[r] !== need) { ok = false; break; }
            used[l] = used[r] = true;
            ans.push(nums[l] + k);
        }
        if (ok) return ans;
    }
    return [];
}
