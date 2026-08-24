// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/
var minLights = function(lights) {
        let n = lights.length;
        let d = new Array(n).fill(0);
        for (let i = 0; i < n; i++) {
            let v = lights[i];
            if (v > 0) {
                let l = Math.max(0, i - v);
                let r = Math.min(n - 1, i + v);
                d[l]++;
                if (r + 1 < n) d[r + 1]--;
            }
        }
        let s = 0, cnt = 0, ans = 0;
        for (const x of d) {
            s += x;
            if (s == 0) cnt++;
            else {
                ans += (cnt + 2) / 3;
                cnt = 0;
            }
        }
        ans += (cnt + 2) / 3;
        return ans;
    
};
