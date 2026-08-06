object Solution {
  def stoneGameIII(stoneValue: Array[Int]): String = { val dp=Array.fill[Long](stoneValue.length+1)(0); for(i <- stoneValue.length-1 to 0 by -1) { var sum=0L; dp(i)=Long.MinValue/4; for(j <- i until math.min(i+3,stoneValue.length)) { sum += stoneValue(j); dp(i)=math.max(dp(i),sum-dp(j+1)) } }; if(dp(0)>0)"Alice" else if(dp(0)<0)"Bob" else "Tie" }
}
