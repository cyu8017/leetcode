object Solution {
  def maxSatisfaction(satisfaction: Array[Int]): Int = { var sum=0; var ans=0; satisfaction.sorted(Ordering.Int.reverse).takeWhile { x => if(sum+x <= 0) false else { sum += x; ans += sum; true } }; ans }
}
