// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

const POS = (() => {
    const pos = new Map();
    const keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < keys[i].length; j++) {
            pos.set(keys[i][j], [i, j]);
        }
    }
    return pos;
})();
export function totalDistance(s: any): any {
    let pre = 'a', ans = 0;
    for (const cur of s) {
        const p1 = POS.get(pre), p2 = POS.get(cur);
        ans += Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
        pre = cur;
    }
    return ans;
}
