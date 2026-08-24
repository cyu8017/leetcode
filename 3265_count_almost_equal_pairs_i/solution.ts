// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

export function countPairs(nums: any): any {
    const sprintfNum = (x) => String(x);
    const almostEqual = (a, b) => {
        let sa = sprintfNum(a), sb = sprintfNum(b);
        while (sa.length < sb.length) sa = '0' + sa;
        while (sb.length < sa.length) sb = '0' + sb;
        const diff = [];
        for (let i = 0; i < sa.length; i++) if (sa[i] !== sb[i]) diff.push(i);
        if (diff.length === 0) return true;
        if (diff.length !== 2) return false;
        const i0 = diff[0], j = diff[1];
        return sa[i0] === sb[j] && sa[j] === sb[i0];
    };
    let ans = 0;
    for (let i = 0; i < nums.length; i++)
        for (let j = i + 1; j < nums.length; j++)
            if (almostEqual(nums[i], nums[j])) ans++;
    return ans;
}
