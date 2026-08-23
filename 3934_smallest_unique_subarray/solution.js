// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/
var smallestUniqueSubarray = function(nums) {
        let n = nums.length;
        let sa = new Array(n);
        let rank = nums.slice(0, n);
        for (let i = 0; i < n; i++) sa[i] = i;
        for (let width = 1; width < n; width <<= 1) {
            let w = width;
            let r = rank;
            sa.sort((a,b)=> {
                if (r[a] != r[b]) return ((r[a])-(r[b]));
                let ra = a + w < n ? r[a + w] : -1;
                let rb = b + w < n ? r[b + w] : -1;
                return ((ra)-(rb));
            });
            let next = new Array(n).fill(0);
            for (let i = 1; i < n; i++) {
                let a = sa[i - 1], b = sa[i];
                let different = rank[a] != rank[b];
                let ra = a + width < n ? rank[a + width] : -1;
                let rb = b + width < n ? rank[b + width] : -1;
                next[b] = (different || ra != rb) ? next[a] + 1 : next[a];
            }
            rank = next;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        let pos = new Array(n).fill(0);
        for (let i = 0; i < n; i++) pos[sa[i]] = i;
        let lcp = new Array(Math.max(0, n - 1)).fill(0);
        let height = 0;
        for (let i = 0; i < n; i++) {
            let p = pos[i];
            if (p == n - 1) {
                height = 0;
                continue;
            }
            let j = sa[p + 1];
            while (i + height < n && j + height < n && nums[i + height] == nums[j + height]) height++;
            lcp[p] = height;
            if (height > 0) height--;
        }
        let ans = n;
        for (let p = 0; p < n; p++) {
            let start = sa[p];
            let need = 1;
            if (p > 0 && lcp[p - 1] + 1 > need) need = lcp[p - 1] + 1;
            if (p + 1 < n && lcp[p] + 1 > need) need = lcp[p] + 1;
            if (need <= n - start && need < ans) ans = need;
        }
        return ans;
    
};
