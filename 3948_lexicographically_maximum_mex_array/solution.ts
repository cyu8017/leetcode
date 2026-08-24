// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

export function maxMexArray(nums: any): any {
    const n = nums.length;
    const remaining = new Array(n + 2).fill(0);
    for (const x of nums) {
        if (x <= n + 1) remaining[x]++;
    }
    let mex = 0;
    while (remaining[mex] > 0) mex++;
    const answer = [];
    const seen = new Array(n + 2).fill(0);
    let stamp = 0, index = 0;
    while (index < n) {
        if (mex === 0) {
            answer.push(0);
            const x = nums[index];
            if (x <= n + 1) remaining[x]--;
            index++;
            continue;
        }
        stamp++;
        let need = mex;
        while (need > 0) {
            const x = nums[index];
            if (x < mex && seen[x] !== stamp) {
                seen[x] = stamp;
                need--;
            }
            if (x <= n + 1) remaining[x]--;
            index++;
        }
        answer.push(mex);
        mex = 0;
        while (remaining[mex] > 0) mex++;
    }
    return answer;
}
