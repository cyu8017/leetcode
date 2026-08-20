// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator(characters: String, combinationLength: Int) {
  private val items = characters.combinations(combinationLength).toIterator
  private var nextItem: Option[String] = if (items.hasNext) Some(items.next()) else None

  def next(): String = {
    val current = nextItem.get
    nextItem = if (items.hasNext) Some(items.next()) else None
    current
  }

  def hasNext(): Boolean = nextItem.isDefined
}
