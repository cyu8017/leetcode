// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

class Solution {
    fun stoneGameIX(stones: IntArray): Boolean {
var cnt: IntArray = IntArray(3)
for (s in stones) {
cnt[s % 3]++
}
if (cnt[0] % 2 == 0) {
return cnt[1] > 0 && cnt[2] > 0
}
return kotlin.math.abs(cnt[1] - cnt[2]) > 2
}
}
