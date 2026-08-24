// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

export function packKey(i: any, f0: any, f1: any, d0: any, d1: any): any {
        return ((((i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1);
    
}export function maxServe(i: any, f0: any, f1: any, d0: any, d1: any): any {
        if (i == n) return i;
        let key = packKey(i, f0, f1, d0, d1);
        if (memo.has(key)) return memo.get(key);
        let need = dem[i];
        let can0 = f0 >= need;
        let can1 = f1 >= need;
        let best = i;
        if (!can0 && !can1) {
            memo.set(key, best);
            return best;
        }
        if (can0) {
            let nd1 = d1 > d0 ? d1 - d0 : 0;
            best = Math.max(best, maxServe(i + 1, f0 - need, f1, need, nd1));
        }
        if (can1) {
            let nd0 = d0 > d1 ? d0 - d1 : 0;
            best = Math.max(best, maxServe(i + 1, f0, f1 - need, nd0, need));
        }
        memo.set(key, best);
        return best;
    
}export function canWithW(i: any, f0: any, f1: any, d0: any, d1: any): any {
        if (i >= bestServe) return true;
        if (i == n) return true;
        let key = packKey(i, f0, f1, d0, d1);
        if (memo.has(key)) return memo.get(key) == 2;
        let need = dem[i];
        let can0 = f0 >= need;
        let can1 = f1 >= need;
        let ok = false;
        if (!can0 && !can1) {
            memo.set(key, 1);
            return false;
        }
        if (can0 && d0 <= W) {
            let nd1 = d1 > d0 ? d1 - d0 : 0;
            if (canWithW(i + 1, f0 - need, f1, need, nd1)) ok = true;
        }
        if (!ok && can1 && d1 <= W) {
            let nd0 = d0 > d1 ? d0 - d1 : 0;
            if (canWithW(i + 1, f0, f1 - need, nd0, need)) ok = true;
        }
        memo.set(key, ok ? 2 : 1);
        return ok;
    
}export function minMaxWaitingTime(demand: any, fuel: any): any {
        dem = demand;
        n = demand.length;
        let f0 = fuel[0], f1 = fuel[1];
        if (f0 < demand[0] && f1 < demand[0]) return -1;
        memo.clear();
        bestServe = maxServe(0, f0, f1, 0, 0);
        if (bestServe == 0) return -1;
        let lo = 0, hi = 0;
        for (const x of demand) hi += x;
        let ans = hi;
        while (lo <= hi) {
            let mid = (lo + hi) / 2;
            W = mid;
            memo.clear();
            if (canWithW(0, f0, f1, 0, 0)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    
}
