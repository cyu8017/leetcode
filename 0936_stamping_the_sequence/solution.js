// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

/**
 * @param {string} stamp
 * @param {string} target
 * @return {number[]}
 */
var movesToStamp = function(stamp, target) {
    const m = stamp.length, n = target.length;
    const arr = target.split("");
    const done = new Array(n - m + 1).fill(false);
    const ans = [];
    let remaining = n;
    const canStamp = (i) => {
        let changed = false;
        for (let j = 0; j < m; j++) {
            if (arr[i + j] === "?") continue;
            if (arr[i + j] !== stamp[j]) return false;
            changed = true;
        }
        return changed;
    };
    const doStamp = (i) => {
        let count = 0;
        for (let j = 0; j < m; j++) {
            if (arr[i + j] !== "?") {
                arr[i + j] = "?";
                count++;
            }
        }
        return count;
    };
    while (remaining > 0) {
        let stamped = false;
        for (let i = 0; i <= n - m; i++) {
            if (!done[i] && canStamp(i)) {
                remaining -= doStamp(i);
                ans.push(i);
                done[i] = true;
                stamped = true;
                if (remaining === 0) break;
            }
        }
        if (!stamped) return [];
    }
    ans.reverse();
    return ans;
};
