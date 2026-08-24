// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution {

    fun findWinners(matches: Array<IntArray>): MutableList<MutableList<Int>> {

            var lose = HashMap<Int, Int>()
            var seen = HashSet<Int>()
            for (m in matches) {
                seen.add(m[0])
                seen.add(m[1])
                lose.put(m[1], lose.getOrDefault(m[1], 0) + 1)
            }
            var zero = ArrayList<Int>()
            var one = ArrayList<Int>()
            for (p in seen) {
                var L = lose.getOrDefault(p, 0)
                if (L == 0) zero.add(p)
                else if (L == 1) one.add(p)
            }
            zero.sort()
            one.sort()
            var ans = ArrayList<Int>()
            ans.add(zero)
            ans.add(one)
            return ans

    }

}
