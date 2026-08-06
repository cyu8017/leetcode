object Solution {
  def maxScore(s: String): Int = { var ones=s.count(_=='1'); var zeros=0; var ans=0; for(i<-0 until s.length-1){if(s(i)=='0')zeros+=1 else ones-=1;ans=math.max(ans,zeros+ones)};ans }
}
