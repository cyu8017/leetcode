// LeetCode 3996 - Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/

export function canReach(start: any, target: any): any {
        return ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2);
    
}
