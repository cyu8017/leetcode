// LeetCode 3932 - Count K Th Roots In A Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/

export function countKthRoots(l: any, r: any, k: any): any {
        if (k == 1) return r - l + 1;
        let ans = 0;
        for (let x = 0;; x++) {
            let y = 1;
            let tooBig = false;
            for (let i = 0; i < k; i++) {
                if (x != 0 && y > r / x) {
                    tooBig = true;
                    break;
                }
                y *= x;
                if (y > r) break;
            }
            if (tooBig || y > r) break;
            if (l <= y && y <= r) ans++;
        }
        return ans;
    
}
