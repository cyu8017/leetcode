class Solution { fun reverseBits(n: Int): Int { var x = n; var ans = 0; repeat(32) { ans = (ans shl 1) or (x and 1); x = x ushr 1 }; return ans } }
