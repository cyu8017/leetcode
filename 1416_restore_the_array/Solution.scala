object Solution {
  def numberOfArrays(s: String, k: Int): Int = { val mod=1000000007; val dp=Array.fill(s.length+1)(0); dp(s.length)=1; for(i <- s.length-1 to 0 by -1 if s(i)!='0') { var v=0L; for(j <- i until s.length if v<=k) { v=v*10+s(j)-'0'; if(v<=k)dp(i)=((dp(i).toLong+dp(j+1))%mod).toInt } }; dp(0) }
}
