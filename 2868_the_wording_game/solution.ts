// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

export function canAliceWin(a: string[], b: string[]): boolean {
    let i = 0, j = 0;
    let last = String.fromCharCode(0);
    let alice = true;
    while (true) {
        if (alice) {
            while (i < a.length && a[i][0] <= last) i++;
            if (i === a.length) return false;
            last = a[i][a[i].length - 1];
            i++;
        } else {
            while (j < b.length && b[j][0] <= last) j++;
            if (j === b.length) return true;
            last = b[j][b[j].length - 1];
            j++;
        }
        alice = !alice;
    }
}
