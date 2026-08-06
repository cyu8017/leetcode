object Solution {
  def peopleIndexes(favoriteCompanies: List[List[String]]): List[Int] = {
    val sets = favoriteCompanies.map(_.toSet)
    sets.indices.filter(i => !sets.indices.exists(j => i != j && sets(i).subsetOf(sets(j)))).toList
  }
}
