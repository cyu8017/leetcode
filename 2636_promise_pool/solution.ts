// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

export async function promisePool(functions: any, n: any): any {
    let i = 0;
    const worker = async () => {
        while (i < functions.length) {
            const cur = i++;
            await functions[cur]();
        }
    };
    const workers = [];
    for (let k = 0; k < Math.min(n, functions.length); k++) workers.push(worker());
    await Promise.all(workers);
}
