object Solution {
  def numTeams(rating: Array[Int]): Int = rating.indices.map { j => val l = rating.take(j); val r = rating.drop(j+1); l.count(_ < rating(j)) * r.count(_ > rating(j)) + l.count(_ > rating(j)) * r.count(_ < rating(j)) }.sum
}
