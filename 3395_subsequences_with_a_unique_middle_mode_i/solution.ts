// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

export function subsequencesWithMiddleMode(nums: any): any {
    const mod = 1000000007;
    const n = nums.length;
    let ans = 0;
    const uniqueMode = (a) => {
        const freq = new Map();
        for (const x of a) freq.set(x, (freq.get(x) || 0) + 1);
        let best = 0, cnt = 0;
        for (const f of freq.values()) {
            if (f > best) { best = f; cnt = 1; }
            else if (f === best) cnt++;
        }
        return cnt === 1;
    };
    for (let mid = 2; mid < n - 2; mid++) {
        for (let a = 0; a < mid; a++) {
            for (let b = a + 1; b < mid; b++) {
                for (let c = mid + 1; c < n; c++) {
                    for (let d = c + 1; d < n; d++) {
                        if (uniqueMode([nums[a], nums[b], nums[mid], nums[c], nums[d]])) ans++;
                    }
                }
            }
        }
    }
    return ans % mod;
}
