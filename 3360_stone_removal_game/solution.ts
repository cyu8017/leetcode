// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

export function canAliceWin(n: any): any {
    let take = 10;
    let alice = true;
    while (n >= take && take > 0) {
        n -= take;
        take--;
        alice = !alice;
    }
    return !alice;
}
