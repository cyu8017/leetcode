object Solution {
  def numSteps(s: String): Int = { var steps=0; var carry=0; for(i <- s.length-1 to 1 by -1) { if(s(i)-'0'+carry == 1) { steps += 2; carry=1 } else steps += 1 }; steps+carry }
}
