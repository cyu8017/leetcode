// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const n = functions.length;
        if (n === 0) { resolve([]); return; }
        const ans = new Array(n);
        let done = 0;
        functions.forEach((fn, i) => {
            fn().then((v) => {
                ans[i] = v;
                done++;
                if (done === n) resolve(ans);
            }).catch(reject);
        });
    });
};
