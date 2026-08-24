// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

export function escapeGhosts(ghosts: number[][], target: number[]): boolean {
    const targetDist = Math.abs(target[0]) + Math.abs(target[1]);
    for (const ghost of ghosts) {
        if (Math.abs(ghost[0] - target[0]) + Math.abs(ghost[1] - target[1]) <= targetDist) {
            return false;
        }
    }
    return true;
}
