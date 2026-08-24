// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/
var maxDistance = function(moves) {
        let x = 0, y = 0, z = 0;
        for (let i = 0; i < moves.length; i++) {
            let c = moves[i];
            if (c == 'U') x -= 1;
            else if (c == 'D') x += 1;
            else if (c == 'L') y -= 1;
            else if (c == 'R') y += 1;
            else z += 1;
        }
        return Math.abs(x) + Math.abs(y) + z;
    
};
