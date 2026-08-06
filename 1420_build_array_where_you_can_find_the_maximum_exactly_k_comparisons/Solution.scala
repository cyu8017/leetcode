object Solution {
  def numOfArrays(n: Int, m: Int, k: Int): Int = { val mod=1000000007; var dp=Array.fill(k+1,m+1)(0); for(x<-1 to m)dp(1)(x)=1; for(_<-1 until n){val nx=Array.fill(k+1,m+1)(0); for(c<-1 to k){var p=0;for(mx<-1 to m){p=(p+dp(c-1)(mx-1))%mod;nx(c)(mx)=((mx.toLong*dp(c)(mx)+p)%mod).toInt}};dp=nx}; dp(k).foldLeft(0)((a,b)=>(a+b)%mod) }
}
