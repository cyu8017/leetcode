// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

function numberOfWeakCharacters(properties: number[][]): number {
    properties = properties.slice().sort((a, b: any) => (a[0] !== b[0] ? a[0] - b[0] : b[1] - a[1]));
    let ans = 0, maxDef = 0;
    for (let i = properties.length - 1; i >= 0; i--) {
        if (properties[i][1] < maxDef) ans++;
        else maxDef = properties[i][1];
    }
    return ans;
}
