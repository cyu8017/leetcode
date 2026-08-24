// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

var countSubarrays = function(nums, k, m) {
    const f = (lim) => {
        const cnt = new Map();
        let ans = 0, l = 0, t = 0;
        for (const x of nums) {
            const c = (cnt.get(x) || 0) + 1;
            cnt.set(x, c);
            if (c === m) t++;
            while (cnt.size >= lim && t >= k) {
                const y = nums[l++];
                const cy = cnt.get(y) - 1;
                if (cy === m - 1) t--;
                if (cy === 0) cnt.delete(y);
                else cnt.set(y, cy);
            }
            ans += l;
        }
        return ans;
    };
    return f(k) - f(k + 1);
};
