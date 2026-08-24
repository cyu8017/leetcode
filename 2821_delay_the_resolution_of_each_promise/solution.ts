// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/

export function delayAll(functions: any, ms: number): any {
    return functions.map((fn) => {
        return async function() {
            try {
                const result = await fn();
                await new Promise((r) => setTimeout(r, ms));
                return result;
            } catch (err) {
                await new Promise((r) => setTimeout(r, ms));
                throw err;
            }
        };
    });
}
