// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

object Solution {
  def accountsMerge(accounts: List[List[String]]): List[List[String]] = {
    val parent = scala.collection.mutable.HashMap.empty[String, String]
    def find(x0: String): String = {
      parent.getOrElseUpdate(x0, x0)
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    def unite(a: String, b: String): Unit = { parent(find(a)) = find(b) }
    val emailName = scala.collection.mutable.HashMap.empty[String, String]
    for (account <- accounts) {
      val name = account.head
      val first = account(1)
      var i = 1
      while (i < account.length) {
        val email = account(i)
        parent.getOrElseUpdate(email, email)
        emailName(email) = name
        unite(first, email)
        i += 1
      }
    }
    val groups = scala.collection.mutable.HashMap.empty[String, scala.collection.mutable.ArrayBuffer[String]]
    for (email <- parent.keys) {
      val root = find(email)
      groups.getOrElseUpdate(root, scala.collection.mutable.ArrayBuffer.empty[String]) += email
    }
    val result = scala.collection.mutable.ArrayBuffer.empty[List[String]]
    for (emails <- groups.values) {
      val sorted = emails.sorted
      result += (emailName(sorted.head) :: sorted.toList)
    }
    result.toList
  }
}
