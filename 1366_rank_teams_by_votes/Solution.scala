object Solution {
  def rankTeams(votes: Array[String]): String = {
    val ranks = votes.head.indices
    val counts = votes.head.map(team => team -> Array.fill(votes.head.length)(0)).toMap
    votes.foreach(vote => vote.indices.foreach(i => counts(vote(i))(i) += 1))
    counts.keys.toSeq.sortWith((a, b) => {
      val index = ranks.find(i => counts(a)(i) != counts(b)(i))
      index.map(i => counts(a)(i) > counts(b)(i)).getOrElse(a < b)
    }).mkString
  }
}
