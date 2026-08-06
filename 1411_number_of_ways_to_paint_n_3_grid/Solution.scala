object Solution {
  def numOfWays(n: Int): Int = { val mod=1000000007L; var aba=6L; var abc=6L; for(_ <- 1 until n) { val x=(3*aba+2*abc)%mod; abc=(2*aba+2*abc)%mod; aba=x }; ((aba+abc)%mod).toInt }
}
