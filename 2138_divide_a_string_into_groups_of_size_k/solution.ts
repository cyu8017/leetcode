// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

export function divideString(s: string, k: number, fill: string): string[] {
    const ans = [];
    for (let i = 0; i < s.length; i += k) {
        if (i + k <= s.length) ans.push(s.substring(i, i + k));
        else {
            let chunk = s.substring(i);
            while (chunk.length < k) chunk += fill;
            ans.push(chunk);
        }
    }
    return ans;
}
